
import pandas as pd
import numpy as np
"""
202011069017 蒋宗青
"""
def Read(filePath):
    data = pd.read_excel(filePath, 'Sheet1', index_col=0)
    data.to_csv('Data/data.csv', encoding='utf-8')
    data = pd.read_csv('Data/data.csv')
    dataArray=data.values
    print(dataArray)
    return dataArray

def ln(x): #封装一个ln()函数（可应用于处理array)
    ln_x=[]
    for i in range(len(x)):
        ln_x.append(np.log(x[i])) #逐个存入list
    return np.array(ln_x) #返回数组

def Simpson_Shannon(dataArray):
    aSum=sum(dataArray[:,1])
    bSum = sum(dataArray[:, 2])
    cSum = sum(dataArray[:, 3])
    dSum = sum(dataArray[:, 4])
    print(aSum,bSum,cSum,dSum)

    aSimpson=1-sum(dataArray[:,1]**2)/(aSum**2)
    bSimpson = 1 - sum(dataArray[:, 2] ** 2) / (bSum ** 2)
    cSimpson = 1 - sum(dataArray[:, 3] ** 2) / (cSum ** 2)
    dSimpson = 1 - sum(dataArray[:, 4] ** 2) / (dSum ** 2)
    print("Simpson's diversity 指数：")
    print(aSimpson,bSimpson,cSimpson,dSimpson)

    Array_a=dataArray[:4, 1] / aSum
    Array_b=dataArray[:4, 2] / bSum
    Array_c=dataArray[:, 3] / cSum
    Array_d=dataArray[:, 4] / dSum

    ln_a=ln(Array_a)
    ln_b=ln(Array_b)
    ln_c=ln(Array_c)
    ln_d=ln(Array_d)

    aShannon = -sum(ln_a*Array_a)
    bShannon = -sum(ln_b * Array_b)
    cShannon = -sum(ln_c* Array_c)
    dShannon = -sum(ln_d * Array_d)

    print("Shannon-Wiener 指数：")
    print(aShannon,bShannon,cShannon,dShannon)

if __name__ == '__main__':
    filePath='Data/communitySpecies.xlsx'
    dataArray=Read(filePath)
    Simpson_Shannon(dataArray)