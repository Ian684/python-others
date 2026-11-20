import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# 用來求解洛倫茲方程
# =========================================================洛倫茲方程模擬圖
def lorenz(state,t,sigma=10.0,rho=28.0,beta=8.0/3.0):
    x,y,z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt,dydt,dzdt]
# 洛倫茲方程
statistic_1 = [0.0,1.0,0.0]  
statistic_2 = [0.0,1.01,0.0] 
# 微小差距的兩個初始條件
t = np.linspace(0,30,10000)
# 10000個等間距的點(numpy陣列)
track_1 = odeint(lorenz,statistic_1,t)
track_2 = odeint(lorenz,statistic_2,t)
# (numpy陣列)
x1,y1,z1 = track_1.T
x2,y2,z2 = track_2.T
# 行列對調並解包(numpy陣列)
picture = plt.figure(figsize=(10,6))
result = picture.add_subplot(111,projection='3d')
# 在原圖上劃分成一行一列並建立一個3d圖
result.plot(x1,y1,z1,lw=0.5,color='b',label='Track_1 (Initial:[0.0,1.0,0.0])')
result.plot(x2,y2,z2,lw=0.5,color='r',label='Track_2 (Initial:[0.0,1.01,0.0])')
# 兩條軌跡
result.set_title('Smulation results of Lorenz equation')
result.set_xlabel('X')
result.set_ylabel('Y')
result.set_zlabel('Z')
result.legend()
# =========================================================分離度與時間圖
separation = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
# 計算numpy陣列自動對齊並計算距離
plt.figure(figsize=(10,6))
plt.plot(t,separation,label='Separation',color='purple')
# 繪製分離度與時間關係圖
plt.title('Separation of Lorenz Tracks')
plt.xlabel('Time')
plt.ylabel('Separation')
plt.legend()
# =========================================================李亞普諾夫指數與時間圖
def jacobian(state,sigma=10.0,rho=28.0,beta=8.0/3.0):
    x,y,z = state
    j = np.array([[-sigma,sigma,0],
                  [rho-z,-1,-x],
                  [y,x,-beta]])
    return j
# 用jacobian矩陣計算李亞普諾夫指數
def max_lyapunov_number(statistic,t):
    track = odeint(lorenz,statistic,t)
# (numpy陣列)
    arr = []
    for i in range(len(t)):
        j = jacobian(track[i])
        values = np.linalg.eigvals(j)
        arr.append(max(values.real))
# 計算特徵值並取實部
    return arr
# 計算最大李亞普諾夫指數
lyapunov_number = max_lyapunov_number(statistic_1,t)
plt.figure(figsize=(10,6))
plt.plot(t,lyapunov_number,label='Lyapunov_number',color='green')
plt.title('Change of Lyapunov Number')
plt.xlabel('Time')
plt.ylabel('Lyapunov Number')
plt.legend()
plt.show()
