import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import linecache
import pandas as pd
def get_line(file, nums_line):
    return linecache.getline(file, nums_line).strip()

#数据输入
file_dir_m0_1 = './test/dist3/m0/ESBN_contextnorm_lr0.0005/run'
arr_m0_1 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m0_1+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m0_1.append(train_accuracy)
    #train_loss_list.append(train_loss)

file_dir_m50_1 = './test/dist3/m50/ESBN_contextnorm_lr0.0005/run'
arr_m50_1 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m0_1+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m50_1.append(train_accuracy)
    #train_loss_list.append(train_loss)

file_dir_m85_1 = './test/dist3/m85/ESBN_contextnorm_lr0.0005/run'
arr_m85_1 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m0_1+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m85_1.append(train_accuracy)
    #train_loss_list.append(train_loss)
    
file_dir_m95_1 = './test/dist3/m95/ESBN_contextnorm_lr0.0005/run'
arr_m95_1 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m95_1+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m95_1.append(train_accuracy)
    #train_loss_list.append(train_loss)

file_dir_m0_2 = './test/dist3/m0/ESBN_default_memory_contextnorm_lr0.0005/run'
arr_m0_2 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m0_2+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m0_2.append(train_accuracy)
    #train_loss_list.append(train_loss)

file_dir_m50_2 = './test/dist3/m50/ESBN_default_memory_contextnorm_lr0.0005/run'
arr_m50_2 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m50_2+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m50_2.append(train_accuracy)
    #train_loss_list.append(train_loss)

file_dir_m85_2 = './test/dist3/m85/ESBN_default_memory_contextnorm_lr0.0005/run'
arr_m85_2 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m85_2+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m85_2.append(train_accuracy)
    #train_loss_list.append(train_loss)
    
file_dir_m95_2 = './test/dist3/m95/ESBN_default_memory_contextnorm_lr0.0005/run'
arr_m95_2 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m95_2+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m95_2.append(train_accuracy)
    #train_loss_list.append(train_loss)

file_dir_m0_3 = './test/dist3/m0/ESBN_confidence_ablation_contextnorm_lr0.0005/run'
arr_m0_3 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m0_3+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m0_3.append(train_accuracy)
    #train_loss_list.append(train_loss)

file_dir_m50_3 = './test/dist3/m50/ESBN_confidence_ablation_contextnorm_lr0.0005/run'
arr_m50_3 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m50_3+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m50_3.append(train_accuracy)
    #train_loss_list.append(train_loss)

file_dir_m85_3 = './test/dist3/m85/ESBN_confidence_ablation_contextnorm_lr0.0005/run'
arr_m85_3 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m85_3+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m85_3.append(train_accuracy)
    #train_loss_list.append(train_loss)
    
file_dir_m95_3 = './test/dist3/m95/ESBN_confidence_ablation_contextnorm_lr0.0005/run'
arr_m95_3 = []
#train_loss_list = []
for f in range(1, 10):
    fname=file_dir_m95_3+str(f)+'.txt'
    current_context = get_line(fname, 2).split()
    train_accuracy = float(current_context[1])
    #train_loss = float(current_context[0])
    arr_m95_3.append(train_accuracy)
    #train_loss_list.append(train_loss)

y1=np.array([np.mean(arr_m0_1), np.mean(arr_m50_1), np.mean(arr_m85_1), np.mean(arr_m95_1)])
y2=np.array([np.mean(arr_m0_2), np.mean(arr_m50_2), np.mean(arr_m85_2), np.mean(arr_m95_2)])
y3=np.array([np.mean(arr_m0_3), np.mean(arr_m50_3), np.mean(arr_m85_3), np.mean(arr_m95_3)])
y123=np.dstack((np.array(y1).T,np.array(y2).T,np.array(y3).T))[0]
std_err1 = [np.std(arr_m0_1), np.std(arr_m50_1), np.std(arr_m85_1), np.std(arr_m95_1)]
std_err2 = [np.std(arr_m0_2), np.std(arr_m50_2), np.std(arr_m85_2), np.std(arr_m95_2)]
std_err3 = [np.std(arr_m0_3), np.std(arr_m50_3), np.std(arr_m85_3), np.std(arr_m95_3)]
std_err123=np.vstack((np.array(std_err1).T,np.array(std_err2).T,np.array(std_err3).T))

#画图
#mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False
bar_width = 0.2
df=pd.DataFrame(y123,index= ['0','50','85','95'],columns=['ESBN','ESBN default memory','ESBN confidence ablation'])
df.plot(kind='bar',yerr=std_err123,rot=0)
#plt.bar_label()
plt.legend(loc=4)
plt.xlabel("m(objects withheld during training)")
plt.ylabel("test accuracy")
plt.title("Distribution-of-three ")
plt.grid(True, axis="x", ls=":", color="gray", alpha=.2)
plt.show()