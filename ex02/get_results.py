from qiskit.visualization.counts_visualization import plot_histogram
from qiskit_ibm_runtime import QiskitRuntimeService
import matplotlib.pyplot as plt

service = QiskitRuntimeService()
# job_id = input("enter job id: ")
job_id = "d7laf8a4lglc7380cl80"
job = service.job(job_id)
count_result01 = job.result()[0].data.meas.get_counts()
nbshots = 500
two_qubits_superposition_entanglement = {i: j/ nbshots for i, j in count_result01.items()} # add some normalisation to comply with subject

data = [two_qubits_superposition_entanglement]
title = "ex02"
color=['crimson','midnightblue']
print("values : ", data)
plot_histogram(two_qubits_superposition_entanglement, color=color)
plt.show()
