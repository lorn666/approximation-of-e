import numpy as np
import concurrent.futures
import time
from tqdm import tqdm

def simulate(n):
    #生成服从标准正态分布的x与y的值
    random_x = np.random.randn(n)
    random_y = np.random.randn(n)
    #计算平方和
    sum = random_x**2 + random_y**2
    #计算距离的平方大于2的个数
    n1 = np.sum(sum>2)
    return n1

if __name__ == '__main__':
    # n = int(input('请输入模拟次数:'))
    start = time.time()
    n = 10000
    batch_size = 1000
    times = int(n/batch_size)
    n1=0
    

    with concurrent.futures.ProcessPoolExecutor(max_workers=30) as executor:
        # 准备要并行处理的参数列表
        args = [batch_size] * times

        # 使用进程池并行执行函数，并实时更新进度条
        results = []
        with tqdm(total=times) as pbar:
            for result in executor.map(simulate, args):
                n1 += result
                pbar.update()

    # 计算e的大小
    e = float(n)/float(n1)
    print(e)
    print(f'time={time.time()-start}s')
