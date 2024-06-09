# import numpy as np
# import concurrent.futures
# import time
# from tqdm import tqdm

# import random

# def simulate(n):
#     total_N = 0

#     for _ in range(n):
#         previous_num = random.uniform(0, 1)
#         N = 1

#         while True:
#             N+=1
#             current_num = random.uniform(0, 1)
#             if current_num >= previous_num:
#                 break
#             else:
#                 previous_num = current_num

#         total_N += N

#     average_N = total_N / n
#     return average_N

# if __name__ == '__main__':
#     # 调用函数并传入实验次数n
#     n = 100000000000
#     batch_size=1000000
#     times = int(n/batch_size)
#     n1=0
        

#     with concurrent.futures.ProcessPoolExecutor(max_workers=300) as executor:
#         # 准备要并行处理的参数列表
#         args = [batch_size] * times

#         # 使用进程池并行执行函数，并实时更新进度条
#         results = []
#         with tqdm(total=times) as pbar:
#             for result in executor.map(simulate, args):
#                 n1 += result
#                 pbar.update()

#     average_N = n1/times
#     print(f"Average N: {average_N}")

import numpy as np
import concurrent.futures
import time
from tqdm import tqdm
import numba

@numba.jit(nopython=True)
def simulate(n):
    total_N = 0

    for _ in range(n):
        previous_num = np.random.uniform(0, 1)
        N = 1

        while True:
            N+=1
            current_num = np.random.uniform(0, 1)
            if current_num >= previous_num:
                break
            else:
                previous_num = current_num

        total_N += N

    average_N = total_N / n
    return average_N

if __name__ == '__main__':
    # 调用函数并传入实验次数n
    n = 10000000000000
    batch_size = 10000000
    times = int(n/batch_size)
    n1 = 0
        
    with concurrent.futures.ProcessPoolExecutor(max_workers=300) as executor:
        # 准备要并行处理的参数列表
        args = [batch_size] * times

        # 使用进程池并行执行函数，并实时更新进度条
        results = []
        with tqdm(total=times) as pbar:
            for result in executor.map(simulate, args):
                n1 += result
                pbar.update()

    average_N = n1/times
    print(f"approximate of e: {average_N}")