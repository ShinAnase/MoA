import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

cust_palt = ['#111d5e','#c70039','#37b448','#B43757', '#ffbd69', '#ffc93c','#FFFF33','#FFFACD',]

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
    fig = plt.figure(figsize=(20,10))
    sns.barplot(x = cntWithIdx.reset_index()["index"].astype(str), y = cntWithIdx.values)
    plt.show()
    return

# 1次元データフレームのカーネル密度推定法(KDE)による分布表現
def distKde(distDf):
    fig = plt.figure(figsize=(20,10))
    sns.kdeplot(distDf.values, shade=True)
    plt.show()
    return

#meta情報(mean, median, min, max, std, variance, skew(歪度), kurtosis(尖度))の分布
#train, testのメタ情報の差異を調べる
def metaDist(dfTrain, dfTest):
    fig = plt.figure(constrained_layout=True, figsize=(20, 16))
    grid = GridSpec(ncols=4, nrows=4, figure=fig)
    
    ax1 = fig.add_subplot(grid[0, :2])
    ax1.set_title('Distribution of Mean Values per Column', weight='bold')
    sns.kdeplot(dfTrain.mean(axis=0),color=cust_palt[0], shade=True, label='Train')
    sns.kdeplot(dfTest.mean(axis=0),color=cust_palt[1], shade=True, label='Test')
    
    ax2 = fig.add_subplot(grid[0, 2:])
    ax2.set_title('Distribution of Median Values per Column', weight='bold')
    sns.kdeplot(dfTrain.median(axis=0),color=cust_palt[0], shade=True, label='Train')
    sns.kdeplot(dfTest.median(axis=0),color=cust_palt[1], shade=True, label='Test')
    
    ax3 = fig.add_subplot(grid[1, :2])
    ax3.set_title('Distribution of Minimum Values per Column', weight='bold')
    sns.kdeplot(dfTrain.min(axis=0),color=cust_palt[0], shade=True, label='Train')
    sns.kdeplot(dfTest.min(axis=0),color=cust_palt[1], shade=True, label='Test')
    
    ax4 = fig.add_subplot(grid[1, 2:])
    ax4.set_title('Distribution of Maximum Values per Column', weight='bold')
    sns.kdeplot(dfTrain.max(axis=0),color=cust_palt[0], shade=True, label='Train')
    sns.kdeplot(dfTest.max(axis=0),color=cust_palt[1], shade=True, label='Test')
    
    ax5 = fig.add_subplot(grid[2, :2])
    ax5.set_title('Distribution of Std\'s per Column', weight='bold')
    sns.kdeplot(dfTrain.std(axis=0),color=cust_palt[0], shade=True, label='Train')
    sns.kdeplot(dfTest.std(axis=0),color=cust_palt[1], shade=True, label='Test')
    
    ax6 = fig.add_subplot(grid[2, 2:])
    ax6.set_title('Distribution of Variances per Column', weight='bold')
    sns.kdeplot(dfTrain.var(axis=0),color=cust_palt[0], shade=True, label='Train')
    sns.kdeplot(dfTest.var(axis=0),color=cust_palt[1], shade=True, label='Test')
    
    ax7 = fig.add_subplot(grid[3, :2])
    ax7.set_title('Distribution of Skew Values per Column', weight='bold')
    sns.kdeplot(dfTrain.skew(axis=0),color=cust_palt[0], shade=True, label='Train')
    sns.kdeplot(dfTest.skew(axis=0),color=cust_palt[1], shade=True, label='Test')
    
    ax8 = fig.add_subplot(grid[3, 2:])
    ax8.set_title('Distribution of Kurtosis Values per Column', weight='bold')
    sns.kdeplot(dfTrain.kurtosis(axis=0),color=cust_palt[0], shade=True, label='Train')
    sns.kdeplot(dfTest.kurtosis(axis=0),color=cust_palt[1], shade=True, label='Test')
    
    plt.suptitle('Meta Distributions of Train/Test Set', fontsize=25, weight='bold')
    plt.show()
    
    return