import pandas as pd
import numpy as np
import datetime

def main1():#loc/iloc pratice
    nums = [i for i in range(10)]
    index = [i for i in range(10,20) ]
    #print(dict(zip(index, nums)))
    Series1 = pd.Series(dict(zip(index, nums)))
    print(Series1)
    print('-'*20)
    print(Series1.iloc[[0]])

def main2():#
    '''
    練習
    有個Series結構如下, 請回答以下問題
    各科平均分數為何？
    list中兩個分數代表兩個學生
    請問第一個學生的平均分數為何？
    請問第二個學生的平均分數為何？
    國文    [100, 80]
    英文     [72, 90]
    數學     [92, 90]
    自然     [88, 93]
    社會     [87, 82]
    dtype: object
    '''
    def column():
        s1 = 0
        s2 = 0
        s1 += Series_grades.iloc[i][0]
        s2 += Series_grades.iloc[i][1]
        return s1, s2

    nums = [[100, 80],[72, 90],[92, 90],[88, 93],[87, 82]]
    index = ["國文","英文","數學","自然","社會"]
    dic_data = dict(zip(index, nums))
#-------------------------------------------------------------------------------------------------------------
    Series_grades = pd.Series(dic_data)
    print(f'原檔案:\n{Series_grades}')
    print('-'*20)
    average_grades = Series_grades.map(np.mean)
    print(f'平均值:\n{average_grades}')
#-------------------------------------------------------------------------------------------------------------2-1
    student1 = 0
    student2 = 0
    for i in range(len(Series_grades)):
        student1 += Series_grades.iloc[i][0]
        student2 += Series_grades.iloc[i][1]
    print(f"Student1:{student1/len(Series_grades)}")
    print(f"Student2:{student2/len(Series_grades)}")
#-------------------------------------------------------------------------------------------------------------2-2
    Dataframe_grades = pd.DataFrame(dic_data, index=[1,2])
    person_grades = Dataframe_grades.mean(axis=1)
    print(f"第一位同學的平均值為:{person_grades.iloc[0]}\n第一位同學的平均值為:{person_grades.iloc[1]}")
#-------------------------------------------------------------------------------------------------------------2-3
    SV = Series_grades.values
    nA = np.array(list(SV))
    print(np.mean(nA, axis=0))

def main3():
    '''
    有個dictionary如下，請使用這個字典建立一個DataFrame
    Score_dict = {
    "English":85,
    "Chinese":88,
    "Math":70,
    "Society":82,
    "Natural":100
    }
    對於這個DataFrame篩選出分數介於80~90分的科目
    '''
    Score_dict = {
    "English":85,
    "Chinese":88,
    "Math":70,
    "Society":82,
    "Natural":100
    }

    df = pd.DataFrame({"Score":Score_dict})
    print(f'orign:\n{df}\n')
    print(df[(df['Score']>80) & (df['Score']<90)])
    print("answer:\n", df[(df['Score']>80) & (df['Score']<90)].index)#answer
    print(df[(df['Score']>80) & (df['Score']<90)])

def main4():
    Peter = pd.Series({
    "Math":80,
    "Chinese":78,
    "English":88,
    "Society":70,
    "Natural":100
    })
    Mary = pd.Series({
    "Math":70,
    "Chinese":62,
    "English":90,
    "Society":78,
    "Natural":82
    })
    Score = pd.DataFrame({"Peter":Peter, "Mary":Mary})
    print(Score)
    index_S = Score.index.to_list()
    column_S = Score.columns.to_list()
    index_S[0]='math'
    column_S[0] = "P"
    Score.index = index_S
    Score.columns = column_S
    print(Score)
    Score = Score.rename(columns={'P':2})
    print(Score)
    Score = Score.rename(index=lambda x: x.upper())
    print(Score)
    Score = Score.rename(index=lambda x: x.lower())
    print(Score)

def main5():
    '''
    有個DataFrame如下
    Name   Local    Birthday
    0    Peter   新北市   1990/8/20
    1  Richard   台中市   1981/7/29
    2   Storen   新北市   1982/4/24
    3     Mary   台北市   1988/10/21
    請對於上述DataFrame產生一個Age欄位(Age欄位由Birthday計算，年紀為整數無小數點)
    PS:可能使用到的方法：
    轉換時間型態：pd.to_datetime()
    現在時間：datetime.datetime.today()
    datetime型態取天數：datetime_Variable.dt.days
    '''
    data = {
        "Name":['Peter', 'Richard', 'Storen', 'Mary'],
        "Local":['新北市', '台中市', '新北市', '台北市'],
        "Birthday":['1990/8/20', '1981/7/29', '1982/4/24', '1988/10/21']
    }

    or_df = pd.DataFrame(data)
    print(f'原資料:\n{or_df}')
    b_se = or_df["Birthday"].values#ndarray_str日期
    b_se = np.array(list(b_se))
    print(b_se)
    date = np.where(b_se.dtype == 'object', pd.to_datetime(b_se), b_se)
    print
    print(datetime.datetime.today() - date)

    #or_df['Age']=
    #print(or_df)


if __name__=='__main__':
    #main1()
    #main2()
    #main3()
    #main4()
    main5()