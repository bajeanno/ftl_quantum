from numpy.testing.print_coercion_tables import print_new_cast_table
import fontTools.ttLib.standardGlyphOrder
import matplotlib.pyplot as plt
from qiskit.visualization.counts_visualization import plot_histogram
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit_ibm_runtime import QiskitRuntimeService

qc00 = QuantumCircuit(1)  # Init a quantum circuit to one qubit at state 0
qc00.h(0)                 # Operates a Hadamard gate on qubit 0 so it state is now a superposition of 0 and 1
qc00.measure_all()        # Measure all qubits so they fix their states

qc01 = QuantumCircuit(2)  # Init a quantum circuit to one qubit at state 0
qc01.h(0)                 # Operates a Hadamard gate on qubit 0 so it state is now a superposition of 0 and 1
qc01.cx(0, 1)             # Operates a controlled-x gate from qubit 0 to 1 so they are entangled
qc01.measure_all()        # Measure all qubits so they fix their states

nbshots = 500
sampler = StatevectorSampler()
result00 = sampler.run([qc00], shots=nbshots).result()
result01 = sampler.run([qc01], shots=nbshots).result()
count_result00 = result00[0].data.meas.get_counts()  # ty:ignore[unresolved-attribute]
count_result01 = result01[0].data.meas.get_counts()  # ty:ignore[unresolved-attribute]
one_qbit_superposition = {i: j/ nbshots for i, j in count_result00.items()} # add some normalisation to comply with subject
two_qubits_superposition_entanglement = {i: j/ nbshots for i, j in count_result01.items()} # add some normalisation to comply with subject

data = [one_qbit_superposition, two_qubits_superposition_entanglement]
title = "ex02"
legend = ["ex00", "ex01"]
color=['crimson','midnightblue']
print("values : ", data)
plot_histogram(data, title=title, legend=legend, color=color)
plt.show()
