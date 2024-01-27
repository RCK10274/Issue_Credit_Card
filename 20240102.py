import numpy as np
import time

def get_random(low, high, arr):
    set_seed = 123
    vv = np.random.RandomState(set_seed).randint(low,high,arr)
    return vv

def creat_array(nums):
    unv = np.array(nums)
    return unv

def main1():
#請隨機產生10個數為介於0~100的ndarray
#如果隨機產生的數有大於80的數則有大到小輸出矩陣, 否則由小到大輸出矩陣
    v = get_random(0,100,10)
    print(f'原資料:{v}')
    sortnums = np.where(np.any(v>80)==True, np.sort(v), abs(np.sort(-v)))
    print(f'修改後資料:{sortnums}')

def main2():
#請隨機產生10個數值介於0 ~ 100且為2*5的ndarray
#輸出該隨機產生的ndarray
#對於每個元素由小到大排序的結果
    vv = get_random(0,100,(2,5))
    print(f'原資料:\n{vv}')
    print((f'修改後資料:\n{np.sort(vv.flatten()).reshape(2,5)}'))

def main3():
#隨機產生10個介於0 ~ 100的數建構ndarray
#輸出隨機產生的ndarray
#若該ndarray中有大於5個數為偶數則輸出偶數的最大值與偶數的最小值
#若該ndarray中有小於或等於5個數為偶數則輸出奇數的最大值與奇數的最小值
    vv = get_random(0,100,(10))
    print(f'原資料:{vv}')
    index1 = np.where(vv%2!=0)
    index2 = np.where(vv%2==0)
    #print(index1, index2)
    if len(index2)>5:
        print(np.amax(vv[index2]), np.amin(vv[index2]))
    else:
        print(np.amax(vv[index1]), np.amin(vv[index1]))

def main4():
    vv = creat_array(np.arange(0,3))
    print(np.newaxis)
    new_axis = vv[:, np.newaxis, np.newaxis]
    print(new_axis)


if __name__=="__main__":
    main4()
