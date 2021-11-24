from itertools import cycle
import matplotlib.colors as colors
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import numpy as np
import pylab
from matplotlib.ticker import NullFormatter
   

def load_data(data_path):

    data = np.loadtxt(data_path, dtype=np.float)
    return data



def plotRes(X, labels):

    colors_ = cycle(colors.cnames.keys())
    #print(colors_ )
    n_clusters = np.unique(labels).size
    for k, col in zip(range(n_clusters), colors_):
        #print(col)
        mask = labels == k
        plt.scatter(X[mask, 0], X[mask, 1], c=col, s=5,edgecolor=col, marker='.', alpha=0.8)
    plt.title('The Distribution of Aggregation Results of the Sysevr Data Set\nThe clustering result is %d categories' % (n_clusters))
    plt.figure()
    
    plt.show()


if __name__ == "__main__":
    BenchMark_vectorList = '/home/ll/data/t-sne/Qemu/Qemu_vecList.txt'
    BenchMark_label_tag =  "/home/ll/data/t-sne/Qemu/Qemu_label.txt"
    BenchMark_tsne = "/home/ll/data/t-sne/Qemu/Qemu_t-SNE2_vecList.txt"


    # load data
    #data = load_data(BenchMark_vectorList)
    #print(len(data))
    # load label
    
    labels = np.loadtxt(BenchMark_label_tag)[:10000]
    #print(labels)

    # t-SNE调参、画图
    #plt.figure(figsize=(18, 6))
    #perplexities = [30]
    #n_iters = [2000, 4000, 6000]
    
    
    #ax = plt.subplot(131 + 30)

    #X_tsne = TSNE(n_components=2, init='pca', random_state=33, perplexity=30, n_iter=1500).fit_transform(data)

    print("circles, perplexity")
       
    #     ax.set_title("perplexity=%d" % perplexity)
    #     ax.scatter(X_tsne[:, 0], X_tsne[:, 1], s=5, c=labels, label='yellow dots--vulnerable func\npurple dots--non-vulnerable func ')
    #     ax.axis('tight')
    #plt.show()
    # save vectors
    #with open(BenchMark_tsne, 'w') as f:
        #a = np.array(X_tsne)
        #np.savetxt(f, a)
  
    X = np.loadtxt(BenchMark_tsne)[:10000]
    Y = labels[:10000]
    # 画有无漏洞图
    plt.scatter(X[:, 0], X[:, 1], s=5, c=labels,marker='+',label='yellow dots--vulnerable func\npurple dots--non-vulnerable func ')
    #plt.scatter(X[:, 0], X[:, 1], s=5,  label='yellow dots--vulnerable func\npurple dots--non-vulnerable func ')
    #plt.scatter(X[:, 0], X[:, 1], s=5)
    #plt.title('the Distribution of Vulnerable and Non-Vulnerable Functions in Sysevr Data Set')
    #plt.figure(figsize=(18, 6))
    plt.axis('off') 
    plt.savefig('/home/ll/data/t-sne/pdf/g2v/gd.pdf')
    plt.show()
    plt.close()
    
    
    # 画聚类结果图
    #labels = np.loadtxt('/home/ll/data/t-sne/Sysevr/ggnn/Sysevr_ggnn_birchlabel1.2.txt')
   # plotRes(X, labels)




