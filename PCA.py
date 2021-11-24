# import PCA as pc
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt


# /home/y/GraduationProject/doc2vec/devign_data/devign_vecList_100size_400iter.txt
# /home/y/GraduationProject/doc2vec/SeVC_data/SeVC_vecList_100size_200iter.txt
# /home/y/GraduationProject/doc2vec/SARD_data/vecList_120_1_500.txt

def load_data(data_path):
    
    data = np.loadtxt(data_path, dtype=np.float)
    return data




if __name__ == "__main__":

    vectorList = "/home/ll/data/t-sne/Sysevr/ggnn/Sysevr_ggnn_vecList.txt"
   
    PCA_path= '/home/ll/data/t-sne/Sysevr/ggnn/Sysevr_ggnn_15size.txt'
   


    data_path = vectorList
    data = load_data(data_path)
    #print(len(data[1]))

    # 设置降维的维数
    pca1 = PCA(n_components=15)
    res = pca1.fit_transform(data)

    # explained_variance_ratio_，它代表降维后的各主成分的方差值占总方差值的比例，这个比例越大，则越是重要的主成分。
    ratio = pca1.explained_variance_ratio_
    print("各特征的权重为: ratio = ",ratio)
    print("使用sklearn.decomposition.PCA 的结果为: res = ", res)

    # 保存降维后的向量
   
    with open(PCA_path,'w') as f:
        a = np.array(res)
        np.savetxt(f, a)
    
    

