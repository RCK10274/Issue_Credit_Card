import pandas as pd
import numpy as np


def practice1():#replace
    """
    請使用這份資料集, 計算年紀的平均值
    醫療保險金資料集
    """
    df = pd.read_csv(filename)
    df.loc[:,"age"] = df.loc[:,"age"].str.replace("歲","")#也可以寫成replace("40歲","40")但不要寫死比較好
    print(df.loc[:,"age"].astype(int).mean())

def main2():#查看多個資料欄位filter
    df = pd.read_csv(filename)
    print(df[["age","charges"]])
    print(df.filter(like="a"))#like={欄位名稱中部分的名稱}
    print(df.filter(regex='^s'))#使用正規表達式查找符合資料regex = {正則表達式}

def main3():#取出指定資料型別資料
    df = pd.read_csv(filename)
    print(df.dtypes)
    print(df.select_dtypes(include=int))#包含指定類型
    print(df.select_dtypes(exclude=int))#不包含指定類型

def practice4():
    '''
    請使用醫療保險金資料集資料集
    試著將int及float兩種型態欄位以DataFrame方式呈現出來
    '''
    df = pd.read_csv(filename)
    df_int_float = df.select_dtypes(include=[int,float])
    print(df_int_float)

def practice5():
    '''
    請使用醫療保險金資料集資料集
    該資料集中欄位型態如下
    age          object
    sex          object
    bmi         float64
    children      int64
    smoker       object
    region       object
    charges     float64
    請對欄位依照型別進行排序, 呈現的欄位順序為float, int, object
    此例來說, 順序變為bmi, charges, children, age, sex, smoker, region
    '''
    df = pd.read_csv(filename)
    get_int = df.select_dtypes(int)
    get_float = df.select_dtypes(float)
    get_object = df.select_dtypes(object)
    res = get_float.join(get_int).join(get_object)
    print(res)

def main6():
    df = pd.read_csv(filename)
    mean = df.loc[:,"bmi"].mean()
    bigger_mean = df[df.loc[:,"bmi"]>mean]
    print(bigger_mean.sort_values(["bmi"], ascending=True))

def main7():
    df = pd.read_csv(filename)
    '''
    pandas.concat()、Series.append()、pandas.merge() 和 DataFrame.join()
    '''
    #print(pd.concat([df.iloc[0], df.iloc[1]], axis=1))
    #print(pd.merge(df.iloc[0], df.iloc[1], right_index=True, left_index=True))
    #print(df.iloc[0].append(df.iloc[1], ignore_index=True))

def practice8():#mutiindex多重索引
    co_index = pd.MultiIndex.from_tuples(
        [('中華電信','北區'),
         ('中華電信','中區'),
         ('中華電信','南區'),
         ('遠傳電信','北區'),
         ('遠傳電信','中區'),
         ('遠傳電信','南區')]
    )
    values = [600,400,350,550,480,530]
    se = pd.Series(values,index=co_index)
    count = {"中華電信":np.sum(se["中華電信"]),"遠傳電信":np.sum(se["遠傳電信"])}
    print(f"最大值為'{max(count)}', 與對方相差{abs(count['中華電信']-count['遠傳電信'])}人")    

if __name__=="__main__":
    filename = "D:/git/105714234/insurance.csv"
    practice8()




    #常用的正則表示式
    #   .  : 任意字元
    #   \d : 0~9
    #   \D : 非0~9
    #   \s : \t,\n,\f,\r
    #   \S : 非\t,\n,\f,\r,\x0B
    #   \w : a~z,A~Z,0~9
    #   \W : 非a~z,A~Z,0~9
    #   \b : 英文單字的邊界
    #   \B : 非英文單字的邊界
    #==============================================
    #   x?     : x出現0~1次 (先採用1個,再用0個)
    #   x*     : x出現0~n次 (先採用n個,再次用n-1個,...)
    #   x+     : x出現1~n次 (先採用n個,再次用n-1個,...)
    #   x{n}   : x出現n次
    #   x{n,m} : x出現n~m次
    #   [0-9]  : 0~9
    #   [^0-9] : 非0~9 
    #   [A-Z]  : A~Z
    #   [^A-Z] : 非A~Z
    #   [ABC]  : A或B或C