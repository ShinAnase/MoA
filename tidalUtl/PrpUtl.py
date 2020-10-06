import numpy as np
import pandas as pd


from sklearn.preprocessing import LabelEncoder
#ラベルエンコード(文字列→数値)
def Label_encode(train, test, feature_name):
    for f in feature_name:
        lbl = LabelEncoder()
        lbl.fit(list(train[f].values) + list(test[f].values))
        train[f] = lbl.transform(list(train[f].values))
        test[f] = lbl.transform(list(test[f].values))
    
    return train, test



#指定したcolumnと値に応じて欠損値補完を行い、新たにXXX_isnan列を設ける。
def FillnaAndInsertIsnan(DataFrame, ColsAndFillVals):
    dfIsNan = None
    for (col, val) in ColsAndFillVals:
        #欠損値の位置を示すbool列生成
        IsnanSeries = DataFrame[col].isnull()
        #欠損値を補完。
        DataFrame[col] = DataFrame[col].fillna(val)
        #Insert用の欠損値の位置を示すbool列
        if dfIsNan is None:
            dfIsNan = pd.DataFrame(IsnanSeries,columns=[IsnanSeries.name])
            dfIsNan = dfIsNan.rename(columns={IsnanSeries.name: IsnanSeries.name + "_isnan"})
        else:
            dfIsNan.insert(len(dfIsNan.columns), col + "_isnan", IsnanSeries)
        
    return DataFrame, dfIsNan


from sklearn.decomposition import PCA
#主成分解析によるデータの次元削減
#in :dfTrain, dfTest, Dim:制限する次元数,random_state
#out:PCA変換後Train, Test, 学習後pcaモデル
def tidalPCA(dfTrain, dfTest, random_state, Dim=None):
    if Dim is None:
        pca = PCA(random_state = random_state)
    else:
        pca = PCA(n_components = Dim, random_state = random_state)
    data = pd.concat([dfTrain, dfTest])
    pca.fit(data)
    pca_train = pca.transform(dfTrain)
    pca_test = pca.transform(dfTest)
    return pca_train, pca_test, pca


from sklearn.feature_selection import VarianceThreshold
#各特徴量について、threshold(defaultは0.5)より低い分散をdropする。
#In1  :df, trainとtest dataの連結が望ましい。(data = trainFeature.append(testFeature))
#In2  :threshold, どのくらいの大きさの分散までdropするか。(defaultは0.5)
def tidalVarianceThrs(df, threshold=0.5):
    var_thresh = VarianceThreshold(threshold=threshold)
    dfTransformed = var_thresh.fit_transform(df)
    return dfTransformed