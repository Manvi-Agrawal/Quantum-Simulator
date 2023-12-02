import copy

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self, greeting="hello"):
        pre = copy.copy(self)
        pre.name=greeting
        return pre
    

def parse_register(reg):
    reg = reg.strip()[:-1]
    args = reg.split(",")
    return [int(x[1:].lstrip('[').rstrip(']')) for x in args]

# s1 = Student("Bob")
# s2 = copy.copy(s1)
# s2.name="Alice"
# s2.greet()
# print(s1.name)

res = parse_register("q[1];")
print(res)
    