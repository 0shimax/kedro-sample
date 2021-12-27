import requests
import base64
import json
import numpy as np
from onnx import numpy_helper
from google.protobuf.json_format import MessageToJson
import time


ENDPOINT = 'http://localhost:9001/v1/models/default/versions/1:predict'
json_request_headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

float_input_array = np.array([[2.0,4,3.0,1.0,96.0]], dtype=np.float32)
categorical_input_array = np.array([["False","False","True"]], dtype="O")
float_tensor_proto = numpy_helper.from_array(float_input_array)
cat_tensor_proto = numpy_helper.from_array(categorical_input_array)

inputs = {}
json_str = MessageToJson(float_tensor_proto, use_integers_for_enums=True)
data = json.loads(json_str)
inputs["float_input"] = data
json_str = MessageToJson(cat_tensor_proto, use_integers_for_enums=True)
data = json.loads(json_str)
inputs["categorical_input"] = data

payload = {}
payload["inputs"] = inputs

start = time.time()
res = requests.post(ENDPOINT, headers=json_request_headers, data=json.dumps(payload))
elapsed_time = time.time() - start
print ("elapsed_time:{}".format(elapsed_time*1000) + "[ms]")

res_dic = json.loads(res.text)
if "outputs" in res_dic:
    raw_data = res_dic['outputs']['variable']['rawData']
    outputs = np.frombuffer(base64.b64decode(raw_data), dtype=np.float32)
    print(outputs)  # (1, 1000)
else:
    raise RuntimeError(f"internal server error: {res_dic['error_message']}")