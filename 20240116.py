import numpy as np
import pandas as pd



def homework20240111(filename):
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

def homework_by_pandas(filename):
    data = pd.read_csv(filename)
#--------------------------------------------------------------------------------------------答案
    print(f"該資料集共有幾個欄位、幾筆資料（扣除欄位）？:\t{data.shape[0]}欄位; {data.shape[1]}筆資料")
def main1():
    Class_A = {
        "Java":80,
        "C#":88,
        "Python":85,
        "JavaScript":70,
        "Ruby":100
    }
    Class_B = {
        "R":80,
        "Python":88,
        "Matlab":85,
        "C#":70,
        "Java":100
    }

    seriesA = pd.Series(Class_A)
    seriesB = pd.Series(Class_B)
    print(seriesA)
    print('-'*20) 
    print(seriesB)
    print('-'*20) 
    print()   
    new_index = seriesA.index.intersection(seriesB.index)
    average_S = (seriesA[new_index]+seriesB[new_index])/2
    seriesA[new_index]=average_S
    seriesB[new_index]=average_S
    print(seriesA)
    print('-'*20) 
    print(seriesB)
    print('-'*20)    



if __name__=='__main__':

    #homework20240111("insurance.csv")
    #homework_by_pandas('insurance.csv')
    main1()