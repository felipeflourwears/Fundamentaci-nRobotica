import numpy as np
import random

class Perceptron:        
    """Perceptron class

            Args:
                M: Number of inputs
                alpha: Learning rate
            
            Attributes:
                W: The weights for the perceptron
                b: bias
                alpha: The learning rate
    """
    def __init__(self, N,M, alpha=0.1):        
        # Creates an array of N weights and initializes with random values
        # define iputs
        self.M=M
        self.W = (np.random.random(N))
        self.b = (np.random.random(1))
        print("Imprimienndo bios")
        print(self.b)
        print("Imprimiendo weights")
        print(self.W)
                
    def sigmoid(self, x):
        #TO DO: Apply the sigmoid function
        s=1/(1+np.exp(-x))
        return s

    def error(self, y, yhat):
        #TO DO: Apply the sigmoid function
        e=(1-y)*(np.log(1-yhat)+y*(np.log(yhat)))
        return e
        
    def predict(self, x):
        """
            Makes a prediction for the specified input
                
            Args:
                x: Input to make a prediction on.
        """        
        #TO DO: Define the predict function
        y_hat=[0]*self.M
        #y_hat=0
        print(x)
        for i in range(self.M):
        #y_hat=self.sigmoid(self.W[0]*x[0]+self.W[1]*x[1]+self.b[0])
            y_hat[i]=self.sigmoid(self.W[0]*x[i][0]+self.W[1]*x[i][1]+self.b[0])
            print("Imprimiendo Y sombrerito")
            print(y_hat[i])
        return y_hat
        
    def perceptronStep(self, X, y):
        """
        The perceptron basic step. It updates the weights based on the input data.
                
        Args:
            X: Array with the input data
            y: Data labels
        """
        # TO DO: Implement the perceptron algorithm.
        pass
        
    def train(self, X, y, epochs = 10):
        """
        Runs the perceptron step a specified number of epochs
                
        Args:
            X: input data
            y: labels
            epochs: The number of times the step is executed
        """
        # loop over the desired epochs
        e=0
        for epoch in range(epochs):
            """
            for i in range(self.M):
                yhat=self.predict(X[i])
                e+=self.error(yhat, y[i])
                dy=[yhat-y[i]]
                dw1+=dy*X[i][0]
                dw2=dy*X[i][1]
                db+=dy
            """
        self.perceptronStep(X, y)
        return

X = [[0,0],[0,1], [1,0], [1,1]]
y = [[0],[0], [0], [1]]
print("<------------------------------------------>")
p = Perceptron(2,4)
print("<------------------------------------------>")
print(f"Initial weights {p.W}")
prediction = p.predict(X)
# Test training with different epochs
p.train(X, y, 25)