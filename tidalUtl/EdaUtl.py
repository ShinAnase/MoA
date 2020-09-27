import numpy as np
import pandas as pd

#データの中にnullがあるかどうか調べる。
#in:   DataFrame
#out:  Dataframe(nullのあるcolumnNM, count)
def chkDfIsNull(df):
    chk_tmp = df.isnull().sum() #checking for total null values
    ISNULL = None
    for i in range(len(chk_tmp)):
        # extract null columns
        if chk_tmp[i] != 0:
            print("Column: " + str(df.columns[i]) + "   number: " + str(chk_tmp[i]))
            if ISNULL is None:
                ISNULL = pd.DataFrame([[df.columns[0], chk_tmp[0]]], columns = ["dfColumnNm", "null"])
            else:
                tmp = pd.DataFrame([[df.columns[i], chk_tmp[i]]], columns = ["dfColumnNm", "null"])
                ISNULL = ISNULL.append(tmp)
            
    if ISNULL is not None:
        ISNULL = ISNULL.reset_index(drop=True)
        return ISNULL
    
    print("df is not NULL.")
    return None


#指定列の一意性の確認
#in   :dataframe, column name
#out  :stats(if unique, return None.)
def chkUnique(df, clmnNm):
    numUniq = df[clmnNm].nunique()
    numObs = df.shape[0]
    if numObs == numUniq:
        print(clmnNm + " is unique.")
        return None
    else:
        print(clmnNm + " is not unique.")
        df = pd.DataFrame(df[clmnNm].value_counts()).reset_index()
        df.columns = ["uni_" + clmnNm, "nunique"]
        return df

    
#dfの相関係数を計算。
#絶対値として算出している。
def cnptCorr(df):
    #相関係数の導出 & series化　(相関係数の高い順にソートされている)
    correlations = df.iloc[:,1:].corr().abs().unstack().sort_values(kind="quicksort",ascending=False).reset_index()
    #同じ特徴同士の相関係数は排除
    correlations = correlations[correlations['level_0'] != correlations['level_1']].reset_index(drop=True)
    #列名をわかりやすく
    correlations.columns = ['level_0', 'level_1', "corr"]
    
    return correlations
