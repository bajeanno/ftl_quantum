import qiskit_aer.noise.errors.base_quantum_error
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import SamplerV2
from qiskit.visualization.counts_visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile

def search_algorithm(nbqubits: int, oracle):
    qc = QuantumCircuit(nbqubits)
    qc.x(3)
    qc.h(range(4))
    for _ in range(nbqubits):
        oracle_gate = oracle.to_gate()
        qc.append(oracle_gate, range(4))
        qc.h(range(3))
        qc.measure(range(3), range(3))
    return qc

def new_oracle(nbqubits: int):
    oracle = QuantumCircuit(nbqubits)
    return oracle

nbqubits = 4
qc = search_algorithm(nbqubits, new_oracle(4))

noisy_backend = AerSimulator()
nbshots = 500
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
