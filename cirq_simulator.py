import sys
import numpy as np
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm
from pathlib import Path

# Import your simulate function here.
# cs238 can be a file, a folder with an __init__.py file,
# from cs238 import simulate
from simulator import simulate

def cirq_simulate(qasm_string: str) -> list:
    """Simulate a qasm string

    Args:
        qasm_string: a string following the qasm format

    Returns:
        statevector: a list, with a complex number for
            each of the 2^num_qubits possible amplitudes
            Ordered big endian, see:
        quantumai.google/reference/python/cirq/sim/StateVectorTrialResult#state_vector
    """

    circuit = circuit_from_qasm(qasm_string)
    result = cirq.Simulator().simulate(circuit)
    statevector = list(np.around(result.state_vector(), 3))
    return statevector

def expected_result(qasm_file):
    # read the qasm file
    with open(qasm_file, "r") as f:
        qasm_string = f.read()

    # run cirq's simulator on the qasm string
    cirq_state_vector = cirq_simulate(qasm_string)
    
    print(f"{qasm_file} :: {cirq_state_vector}")
    return cirq_state_vector

if __name__ == "__main__":
    # get the directory of qasm files and make sure it's a directory
    qasm_dir = Path(sys.argv[1])

    blacklist = ["con1_216.qasm"]
    if qasm_dir.is_dir():
        # iterate the qasm files in the directory
        for qasm_file in qasm_dir.glob("**/*.qasm"):
            # print(f"{qasm_file} not in {blacklist}....")
            expected_result(qasm_file)
    else:
        expected_result(sys.argv[1])

