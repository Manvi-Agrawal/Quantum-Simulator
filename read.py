

qasm_file = 'qasm/sample2.qasm'


def parse_register(reg):
    print(f"Parsing reg: {reg}")
    return int(reg[1:].lstrip('[').rstrip('];') )


with open(qasm_file, "r") as f:
    qasm_string = f.read()

print(f"----{repr(qasm_string)}----------")

# lines = qasm_string.split("\n")

for line in qasm_string.split('\n'):
    print(f"----{line}----------")


# with open(filename) as file:

#     data = file.readline()
#     while data != "":
#         print(f"---{data}")
#         data = file.readline()
    # data1 = file.readline()
    # print(f"---{data1}")

    # data2 = file.readline()
    # print(f"-------{data2}")

    # data3 = file.readline()
    # print(f"-------{data3}")

    # data4 = file.readline()
    # print(f"-------{data4}")

    # data5 = file.readline()
    # print(f"-------{data5}")

    # data6 = file.readline()
    # print(f"-------{data6}")
    