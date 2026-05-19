from typing import List
import qiskit_aer.noise.errors.base_quantum_error
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import SamplerV2
from qiskit.visualization.counts_visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import Diagonal
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from cirq import dirac_notation

def search_algorithm(nbqubits: int, state: str):
    qc = QuantumCircuit(nbqubits, nbqubits)
    # qc.x(nbqubits)
    qc.h(range(nbqubits))
    number = 1

    for _ in range(number):
        qc.barrier(label="oracle")
        new_oracle(qc, range(nbqubits), state)  # ty:ignore[invalid-argument-type]
        qc.barrier(label="diffusion")
        diffusion(qc, range(nbqubits))  # ty:ignore[invalid-argument-type]

    qc.measure(range(nbqubits), range(nbqubits))
    return qc

def diffusion(qc: QuantumCircuit, nbqubits: List):
    qc.h(nbqubits)
    qc.z(nbqubits)
    qc.cz(nbqubits[0], nbqubits[1])
    qc.h(nbqubits)
    return qc

def new_oracle(qc: QuantumCircuit, nbqubits: List, state: str):
    matrix =   [[1, 0, 0, 0],
                [0, -1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]
    # mark_state = Statevector.from_label(state)
    # mark_circuit = Diagonal((-1)**mark_state.data)
    gate = UnitaryGate(matrix, label="oracle")  # ty:ignore[invalid-argument-type]
    qc.append(gate, nbqubits)
    return qc

nbqubits = 2
state = "01"
qc = search_algorithm(nbqubits, state)
# final_state_homemade = Statevector.from_instruction(qc)
# initial_configuration_str = '1100'
# initial_state = Statevector.from_label(initial_configuration_str)
# print( dirac_notation(final_state_homemade))
noisy_backend = AerSimulator()
nbshots = 5000
options = {"default_shots": nbshots}
sampler = SamplerV2(mode = noisy_backend, options = options)
qc_transpiled = transpile(qc, backend=noisy_backend)
result = sampler.run([qc_transpiled]).result()
count_result = result[0].data.c.get_counts()
values = {i: j/ nbshots for i, j in count_result.items()}
search_algorithm = qc.draw("mpl", idle_wires=False)
search_algorithm.canvas.manager.set_window_title("Deutsch-Jozsa Algorithm")
print(values)
plot_histogram(values)
plt.show()
