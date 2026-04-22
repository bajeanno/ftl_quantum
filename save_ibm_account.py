from qiskit_ibm_runtime import QiskitRuntimeService

with open(".env") as f:
    api_key = f.read()
    api_key = api_key.split("=")[1].strip().strip('"')  # Get the value of the API key and remove any whitespace and quotes

QiskitRuntimeService.save_account(token=api_key)
