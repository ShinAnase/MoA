import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

#指定列のカテゴリカルな特徴量のヒストグラムをtrain, testの順に並べる。
#in  :train data, testdata, visualizing column name
#out :-
def histCategory(dfTrain, dfTest, clmnNm):
    figure = plt.figure(figsize=(12, 4))
    gs_master = GridSpec(nrows=1, ncols=2, figure=figure)
    
    ax1 = figure.add_subplot(gs_master[0, 0])
    ax1.set_title("Train " + clmnNm,weight='bold')
    sns.countplot(x=clmnNm,
                  data=dfTrain,
                  ax=ax1,
                  order=dfTrain[clmnNm].value_counts().index)
    total = float(len(dfTrain[clmnNm]))
    for p in ax1.patches:
        ax1.text(p.get_x() + p.get_width() / 2., #width(x) :get_xは棒グラフの左端の位置
                p.get_height() + 2, #height(y)
                '{:1.2f}%'.format((p.get_height() / total) * 100),
                ha='center')
    
    
    ax2 = figure.add_subplot(gs_master[0, 1])
    ax2.set_title("Test " + clmnNm,weight='bold')
    sns.countplot(x=clmnNm,
                  data=dfTest,
                  ax=ax2,
                  order=dfTest[clmnNm].value_counts().index)
    total = float(len(dfTest[clmnNm]))
    for p in ax2.patches:
        ax2.text(p.get_x() + p.get_width() / 2., #width(x) :get_xは棒グラフの左端の位置
                p.get_height() + 2, #height(y)
                '{:1.2f}%'.format((p.get_height() / total) * 100),
                ha='center')
    
    return


# Index付き1次元データフレームのヒストグラム表現(横向き)
def histCntHorizontal(cntWithIdx):
    fig = plt.figure(figsize=(20,15))
    sns.barplot(y = cntWithIdx.reset_index()["index"].astype(str), x = cntWithIdx.values)
    plt.show()
    return

# Index付き1次元データフレームのヒストグラム表現(縦向き)
def histCntVertical(cntWithIdx):
    fig = plt.figure(figsize=(20,15))
    sns.barplot(x = cntWithIdx.reset_index()["index"].astype(str), y = cntWithIdx.values)
    plt.show()
    return