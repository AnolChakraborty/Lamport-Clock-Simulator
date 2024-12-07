# Lamport Clock Simulator

## Overview
Welcome to the **Lamport Clock Simulator**! This Python project simulates the concept of Lamport clocks in a distributed system environment, allowing you to create local events, send time-stamped messages to other processes, and observe how the Lamport timestamps are updated. It provides an interactive, socket based locally distributed, & a sleek terminal-based user interface that helps in understanding the synchronization between distributed systems.

![Lamport Clock Simulator](https://img.shields.io/badge/Project-Lamport%20Clock%20Simulator-blue)

### Features
- **Interactive TUI**: Built using the `rich` Python library for a beautiful and interactive terminal interface.
- **Lamport Clock Implementation**: Simulates the behavior of logical clocks.
- **Real-time Communication**: Supports sending and receiving time-stamped messages between real python processes.
- **Event Handling**: Trigger local events and simulate message exchanges.
- **Port Validation**: Checks if the port is available, ensuring no conflicts.
- **Logs**: Maintains a detailed event comunication log between the processes.


![Python version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub stars](https://img.shields.io/github/stars/AnolChakraborty/Lamport-Clock-Simulator?style=social)
![GitHub forks](https://img.shields.io/github/forks/AnolChakraborty/Lamport-Clock-Simulator?style=social)
![GitHub issues](https://img.shields.io/github/issues/AnolChakraborty/Lamport-Clock-Simulator)
![GitHub pull requests](https://img.shields.io/github/issues-pr/AnolChakraborty/Lamport-Clock-Simulator)
![Last commit](https://img.shields.io/github/last-commit/AnolChakraborty/Lamport-Clock-Simulator)
![License](https://img.shields.io/badge/License-MIT-blue)




https://github.com/user-attachments/assets/97e190fc-06e4-4c5f-bd15-6f9e892fc3fa






## Installation
Clone this repository and install the dependencies using the following steps:

### Step 1: Clone the Repository
```bash
git clone https://github.com/AnolChakraborty/Lamport-Clock-Simulator.git
cd Lamport-Clock-Simulator
```

### Step 2: Install Required Python Packages
Make sure you have Python 3.8 or higher installed. Then, install the required packages using `pip`:
```bash
pip install rich
```

## How to Run

> **_NOTE:_**  Use a terminal with True Colour support for the best experience.

To start the simulator, run the following command in your terminal:

```bash
python3 main.py
```

### User Instructions
The **Lamport Clock Simulator** is a terminal-based user interface (TUI) application. When you run the application, you will interact with it entirely through your terminal window. Below is a step-by-step guide on how to use the application:

1. **Port Configuration**:
   - The first prompt will ask you to enter a valid port number for this process. Ensure that the port number is between 1024 and 65535 and is not currently in use.
  
2. Multiple Sessions:
   - To simulate interactions between multiple processes, open separate terminal sessions and run the simulator on different ports. For example:
     In one terminal, run the simulator on port 5000:
      ```bash
      python3 main.py
      ```
      In another terminal, run the simulator on port 5001:
      ```bash
      python3 lamport_clock_simulator.py
      ```
      Simillarly run as many instance you want of the same program with different port number.
This setup will allow you to simulate the behavior of multiple distributed processes communicating with each other in your local systen.

3. **Event Options**:
   - Once configured, you will be presented with two main options:
     - `l`: Trigger a local event that increments the Lamport clock. This action updates the logical time of the process.
     - `s`: Send a message to another process with the current Lamport clock time.

4. **Sending Messages**:
   - If you choose to send a message (`s`), you will be prompted to input the destination port. The application checks if the port is valid and attempts to establish a connection.
   - If successful, the message containing the sender's port and the Lamport time is sent to the destination.

5. **Viewing Logs**:
   - The terminal will display a log of the last 10 events, including timestamps, sender/receiver details, and actions performed. This helps you track the sequence of events in the simulation.

### How It Works
1. **Port Configuration**: When prompted, enter a valid port number for this process.
2. **Event Options**:
   - `l`: Trigger a local event to increment the Lamport clock.
   - `s`: Send a message to another process with the current Lamport time.
3. **View Logs**: The terminal will display the last 10 events, including timestamps and sender/receiver information.

## Screenshots
### Initial Welcome Screen
![Welcome Screen](https://i.imghippo.com/files/Anz3107pAA.png)

### In Action
![Event Options](https://i.imghippo.com/files/GX3796vyU.png)

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- This project is done on behalf of our academic requirement of the subject `Distributed Systems - CSE1817OE31`
- **Rich** library for making terminal applications visually appealing.
- Concept of **Lamport Clocks** for logical time synchronization.

## Contact
For questions or comments, please reach out to [Anol Chakraborty](https://www.linkedin.com/in/anolchakraborty/) or create an issue in the repository.

---

### View the Project on [GitHub](https://github.com/AnolChakraborty/Lamport-Clock-Simulator)

