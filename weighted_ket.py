from bitset import Bitset

class WeightedKet:
    def __init__(self, length, amplitude = 1.0 + 0.0*(1j), ket = None):
        self.length = length
        self.amplitude = amplitude

        if ket is None:
            self.ket = Bitset(['0']*length)
        else:
            self.ket = ket
            self.length = len(ket.bits)

    def __str__(self) -> str:
        return f"{self.amplitude} * {self.ket}"
    
    def amplitude_change(self, factor):
        self.amplitude *= factor
