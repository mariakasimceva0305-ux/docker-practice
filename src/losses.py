
import numpy as np

def mean_squared_error(y_true, y_pred):
    return np.mean((np.array(y_true) - np.array(y_pred)) ** 2)

def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(np.array(y_true) - np.array(y_pred)))

def squared_hinge_loss(y_true, y_pred):
    y_true_bin = np.where(np.array(y_true) > 0, 1, -1)
    margin = y_true_bin * np.array(y_pred)
    loss = np.maximum(0, 1 - margin) ** 2
    return np.mean(loss)
