import json
import numpy as np
def g2v(corpuspath,vectorpath,labelpath,maxlen=40):
    with open(corpuspath, encoding='utf-8') as f:
        line = f.readline()
        labels=[]
        dataset=[]
        d = json.loads(line)
        for i in range(len(d)):
            targets = d[i]['target']
            node_features = d[i]['graph_feature']
            labels.append(targets)
            dataset.append(node_features[69:])
        print(len(labels),len(dataset))
        for i in range(len(dataset)):  
            
            with open(vectorpath,'a') as f: 
                a = dataset[i]
                #print(len(a))
                fill_0 = [0]*40
                if len(a) <=  maxlen:
                    a = a + [fill_0] * (maxlen - len(a))
                else:
        #大于maxlen的数据做截取，直接截取maxlen长度
                    a = a[:maxlen]
                a=np.array(a)
                #print(a)
                np.savetxt(f, a, newline=' ')
                f.write('\n')   
            with open(labelpath,'a') as f: 
                label=str(labels[i])
                f.write(label)
                f.write('\n')
            
        f.close()
if __name__ == "__main__":
    CORPUSPATH = "/home/ll/data/ReVeal-bad/data/after_ggnn/Sysevr/train_GGNNinput_graph.json"
    VECTORPATH = "/home/ll/data/t-sne/Sysevr/ggnn/Sysevr_ggnn_vecList.txt"
    LABELPATH = "/home/ll/data/t-sne/Sysevr/ggnn/Sysevr_ggnn_label.txt"
    g2v(CORPUSPATH,VECTORPATH, LABELPATH )