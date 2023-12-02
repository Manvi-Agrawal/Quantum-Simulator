import numpy as np
from copy import copy, deepcopy

from weighted_ket import WeightedKet




class QuantumState:
    def __init__(self, num_bits) -> None:
        self.state = [WeightedKet(num_bits)]

        
    def step(self, op):
        # Note : Making a copy here to be able to influence the original amptitudes when using H gate
        res = copy(self.state)
        print(f"Len(self.state) in step : {len(self.state)}")
        for wk in self.state:
            if (op.gate == "x"):
                print("X gate  detected...")
                wk.ket.bit_flip(op.args[0])

            if (op.gate == "h"):
                print("H gate  detected...")
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
                print("T gate  detected...")
                if wk.ket.bits[op.args[0]] == '1':
                    # >>> np.exp(-0.25*np.pi*1j)
                    # (0.7071067811865476-0.7071067811865476j)
                    wk.amplitude_change(np.exp(-0.25*np.pi*1j))

            if (op.gate == "tdag"):
                print("Tdag gate  detected...")
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
        
    

    def display_state(self):
        for bitset in self.state:
            print(f"{bitset} + ")

