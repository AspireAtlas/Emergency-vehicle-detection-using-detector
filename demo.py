import os
import sys
import optparse
import time

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="Run the command-line version of SUMO")
    options, args = opt_parser.parse_args()
    return options

def run():
    Step = 0
    emergency_vehicle_detected = False  
    emergency_vehicle_passed = False    
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        print(Step)
        det_ev = traci.inductionloop.getLastStepVehicleIDs("det_0")

        for i in det_ev:
            if traci.vehicle.getTypeID(i) == "ev":
                print("Emergency vehicle detected")
                emergency_vehicle_detected = True  
                break  
        
        if emergency_vehicle_detected and not emergency_vehicle_passed:
            # Check the current phase of the traffic light
            current_phase = traci.trafficlight.getPhase("J1")  
            if current_phase == 0:  # Red phase
                # Change traffic light to green for emergency vehicle passage
                traci.trafficlight.setPhase("J1", 2)  
                
                emergency_vehicle_detected = False  
                #time.sleep(10)  # Assuming delay for the emergency vehicle to pass
                
                # Check if the emergency vehicle has passed after the delay
                passed = False
                timeout = time.time() + 20  # Timeout to prevent infinite loop
                while time.time() < timeout:
                    traci.simulationStep()
                    det_ev = traci.inductionloop.getLastStepVehicleIDs("det_1") 
                    if any(traci.vehicle.getTypeID(i) == "ev" for i in det_ev):
                        passed = True
                        break

                if passed:
                    # Revert traffic light to its original phase if emergency vehicle has passed
                    traci.trafficlight.setPhase("J1", current_phase)  
                    emergency_vehicle_passed = True  
        
        Step += 1
    traci.close()
    sys.stdout.flush()

if __name__ == "__main__":
    options = get_options()

    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "demo.sumocfg", "--tripinfo-output", "tripinfo.xml"])
    run()

