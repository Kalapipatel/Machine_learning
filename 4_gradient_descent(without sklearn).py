import math
import numpy as np

def gradient_descent(x, y):
    learning_rate = 0.08
    m_curr = b_curr = 0
    iterations = 3000
    n = len(x)
    cost_fun = 1000
    
    for i in range(iterations):
        y_predicted = m_curr*x + b_curr
        a = cost_fun
        cost_fun = (1/n) * sum([val**2 for val in (y - y_predicted)])
        md = -(2/n)*sum(x*(y - y_predicted))
        bd = -(2/n)*sum((y - y_predicted))
        m_curr = m_curr - learning_rate*md
        b_curr = b_curr - learning_rate*bd
        print(f"m_curr = {m_curr} b_curr = {b_curr} cost function = {cost_fun} iterations = {i}")
        if(math.isclose(a, cost_fun, rel_tol=1e-20)):
            print(f"total iterations are : {i}")
            break
        

        
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x, y)
