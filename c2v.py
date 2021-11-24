import numpy as np
import pickle
import os
import gc
VECTOR_DIM = 1  #token的向量维度
MAXLEN = 400 

def w2c(corpuspath,vectorpath,labelpath): 
    #将语料库转为向量
    dataset = []
    labels = []
    print("Loading data...")
    #逐个读取训练路径下各个训练数据文件并合并入同一结构
    for filename in os.listdir(corpuspath):
        if 'qe'  not in filename:
            continue
        print(filename)
        f = open(os.path.join(corpuspath,filename),"rb")
        [dataset_file, labels_file] = pickle.load(f,encoding = 'iso-8859-1')
        f.close()
        dataset += dataset_file[:-1]
        labels += labels_file[:-1] 
        print(labels)
        for i in range(len(dataset)):  
            with open(vectorpath,'a') as f: 
                a = np.array(dataset[i])
                #print(a)
                np.savetxt(f, a, newline=' ',fmt='%s')
                f.write('\n')   
            with open(labelpath,'a') as f: 
                label=str(labels[i])
                f.write(label)
                f.write('\n')
                
            


    
if __name__ == "__main__":
    CORPUSPATH = "/home/ll/data/code2vec-master/data/Devign-train/"
    VECTORPATH = "/home/ll/data/t-sne/Qemu/Qemu_vecList.txt"
    LABELPATH = "/home/ll/data/t-sne/Qemu/Qemu_label.txt"
    w2c(CORPUSPATH,VECTORPATH, LABELPATH )
    