import numpy as np
import time

def get_random(low, high, arr):
    set_seed = 123
    vv = np.random.RandomState(set_seed).randint(low,high,arr)
    return vv

def c_y(nums):
    unv = np.array(nums)
    return unv

def main1():
    '''
    請隨機產生一個2*4的ndarray, ndarray中的每個值都介於1~10之間
    對每個一維的ndarray刪除索引值1、3的元素
    例：
    隨機產生的二維ndarray:
    [[9 5 1 5]
    [7 7 3 7]]
    刪除索引值1、3後的ndarray
    [[9 1]
    [7 3]]
    '''
    vv = get_random(1,10,(2,4))
    print(vv)
    print(np.delete(vv, (1,3), axis=1))#answer

def main2():
    '''
    請隨機產生一個10個元素一維的ndarray, ndarray中的每個值都介於1~20之間
    請刪除ndarray中所有小於10的數並輸出
    例：
    隨機產生的一維ndarray:
    [ 5 19  5 16 13  8  8 14  7 18]
    刪除小於10的ndarray
    [19 16 13 14 18]
    '''
    vv = get_random(1,20,10)
    print(np.delete(vv, np.where(vv<10)))#answer1
    print("-"*20)
    print(vv[vv>=10])#answer2

def main3():
    """
    請讓使用者不斷的輸入數字, 直到輸入q為止
    將使用者輸入的數建構為一維的ndarray
    刪除ndarray中最大的數, 並輸出
    """

    list1 =[]
    while True:
        a = input('please input digital:\n')
        if a == 'q':
            break
        else:
            list1.append(int(a))
    v = c_y(list1)
    del_index = np.where(v == max(v))
    res = np.delete(v, del_index)
    print(res)#answer

def homework(filename):
    '''
    題目:
    該資料集共有幾個欄位、幾筆資料（扣除欄位）？
    sex欄位共有幾種值, 分別為哪些？ 
    保醫療險的平均年齡為多少（取小數點後兩位）？
    哪個地區的吸煙人數最多？
    '''
    #--------------------------------------------------------------------------------------------題目1
    data = np.genfromtxt(filename, delimiter=',', dtype=None, encoding='utf-8-sig')

    #--------------------------------------------------------------------------------------------題目3
    age_col = data[1:,0]
    age_col = np.where(age_col=='40歲', '40', age_col)
    d_age = age_col.astype(int)

    #--------------------------------------------------------------------------------------------題目2
    sex_col = data[1:,1]
    s_v = np.unique(sex_col)

    #--------------------------------------------------------------------------------------------題目4
    smoker = data[1:,4]
    Index_smoker_yes = np.where(smoker=="yes")
    area_v, area_c = np.unique(data[1:,5][Index_smoker_yes], return_counts=True)
    max_area_c_index = np.argmax(area_c)

    #--------------------------------------------------------------------------------------------答案
    print('-'*20)
    print(f"該資料集共有幾個欄位、幾筆資料（扣除欄位）？:\t{data[1:].shape[0]}筆資料")
    print('-'*20)
    print(f"sex欄位共有幾種值, 分別為哪些？:\t{s_v}")
    print('-'*20)
    print(f"保醫療險的平均年齡為多少（取小數點後兩位):\t{d_age.mean():.2f}")
    print('-'*20)
    print(f"哪個地區的吸煙人數最多？:    {area_v[max_area_c_index]}\t;人數為:{np.amax(area_c)}")

def main4():
    R = get_random(1, 10, (2,5))
    corr = np.corrcoef(R)
    print(corr)

if __name__=='__main__':
    start = time.time()
    #main1()
    #main2()
    #main3()
    #main4()
    data = 'insurance.csv'
    homework(data)
    
    
    
    
    
    end = time.time()
    print('-'*20)
    print(end-start)

