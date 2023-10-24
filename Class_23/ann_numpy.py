from typing import Type, List

import numpy as np

class BaseActivation:
    
    def forward(self, layer: np.ndarray):
        raise NotImplementedError
    
    def backward(self, layer: np.ndarray):
        raise NotImplementedError
    

class SigmoidActivation(BaseActivation):

    def forward(self, layer: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-layer))

    def backward(self, layer: np.ndarray) -> np.ndarray:
        f = self.forward(layer)
        return f * (1 - f)


class LeakyReluActivation(BaseActivation):
    pass


class BaseLossFunction:

    def compute_loss(self, y_true: np.ndarray) -> np.ndarray:
        pass


class MeanSquareError(BaseLossFunction):
    pass


class DenseNeuralNetwork:
    activation_class: Type[BaseActivation] = LeakyReluActivation
    loss_function_class: Type[BaseLossFunction] = MeanSquareError