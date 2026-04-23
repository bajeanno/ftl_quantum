import matplotlib.pyplot as plt
from qiskit_ibm_runtime import SamplerV2
from qiskit.visualization.counts_visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)  # Init a quantum circuit to one qubit at state 0
qc.h(0)                 # Operates a Hadamard gate on qubit 0 so it state is now a superposition of 0 and 1
qc.cx(0,1)
qc.measure_all()        # Measure all qubits so they fix their states

noisy_backend = AerSimulator()
nbshots = 500
options = {"default_shots": nbshots}
sampler = SamplerV2(mode = noisy_backend, options = options)
result = sampler.run([qc]).result()
count_result = result[0].data.meas.get_counts()
values = {i: j/ nbshots for i, j in count_result.items()}

print(values)
plot_histogram(values)
plt.show()
