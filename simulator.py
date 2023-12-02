import copy
import numpy as np


qasm_file = 'qasm/sample3.qasm'
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
            # print(f"Execute bit flip on {arg}")
            if self.bits[arg] == '0':
                self.bits[arg] = '1'
            else:
                self.bits[arg] = '0'
    
    def __str__(self) -> str:
        return ''.join(self.bits)


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
            wk.ket.bit_flip(op.args[0])

        if (op.gate == "h"):
            print("H gate  detected...")
            # print(f"wk before amp change:{wk}")
            wk.amplitude_change(1/np.sqrt(2))
            # print(f"wk after amp change:{wk}")


            wk_new = copy.deepcopy(wk)
            
            wk_new.ket.bit_flip(op.args[0])
            # wk_new.amplitude_change(1/np.sqrt(2))

            # TODO: if (wk.ket.get(op.arg1)) 
            if wk.ket.bits[op.args[0]] == '1':
                wk.amplitude_change(-1)

            res.append(wk_new)

        if op.gate == "cx":
            if wk.ket.bits[op.args[0]] == '1':
                wk.ket.bit_flip(op.args[1])


    return res


def consolidate(state):
    res = []

    i = 0
    N = len(state)
    
    while i < N - 1:
        amp_net = state[i].amplitude

        while i<N-1 and str(state[i].ket) == str(state[i+1].ket):
            # print(f"Adding {state[i+1].amplitude} to {amp_net}")
            amp_net += state[i+1].amplitude
            i += 1
        
        state[i].amplitude = amp_net
        res.append(state[i])
        i = i+1

    if str(res[-1].ket) != str(state[N-1].ket):
        res.append(state[N-1])
     
    return res


def parse_register(reg):
    reg = reg.strip()[:-1]
    args = reg.split(",")
    return [int(x[1:].lstrip('[').rstrip(']')) for x in args]


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
        num_bits = args[0]
        print(f"Added |0>^{num_bits}")
        state.append(WeightedKet(num_bits))


    # Skip Qreg and Creg allocation
    lines = lines[2:]
    
    # Process Op data
    for line in lines:
        print(f"----{line}-----")
        (gate, reg) = line.split(" ")

        if gate in ['x', 'h', 'cx']:
            args = parse_register(reg)
            # si = WeightedKet(num_bits)
            op = Operation(gate, args)
            state = step(op, state)
            display_state(state)

        state.sort(key=lambda x: "".join(x.ket.bits))
        print("After sort")
        display_state(state)

        state = consolidate(state)
        print("After consolidate")
        display_state(state)

    # print(f"Len : {len(state)}")    



with open(qasm_file, "r") as f:
    qasm_string = f.read()
    simulate(qasm_string)
