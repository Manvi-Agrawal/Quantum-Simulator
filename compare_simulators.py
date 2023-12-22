import sys
import numpy as np
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm
from pathlib import Path

# Import your simulate function here.
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


def compare(state_vector, cirq_state_vector):
    """Our comparison function for your grade

    Args:
        state_vector: your state vector amplitude list
        cirq_state_vector: cirq's state vector amplitude list

    Returns:
        Some value influencing your grade, subject to change :)
    """

    return np.all(np.isclose(state_vector, cirq_state_vector))


def compare_results(qasm_file):
    # read the qasm file
    with open(qasm_file, "r") as f:
        qasm_string = f.read()

    # run your simulate function on the qasm string
    state_vector = simulate(qasm_string)
    # run cirq's simulator on the qasm string
    cirq_state_vector = cirq_simulate(qasm_string)
    # compare the results!
    print(f"\n\n ==Simulator comparison : {qasm_file}==")
    # print(f"Actual: {state_vector}; Expected: {cirq_state_vector}")
    res = compare(state_vector, cirq_state_vector)
    print(res)
    return res

if __name__ == "__main__":
    print(f"== Main Function of sim compare ==")

    # get the directory of qasm files and make sure it's a directory
    qasm_dir = Path(sys.argv[1])

    if qasm_dir.is_dir():
        # iterate the qasm files in the directory
        for qasm_file in qasm_dir.glob("**/*.qasm"):
            assert compare_results(qasm_file)
    else:
        assert compare_results(sys.argv[1])

