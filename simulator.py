from operation import Operation
from state import QuantumState

import numpy as np
import sys


def parse_register(reg):
    reg = reg.strip()[:-1]
    args = reg.split(",")
    return [int(x[1:].lstrip('[').rstrip(']')) for x in args]

# Cirq result : [0j, (1+0j)]
def simulate(qasm_string):
    # state = []
    # Skip boilerplate
    lines = qasm_string.split('\n')[2:-1]

    # Qreg allocation
    (alloc, reg) = lines[0].split(" ")
    if alloc == 'qreg':
        args = parse_register(reg)
        num_bits = args[0]
        # print(f"Added |0>^{num_bits}")
        state = QuantumState(num_bits)


    # Skip Qreg and Creg allocation
    lines = lines[2:]

    # Track the max index of register used to truncate statevector
    max_register_index = 0
    
    # Process Op data
    for line in lines:
        # print(f"----{line}-----")
        (gate, reg) = line.split(" ")

        if gate in ['x', 'h', 'cx', 't', 'tdg']:
            args = parse_register(reg)

            max_register_index = max(args + [max_register_index])

            # si = WeightedKet(num_bits)
            op = Operation(gate, args)
            state.step(op)
            # state.display_state()

        state.sort()
        # print("After sort")
        # state.display_state()


        state.consolidate()
        # print("After consolidate")
        # state.display_state()

    result = state.state_vector(max_register_index+1)

    # print(f"res = {result}... \n Final State ...")
    # state.display_state()

    statevector = list(np.around(result, 3))
    return statevector

    # print(f"Len : {len(state)}")    


if __name__ == "__main__":
    qasm_file = sys.argv[1]

    with open(qasm_file, "r") as f:
        qasm_string = f.read()
        result = simulate(qasm_string)
        print(result)