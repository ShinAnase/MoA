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


