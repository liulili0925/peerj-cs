import numpy as np
import pickle
import os
import gc
from gensim.models.word2vec import Word2Vec   
VECTOR_DIM = 40  #token的向量维度
MAXLEN = 900 

def w2c(corpuspath,vectorpath,w2path): 
    #将语料库转为向量
    print("turn the corpus into vectors...")
    model = Word2Vec.load(W2VPATH)
    #对于每一个程序id的文件夹
    for corpusfile in os.listdir(CORPUSPATH):  
        corpus_path = os.path.join(CORPUSPATH, corpusfile)
        #print(corpus_path)
        f_corpus = open(corpus_path, 'rb')
        data = pickle.load(f_corpus)
        f_corpus.close()
            #转向量
        data.append(data[0])
        data[0] = generate_corpus(model, data[0])
           #存储
        #print("saving vectors......")
        with open(vectorpath,'a') as f: 
            
            # print(model.docvecs[i])
            a = np.array(data[0])
            # print(a)
            np.savetxt(f, a, newline=' ')
            f.write('\n')
    
def generate_corpus(model, sample):

    dl_corpus = []
    for word in sample:
        if word in model:
            data=model[word]
        else:
            data=[0]*VECTOR_DIM

    return data
if __name__ == "__main__":
    CORPUSPATH = "/home/ll/data/BenchMark/corpus_nomap0813/Devign/"
    VECTORPATH = "/home/ll/data/t-sne/Devign/w2v/Devign_vecList.txt"
    W2VPATH = "/home/ll/data/BenchMark/w2v_model/wordmodel_min_iter5.model"
    w2c(CORPUSPATH,VECTORPATH, W2VPATH )
    