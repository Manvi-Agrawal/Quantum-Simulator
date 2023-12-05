# PROGRAM PROPERTIES
# miller_11.qasm 3 qubits 54 lines
# decod24-v2_43.qasm 4 qubits 56 lines
# one-two-three-v3_101.qasm 5 qubits 74 lines
# hwb5_53.qasm 6 qubits 1,340 lines
# alu-bdd_288.qasm 7 qubits 88 lines
# f2_232.qasm 8 qubits 1,210 lines
# con1_216.qasm 9 qubits 958 lines
# mini_alu_305.qasm 10 qubits 177 lines
# wim_266.qasm 11 qubits 990 lines
# cm152a_212.qasm 12 qubits 1,225 lines
# squar5_261.qasm 13 qubits 1,997 lines
# sym6_316.qasm 14 qubits 274 lines
# rd84_142.qasm 15 qubits 347 lines
# cnt3-5_179.qasm 16 qubits 179 lines

# EXECUTION DATA...
# miller_11.qasm 70.7868
# decod24-v2_43.qasm 84.7827
# one-two-three-v3_101.qasm 78.8053
# hwb5_53.qasm 60.601
# alu-bdd_288.qasm 58.4354
# f2_232.qasm 116.8259
# con1_216.qasm 85.5444
# mini_alu_305.qasm 84.6055
# wim_266.qasm 84.2334
# cm152a_212.qasm 63.316
# squar5_261.qasm 84.064
# sym6_316.qasm 91.901
# rd84_142.qasm 83.2423
# cnt3-5_179.qasm 78.1452

import numpy as np
import matplotlib.pyplot as plt

execution_times = {"miller_11.qasm": 70.7868,
"decod24-v2_43.qasm": 84.7827,
"one-two-three-v3_101.qasm": 78.8053,
"hwb5_53.qasm": 60.601,
"alu-bdd_288.qasm": 58.4354,
"f2_232.qasm": 116.8259,
"con1_216.qasm": 85.5444,
"mini_alu_305.qasm": 84.6055,
"wim_266.qasm": 84.2334,
"cm152a_212.qasm": 63.316,
"squar5_261.qasm": 84.064,
"sym6_316.qasm": 91.901,
"rd84_142.qasm":83.2423,
"cnt3-5_179.qasm": 78.1452
}

plt.plot(execution_times.keys(), execution_times.values(), label="Execution times")
plt.title("Execution Times for custom simulator")
plt.xlabel("QASM programs...")
plt.ylabel("Execution Time(in milliseconds)...")
plt.tick_params(axis='both', which='major', labelsize=6)
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.show()
