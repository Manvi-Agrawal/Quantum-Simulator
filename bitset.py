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
    
    def truncate(self, new_length):
         self.bits = self.bits[:new_length]

    def __str__(self) -> str:
        return ''.join(self.bits)
    
    def __eq__(self, other): 
        if not isinstance(other, Bitset):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.length == other.length and str(self) == str(other)
