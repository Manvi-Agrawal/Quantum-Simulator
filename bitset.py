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
