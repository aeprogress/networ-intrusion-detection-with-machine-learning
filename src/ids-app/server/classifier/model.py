import joblib
import pandas as pd


class Model:
    def __init__(self) -> None:
        self.classifier = self.load_model()
        self.data = None

    def load_model(self):
        model_path = 'assets/knn_model.sav'
        return joblib.load(model_path)

    def predict(self, data):
        scaler = joblib.load('assets/standard-scaler')
        ohe = joblib.load('assets/one-hot-ecoder')
        self.data = pd.DataFrame(data)
        X = scaler.transform(self.data)
        y_pred = self.classifier.predict(X)
        y_pred = ohe.inverse_transform(y_pred)
        self.data['predicted_label'] = y_pred
        return self.data.predicted_label.to_json(orient='records')


model = Model()


def get_model():
    return model
