import numpy as np
from tqdm import tqdm
import gc

def approximate_e(n, batch_size):
    sum = 0
    num = int(n/batch_size)
    size = [10, batch_size]
    for i in tqdm(range(num)):
        probability_matrix = np.random.uniform(0, 1, size)
        sum_matrix = np.cumsum(probability_matrix, axis = 0)
        index = np.argmax(sum_matrix > 1, axis = 0)+1
        sum_new = np.sum(index)
        sum += sum_new
    print(sum/n)
    
    
def approximate_e_2(n, batch_size):
    sum = 0
    ratio = 1000
    num = int(n/batch_size)
    size = [10, batch_size]
    size_1 = [10, int(batch_size/ratio)]
    
    probability_matrix = np.random.uniform(0, 1, size)
    sum_matrix = np.cumsum(probability_matrix, axis = 0)
    index = np.argmax(sum_matrix > 1, axis = 0)+1
    
    sum_b = np.sum(index[int(batch_size/ratio):])
    for i in tqdm(range(num)):
        new_probability = np.random.uniform(0, 1, size_1)
        sum_matrix = np.cumsum(new_probability, axis = 0)
        index = np.argmax(sum_matrix > 1, axis = 0)+1
        sum_new = np.sum(index)
        sum += (sum_new+sum_b)
    print(sum/n)
    
    
approximate_e_2(1000000000000,10000000)
# approximate_e(100000000,10000000)

    
    
