from scikit_rest_wrapper.models import Model, Schema
from werkzeug.exceptions import NotImplemented
from marshmallow import ValidationError
import socket


def index():
    """
    Controller that fetches the description of the model schema. Raises NotImplemented exception if
    it does not exist.
    :return: result of the describe method of the model schema if it exists.
    """
    model_schema = Schema().get()

    if Schema().has_descr(model_schema):
        return model_schema.describe()
    else:
        raise NotImplemented('This schema has no description implemented.')


def status():
    """
    Controller that returns some statistics about the app.
    :return: A dict having keys 'model', 'schema', 'hostname'
    """
    return {
        'schema': Schema().status(),
        'model': Model().status(),
        'hostname': socket.gethostname()
    }


def predict(data):
    """
    :param data: An datastructure serializable by the model schema
    :return: A copy of data with added the predicted class
    """
    model_schema = Schema().get()
    model = Model().get()

    X = model_schema.load(data).data
    y = model.predict(X).tolist()

    data['target'] = y[0]

    return data


def predict_proba(data):
    """

    :param data: An datastructure serializable by the model schema
    :return: A copy of data with added the prediction
    """
    model_schema = Schema().get()
    model = Model().get()

    if not Model().has_predict_proba(model):
        raise NotImplemented('This controller is not yet implemented.')

    X = model_schema.load(data).data
    y = model.predict_proba(X).tolist()

    data['target'] = y[0]

    return data