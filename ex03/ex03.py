import matplotlib.pyplot as plt
from qiskit_ibm_runtime import SamplerV2
from qiskit.visualization.counts_visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile

def deutsch_jozsa(oracle):
    qc_constant = QuantumCircuit(4, 3)
    qc_constant.x(3)
    qc_constant.h(range(4))

    oracle_gate = oracle.to_gate()
    qc_constant.append(oracle_gate, range(4))

    qc_constant.h(range(3))

    qc_constant.measure(range(3), range(3))
    return qc_constant

def new_constant_oracle():
    oracle_constant = QuantumCircuit(4)
    oracle_constant.x(3)
    return oracle_constant

def new_balanced_oracle():
    oracle_balanced = QuantumCircuit(4)
    oracle_balanced.x(range(3))
    oracle_balanced.cx(0, 3)
    oracle_balanced.cx(1, 3)
    oracle_balanced.cx(2, 3)
    oracle_balanced.x(range(3))
    return oracle_balanced

oracle = input("\t1 - constant\n\t2 - balanced\nchoose oracle: ")
if oracle == "1":
    oracle_constant = new_constant_oracle()
    oracle_constant.draw("mpl", idle_wires=False).canvas.manager.set_window_title("constant oracle")
    qc = deutsch_jozsa(oracle_constant)
elif oracle == "2":
    oracle_balanced = new_balanced_oracle()
    oracle_balanced.draw("mpl", idle_wires=False).canvas.manager.set_window_title("balanced oracle")
    qc = deutsch_jozsa(oracle_balanced)
else:
    exit("invalid choice")

noisy_backend = AerSimulator()
nbshots = 500
options = {"default_shots": nbshots}
sampler = SamplerV2(mode = noisy_backend, options = options)
qc_transpiled = transpile(qc, backend=noisy_backend)
result = sampler.run([qc_transpiled]).result()
count_result = result[0].data.c.get_counts()
values = {i: j/ nbshots for i, j in count_result.items()}
deutsch_jozsa = qc.draw("mpl", idle_wires=False)
deutsch_jozsa.canvas.manager.set_window_title("Deutsch-Jozsa Algorithm")
print(values)
plot_histogram(values)
plt.show()
