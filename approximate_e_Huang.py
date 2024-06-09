import random
import time
import numpy as np
from tqdm import tqdm

def simulate_trial():
    total = 0
    n = 0
    while total <= 1:
        total += random.uniform(0, 1)
        n += 1
    return n

def calculate_expected_value(num_trials):
    total_n = 0
    for i in tqdm(range(num_trials)):
        total_n += simulate_trial()
    return total_n / num_trials


n = int(input("请输入实验次数："))
start_time = time.time()
expected_value = calculate_expected_value(n)
end_time = time.time()
run_time = end_time - start_time
print("e的估计为：", expected_value)
print("程序运行时间：", run_time, "秒")