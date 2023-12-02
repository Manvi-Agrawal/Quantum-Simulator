class Operation:
    def __init__(self, gate, args):
        self.gate = gate
        self.args = args


class Bitset:
    def __init__(self, length):
        self.length = length
        self.bits = ['0']*length
    
    def bit_flip(self, arg):
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


def step(op, state):
    for wk in state:
        if (op.gate == "x"):
            wk.ket.bit_flip(op.args)
        # if (op.gate == "h"):
            # wk.ket.flip(op.args)




qasm_file = 'qasm/sample.qasm'


def parse_register(reg):
    return int(reg.strip()[1:-1].lstrip('[').rstrip(']') )



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

        if gate == 'x':
            args = parse_register(reg)
            # si = WeightedKet(num_bits)
            op = Operation(gate, args)
            step(op, state)
        # state.sort()
        # consolidate()


    for bitset in state:
        print(f"{bitset} + ")


with open(qasm_file, "r") as f:
    qasm_string = f.read()
    simulate(qasm_string)
