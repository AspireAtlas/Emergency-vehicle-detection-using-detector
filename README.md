# Emergency Vehicle Traffic Signal Simulation

This repository contains a simulation for handling emergency vehicle priority at traffic lights using SUMO (Simulation of Urban MObility). The simulation detects the presence of an emergency vehicle and adjusts the traffic signal phases accordingly to give it priority. The simulation is built using Python and the SUMO traffic simulation tool.

## Project Structure

- **demo.py**: Main Python script to run the SUMO simulation. It interacts with SUMO via the traci interface, detects emergency vehicles, and alters the traffic signal behavior.
- **demo.sumocfg**: Configuration file for the SUMO simulation.
- **demo.net.xml**: Network file that defines the road network used in the simulation.
- **tripinfo.xml**: This file logs trip-related data for the vehicles in the simulation.

## Requirements

- **SUMO (Simulation of Urban MObility)**: Make sure to have SUMO installed and the `SUMO_HOME` environment variable set.
- **Python**: This simulation uses Python to control SUMO through its TraCI (Traffic Control Interface) API.

## How to Run the Simulation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/emergency-vehicle-simulation.git
   cd emergency-vehicle-simulation
   ```

2. **Set up SUMO Environment**:
   Make sure your SUMO_HOME environment variable is properly set. For example:
   ```bash
   export SUMO_HOME=/path/to/sumo
   ```

3. **Run the Simulation**:
   The simulation can be run in both GUI and non-GUI mode.
   
   For GUI mode (with SUMO graphical interface):
   ```bash
   python demo.py
   ```
   
   For command-line mode (without SUMO graphical interface):
   ```bash
   python demo.py --nogui
   ```
   
4. **Logic**:
   The simulation includes induction loop detectors placed on the road.
   The system continuously monitors these detectors to identify vehicles of type "ev" (emergency vehicles).
   Once an emergency vehicle is detected, the traffic signal phase changes to green for the lane that the emergency vehicle is approaching, allowing it to pass through the junction.
