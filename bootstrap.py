import numpy as np
import matplotlib.pyplot as plt
from arch.bootstrap import IIDBootstrap
from scipy.stats import norm
from tqdm import tqdm

# 定义指示函数
def indicator(x):
    return np.bitwise_xor("A" in x, True)

# 定义 p_hat 函数，使用 Bootstrap 进行自助法
def p_hat(data, m=int(1e5)):
    bs = IIDBootstrap(data)
    results = bs.apply(indicator, reps=m)
    return 1 / np.mean(results)

# 设定样本量
n_list = [int(1e1), int(1e2), int(1e3), int(1e4)]
reps_list = np.zeros((len(n_list), 10))
labels = []
i=0
for n in n_list:
    # 构造数据集
    dat = np.array(["A"] + ["B"] * (n - 1))

    # 进行 1 次自助法，得到 e 的估计值
    reps = np.array([p_hat(dat) for _ in tqdm(range(10))])
    reps_list[i,:] = reps
    labels.append(f"{n}")
    i+=1
   
# 创建图形对象和子图
fig, ax = plt.subplots()

# 计算箱线图的位置
positions = np.arange(1, len(labels)+1)

# 循环遍历每一行数据，绘制箱线图
for i in range(reps_list.shape[0]):
    ax.boxplot(reps_list[i,:], positions=[positions[i]])

# 设置横坐标标签
ax.set_xticks(positions)
ax.set_xticklabels(labels)

#标记出e的真实大小
plt.axhline(y=np.exp(1), color="red")

# 设置 x 轴为对数刻度
# plt.xscale("log")
plt.xlabel("n")
plt.ylabel(r"e'")
plt.title(r"Bootstrap Estimates of $\tilde{e}$")

# 显示图形
plt.show()
