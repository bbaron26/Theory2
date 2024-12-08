from ntm.parser_bbaron2 import NTMParser
from ntm.simulator_bbaron2 import NTM, NTMSimulator

def run_simulation(csv_file, input_string, max_depth=50):
    #parse the csv file
    config = NTMParser.parse(csv_file)
    ntm = NTM(
        config["name"], 
        config["states"], 
        config["start_state"], 
        config["accept_state"], 
        config["reject_state"], 
        config["transitions"]
    )
    #simulate the Turing machine
    simulator = NTMSimulator(ntm, input_string, max_depth)
    return simulator.simulate()

