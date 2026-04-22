import fontTools.ttLib.standardGlyphOrder
import matplotlib.pyplot as plt
from qiskit.visualization.counts_visualization import plot_histogram
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1)  # Init a quantum circuit to one qubit at state 0
qc.h(0)                 # Operates a Hadamard gate on qubit 0 so it state is now a superposition of 0 and 1
qc.measure_all()        # Measure all qubits so they fix their states

nbshots = 500
sampler = StatevectorSampler()
result = sampler.run([qc], shots=nbshots).result()
count_result = result[0].data.meas.get_counts()  # ty:ignore[unresolved-attribute]
values = {i: j/ nbshots for i, j in count_result.items()}

print(values)
plot_histogram(values)
plt.show()
