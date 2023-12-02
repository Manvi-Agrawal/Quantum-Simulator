import numpy as np
from copy import copy, deepcopy

from weighted_ket import WeightedKet
from bitset import Bitset


def generate_redundant_states(N):
    res = []
    for n in range(2**N):
        bstr = format(n, f'0{N}b')
        bstr = [b for b in bstr]
        s = WeightedKet(N, amplitude = 0.0 + 0.0*(1j), ket = Bitset(bstr))
        res.append(s)
    return res


class QuantumState:
    def __init__(self, num_bits) -> None:
        self.state = [WeightedKet(num_bits)]

        
    def step(self, op):
        # Note : Making a copy here to be able to influence the original amptitudes when using H gate
        res = copy(self.state)
        # print(f"Len(self.state) in step : {len(self.state)}")
        for wk in self.state:
            if (op.gate == "x"):
                # print("X gate  detected...")
                wk.ket.bit_flip(op.args[0])

            if (op.gate == "h"):
                # print("H gate  detected...")
                # print(f"wk before amp change:{wk}")
                wk.amplitude_change(1/np.sqrt(2))
                # print(f"wk after amp change:{wk}")


                wk_new = deepcopy(wk)
                
                wk_new.ket.bit_flip(op.args[0])
                # wk_new.amplitude_change(1/np.sqrt(2))

                # TODO: if (wk.ket.get(op.arg1)) 
                if wk.ket.bits[op.args[0]] == '1':
                    wk.amplitude_change(-1)

                res.append(wk_new)

            if op.gate == "cx":
                if wk.ket.bits[op.args[0]] == '1':
                    wk.ket.bit_flip(op.args[1])

            if (op.gate == "t"):
                # print("T gate  detected...")
                if wk.ket.bits[op.args[0]] == '1':
                    # >>> np.exp(-0.25*np.pi*1j)
                    # (0.7071067811865476-0.7071067811865476j)
                    wk.amplitude_change(np.exp(-0.25*np.pi*1j))

            if (op.gate == "tdg"):
                # print("tdg gate  detected...")
                if wk.ket.bits[op.args[0]] == '1':
                    # >>> np.exp(-0.25*np.pi*1j)
                    # (0.7071067811865476-0.7071067811865476j)
                    wk.amplitude_change(np.exp(0.25*np.pi*1j))
        self.state = copy(res)

    def sort(self):
        self.state.sort(key=lambda x: "".join(x.ket.bits))


    def consolidate(self):
        res = []

        i = 0
        N = len(self.state)
        
        while i < N - 1:
            amp_net = self.state[i].amplitude

            while i<N-1 and str(self.state[i].ket) == str(self.state[i+1].ket):
                # print(f"Adding {self.state[i+1].amplitude} to {amp_net}")
                amp_net += self.state[i+1].amplitude
                i += 1
            
            self.state[i].amplitude = amp_net
            res.append(self.state[i])
            i = i+1

        if res != [] and str(res[-1].ket) != str(self.state[N-1].ket):
            res.append(self.state[N-1])

        if res == []:
            res.append(self.state[0])
        
        self.state = copy(res)
        
    # Cirq result : [0j, (1+0j)]
    def state_vector(self):
        repr = [int(str(wk.ket)[::-1], 2) for wk in self.state]
        # print(f"repr of state_vector :: {repr}")

        # print(f"max(repr) of state_vector :: {max(repr)}")


        m = 1+ int((np.log2(max(repr))))

        # print(f"repr bits: {m}")

        for wk in self.state:
            wk.ket.truncate(m)


        # print("Before extras...")
        # self.display_state()

        extras = generate_redundant_states(m)
        # print("Extras...")
        # extras.display_state()

        self.state.extend(extras)
        # print("Appended extras...")
        # self.display_state()

        self.sort()

        # print("Sort after extras...")
        # self.display_state()

        self.consolidate()
        # print("Consolidate state...")
        # self.display_state()

        return [wk.amplitude for wk in self.state]
         

    def display_state(self):
        for bitset in self.state:
            print(f"{bitset} + ")

