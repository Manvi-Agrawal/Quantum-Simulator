from bitset import Bitset

class WeightedKet:
    def __init__(self, length):
        self.length = length
        self.amplitude = 1.0 + 0.0 * 1j
        self.ket = Bitset(length)

    def __str__(self) -> str:
        return f"{self.amplitude} * {self.ket}"
    
    def amplitude_change(self, factor):
        self.amplitude *= factor
