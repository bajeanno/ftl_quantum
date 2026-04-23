from qiskit_ibm_runtime.batch import Batch
from qiskit_ibm_runtime.options.estimator_options import EstimatorOptions
import matplotlib.pyplot as plt
from qiskit.visualization.counts_visualization import plot_histogram
from qiskit import QuantumCircuit, generate_preset_pass_manager
from qiskit_ibm_runtime import Sampler
from qiskit_ibm_runtime import QiskitRuntimeService

nbshots = 500
qc = QuantumCircuit(2)  # Init a quantum circuit to one qubit at state 0
qc.h(0)                 # Operates a Hadamard gate on qubit 0 so it state is now a superposition of 0 and 1
qc.cx(0, 1)             # Operates a controlled-x gate from qubit 0 to 1 so they are entangled
qc.measure_all()        # Measure all qubits so they fix their stat

service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True, min_num_qubits=100)
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

isa_circuit.draw("mpl", idle_wires=False)
batch = Batch(backend=backend)
sampler = Sampler(mode=batch)
job = sampler.run([isa_circuit], shots=nbshots)
print("job id: ", job.job_id())
