import sys
import numpy as np
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm
from pathlib import Path



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


qasm_file = 'qasm/sample.qasm'

qasm_string = ""
with open(qasm_file, "r") as f:
    qasm_string = f.read()

# run your simulate function on the qasm string
# state_vector = simulate(qasm_string)

# run cirq's simulator on the qasm string
cirq_state_vector = cirq_simulate(qasm_string)

print(f"Cirq result : {cirq_state_vector}")
# compare the results!
