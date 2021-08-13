import numpy as np
from numpy import ndarray


def _error(actual: np.ndarray, predicted: np.ndarray):
    """ Error function """
    return actual - predicted


def mae(pred: ndarray, label: ndarray) -> ndarray:

    """ Mae function """
    return np.mean(np.abs(_error(label, pred)))


def sse(pred: ndarray, label: ndarray) -> ndarray:
    """ sse function """
    return np.sum((label-pred)**2)


def mse(pred: ndarray, label: ndarray) -> ndarray:
    """ mse function """
    return np.mean(np.square(_error(label, pred)))


def rmse(pred: ndarray, label: ndarray) -> ndarray:

    """ rmse Error """
    return np.sqrt(mse(label, pred))