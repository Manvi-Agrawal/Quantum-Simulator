import copy
import numpy as np


qasm_file = 'qasm/sample2.qasm'
# Let state be global variable
# state = []



class Operation:
    def __init__(self, gate, args):
        self.gate = gate
        self.args = args


class Bitset:
    def __init__(self, length):
        self.length = length
        self.bits = ['0']*length
    
    def bit_flip(self, arg):
            print(f"Execute bit flip on {arg}")
            if self.bits[arg] == '0':
                self.bits[arg] = '1'
            else:
                self.bits[arg] = '0'
    
    def __str__(self) -> str:
        return f"|{''.join(self.bits)}>"


class WeightedKet:
    def __init__(self, length):
        self.length = length
        self.amplitude = 1.0 + 0.0 * 1j
        self.ket = Bitset(length)

    def __str__(self) -> str:
        return f"{self.amplitude} * {self.ket}"
    
    def amplitude_change(self, factor):
        self.amplitude *= factor

def step(op, state):
    # Note : Making a copy here to be able to influence the original amptitudes when using H gate
    res = copy.copy(state)
    print(f"Len(state) in step : {len(state)}")
    for wk in state:
        if (op.gate == "x"):
            print("X gate  detected...")
            wk.ket.bit_flip(op.args)

        if (op.gate == "h"):
            print("H gate  detected...")
            # print(f"wk before amp change:{wk}")
            wk.amplitude_change(1/np.sqrt(2))
            # print(f"wk after amp change:{wk}")


            wk_new = copy.deepcopy(wk)
            
            wk_new.ket.bit_flip(op.args)
            # wk_new.amplitude_change(1/np.sqrt(2))


            if wk.ket.bits[op.args] == '1':
                wk.amplitude_change(-1)

            res.append(wk_new)
    return res



def parse_register(reg):
    return int(reg.strip()[1:-1].lstrip('[').rstrip(']') )


def display_state(state):
    for bitset in state:
        print(f"{bitset} + ")


# Cirq result : [0j, (1+0j)]
def simulate(qasm_string):
    state = []
    # Skip boilerplate
    lines = qasm_string.split('\n')[2:-1]

    # Qreg allocation
    (alloc, reg) = lines[0].split(" ")
    if alloc == 'qreg':
        args = parse_register(reg)
        num_bits = args
        print(f"Added |0>^{num_bits}")
        state.append(WeightedKet(num_bits))


    # Skip Qreg and Creg allocation
    lines = lines[2:]
    
    # Process Op data
    for line in lines:
        print(f"----{line}-----")
        (gate, reg) = line.split(" ")

        if gate in ['x', 'h']:
            args = parse_register(reg)
            # si = WeightedKet(num_bits)
            op = Operation(gate, args)
            state = step(op, state)
            display_state(state)

        state.sort(key=lambda x: "".join(x.ket.bits))
        print("After sort")
        display_state(state)

        # consolidate()

    # print(f"Len : {len(state)}")    



with open(qasm_file, "r") as f:
    qasm_string = f.read()
    simulate(qasm_string)
