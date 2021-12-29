import onnxruntime as rt

from models import Features
from models import PredictionResult
import config as config

sess = rt.InferenceSession(config.MODEL_PATH)
float_input_name = sess.get_inputs()[0].name
categorical_input_name = sess.get_inputs()[1].name
label_name = sess.get_outputs()[1].name

def predict(data: Features) -> PredictionResult:
    inputs = {
        float_input_name: Features.to_numpy(data.float_features),
        categorical_input_name: Features.to_numpy(data.categorical_features),
    }
    predicted = sess.run([label_name], inputs)[0]
    return PredictionResult(**{"predicted": [v[1] for v in predicted]})