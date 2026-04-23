from qiskit_ibm_runtime import QiskitRuntimeService

with open(".env") as f:
    api_key = f.read()
    api_key = api_key.split("=")[1].strip().strip('"')  # Get the value of the API key and remove any whitespace and quotes

QiskitRuntimeService.save_account(token=api_key, instance="crn:v1:bluemix:public:quantum-computing:us-east:a/71260753ffbf4ef6910abfb86510bfe0:05250a29-d782-4556-aa3f-10c5bb3674ca::", overwrite=True)
