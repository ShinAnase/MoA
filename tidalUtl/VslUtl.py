import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

#指定列のヒストグラムをtrain, testの順に並べる。
#in  :train data, testdata, visualizing column name
#out :-
def histColumn(dfTrain, dfTest, clmnNm):
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