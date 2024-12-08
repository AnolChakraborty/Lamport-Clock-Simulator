import os
import socket
import threading
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

class LamportClock:
    def __init__(self):
        self.time = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.time += 1
            return self.time

    def update(self, t):
        with self.lock:
            self.time = max(t, self.time) + 1
            return self.time

console = Console()

# A list to store message logs for the TUI
message_log = []

thread_ready_event = threading.Event()

def is_port_available(port):
    """Check if the given port is free and can be bound to a socket."""
    try:
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.bind(('localhost', port))
        test_socket.close()
        return True
    except socket.error:
        return False

def is_valid_port(port, check = 0):
    """Validate that the port number is an integer, within the valid range, and free."""
    try:
        port = int(port)
        if 1024 <= port <= 65535:
            if check is 1:
                return True
            if is_port_available(port):
                return True
            else:
                console.print("[bold red]Error: Port number is already in use.[/bold red]")
                return False
        else:
            console.print("[bold red]Error: Port number must be between 1024 and 65535.[/bold red]")
            return False
    except ValueError:
        console.print("[bold red]Error: Port number must be an integer.[/bold red]")
        return False

def receive_message(lc, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('localhost', int(port)))
        server_socket.listen(5)
    except socket.error as e:
        console.print(f"[bold red]Error: Unable to bind to port {port}. {e}[/bold red]")
        return

    console.print(Panel(Text(f"Listening for incoming messages at port {port}", style="bold green", justify="center"), title="Lamport Clock Simulator", border_style="green"))

    thread_ready_event.set()

    while True:
        try:
            conn, _ = server_socket.accept()
            data = conn.recv(1024).decode()
            if data:
                sender_port, t = data.strip().split(',')
                sender_port = int(sender_port)
                t = int(t)
                new_time = lc.update(t)

                # Add the message to the message log for display
                message_log.append(f"Time {new_time} | Message received from port {sender_port}")
                
                # Update the message table (no clearing here)
                display_message_log(port=port, check=0)
        except Exception as e:
            console.print(f"[bold red]Error receiving message: {e}[/bold red]")
        finally:
            conn.close()

def create_custom_prompt_message():
    # Base message
    message = Text("Please enter event type: ", style="bold cyan")
    
    # Choices styled differently
    choices = Text("[l/s] ", style="bold bright_white")  # Mimic default Prompt.ask styles
    
    # Default value
    default = Text("(default: l)", style="dim white")
    
    # Combine all parts
    full_message = message + choices + default
    
    # Convert Text object to a plain string with formatting codes
    return full_message


def handle_events(lc, sender_port):
    while True:
        console.print(Panel.fit(Text("Available events: `l` - local event or `s` - send message", style="bold cyan", justify="center"), title_align="left", title="Event Options", border_style="cyan"))
        event = Prompt.ask(create_custom_prompt_message(), choices=["l", "s"], default="l", show_choices=False, show_default=False)

        if event == "l":
            new_time = lc.increment()
            message_log.append(f"Time {new_time} | Local event triggered")
            display_message_log(port=sender_port)
        elif event == "s":
            while True:
                port = Prompt.ask("[bold cyan]Please type the destination port")
                
                # Check if the destination port is the same as the sender's port
                if port == str(sender_port):
                    console.print("[bold red]Error: Cannot send a message to the same port.[/bold red]")
                    continue  # Skip to the next iteration of the loop

                if is_valid_port(port, check=1):
                    try:
                        address = ("localhost", int(port))
                        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client_socket.connect(address)
                        new_time = lc.increment()
                        # Send both the sender's port and the time as part of the message
                        client_socket.sendall(f"{sender_port},{new_time}\n".encode())
                        message_log.append(f"Time {new_time} | Message sent to port {port}")
                        client_socket.close()
                        display_message_log(port=sender_port)
                        break  # Exit the loop if the connection is successful
                    except (socket.error, ConnectionRefusedError) as e:
                        console.print(f"[bold red]Connection error to port {port}: {e}[/bold red]")
                    except Exception as e:
                        console.print(f"[bold red]Unexpected error: {e}[/bold red]")
        elif event == "0xPixiE":
            continue
        else:
            console.print("[bold red]Error: Please type 'l' or 's'[/bold red]")


def display_message_log(port, check=1):
    # Display only the message table, keeping the prompt fixed at the top
    console.clear()

    # Create a table for the message log
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Event", style="dim", width=40)
    table.add_column("Timestamp", style="green")

   # Calculate the starting serial number for the last 10 messages
    total_messages = len(message_log)
    start_index = max(total_messages - 10, 0) + 1  # Ensure no negative start_index

    for i, msg in enumerate(message_log[-10:], start=start_index):  # Continue numbering from the correct serial
        table.add_row(str(i), msg)

    # Display the prompt section at the top
    console.print(Panel(Text(f"Listening for incoming messages at port {port}", style="bold green", justify="center"), title="Lamport Clock Simulator", border_style="green"))

    # Display the message table below the prompt
    console.print(table)

    if check is 0:
        console.print(Panel.fit(Text("Available events: `l` - local event or `s` - send message", style="bold cyan", justify="center"), title_align="left", title="Event Options", border_style="cyan"))
        console.print(create_custom_prompt_message() + " : ", end="")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    link_text = Text("View at GitHub", style="bold blue")
    link_text.stylize("link https://github.com/AnolChakraborty/Lamport-Clock-Simulator", 0, len(link_text))
    
    console.print(Panel(Text("Welcome to lamport clock simulator", style="bold yellow", justify="center"), title="❁ ❁ स्वागतम् ❁ ❁", subtitle=Text("Ⓒ Anol Chakraborty | ") + link_text, border_style="yellow", padding=(1,0,1,0)))

    while True:
        port = Prompt.ask("[bold red]Please enter a port number for this process")
        if is_valid_port(port):
            break  # Exit the loop if the port is valid

    lc = LamportClock()

    os.system('cls' if os.name == 'nt' else 'clear')

    threading.Thread(target=receive_message, args=(lc, port), daemon=True).start()
    thread_ready_event.wait()
    handle_events(lc, port)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Panel(Text("Exiting lamport clock simulator, Goodbye !", style="bold cyan", justify="center"), subtitle="💮 💮 Adios 💮 💮", border_style="cyan"))