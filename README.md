# Micrograd-from-scratch-and-neural-network-trained-on-it-

A Python implementation of a tiny automatic differentiation engine inspired by Andrej Karpathy's Micrograd.

This project builds a complete neural network framework from scratch without using any deep learning libraries. The goal is to understand how backpropagation and gradient descent work under the hood.

---

## Features

- Automatic differentiation (Autograd)
- Computational graph construction
- Reverse-mode backpropagation
- Arithmetic operations with gradient tracking
- Tanh activation function
- Exponential and power operations
- Fully connected Neuron implementation
- Layer abstraction
- Multi-Layer Perceptron (MLP)
- Mean Squared Error (MSE) loss
- Gradient descent training
- Graph visualization using Graphviz

---

## Project Structure

```
micrograd.ipynb
```

The notebook contains:

1. Implementation of the `Value` class
2. Computational graph visualization
3. Numerical gradient checking
4. Backpropagation implementation
5. Neuron implementation
6. Layer implementation
7. Multi-Layer Perceptron (MLP)
8. Training on a small dataset

---

## Example Training Data

```python
xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0],
]

ys = [1.0, -1.0, -1.0, 1.0]
```

The network is trained using Mean Squared Error (MSE) loss and gradient descent.

---

## Technologies Used

- Python
- Jupyter Notebook
- Graphviz

---

## Concepts Covered

- Computational Graphs
- Chain Rule
- Reverse-mode Automatic Differentiation
- Backpropagation
- Gradient Descent
- Neural Networks
- Multi-Layer Perceptrons (MLPs)

---

## Inspiration

This project is based on the concepts taught in Andrej Karpathy's Micrograd series and was implemented as a learning exercise to understand neural networks from first principles.

---

## Future Improvements

- Add ReLU activation
- Add Sigmoid activation
- Mini-batch Gradient Descent
- Cross Entropy Loss
- Save/Load model parameters
- Separate the notebook into Python modules
