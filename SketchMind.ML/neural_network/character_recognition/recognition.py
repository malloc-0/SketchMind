# 导入需要的包, Sequential()是最简单的模型——序贯模型
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.datasets import mnist
import numpy as np

# 搭建网络
model = Sequential()
model.add(Dense(500,input_shape=(784,))) #输入层， 28*28=784
model.add(Activation('tanh'))
model.add(Dropout(0.5)) #50% dropout

model.add(Dense(500)) #隐藏层， 500
model.add(Activation('tanh'))
model.add(Dropout(0.5)) #50% dropout

model.add(Dense(8)) #输出结果， 10
model.add(Activation('softmax'))
# 详解
# 通过model.add()增加模型的层数。其中Dense()设定该层的结构，第一个参数表示输出的个数，
# 第二个参数是接受的输入数据的格式。第一层中需要指定输入的格式，在之后的增加的层中输入层
# 节点数默认是上一层的输出个数。Actication()指定激活函数，Dropout()指定每层要丢掉的
# 节点信息百分比。输出层激活函数一般为softmax，不需要丢弃节点。

# 编译模型
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True) #设定学习效率等参数
model.compile(loss = 'categorical_crossentropy', optimizer=sgd, metrics=['accuracy']) #使用交叉熵作为loss
# 详解
# 使用优化器sgd来编译模型，用来指定学习效率等参数。编译时指定loss函数，这里使用交叉熵函数作为loss函数。
# metrics 用来展示训练的acc正确率

# 读取数据
(x_train,y_train),(x_test,y_test) = mnist.load_data() #使用mnist读取数据（第一次需要下载）

X_train = x_train.reshape(x_train.shape[0], x_train.shape[1]*x_train.shape[2])
X_test = x_test.reshape(x_test.shape[0],x_test.shape[1]*x_test.shape[2])

Y_train = (np.arange(10) == y_train[:,None]).astype(int) #将index转换橙一个one_hot矩阵
Y_test = (np.arange(10) == y_test[:,None]).astype(int)
# 详解
# 读取minst数据集，通过reshape()函数转换数据的格式。
# 如果我们打印x_train.shape会发现它是(60000,28,28)，即一共60000个数据，每个数据
# 是28*28的图片。通过reshape转换为(60000,784)的线性张量。
# 如果我们打印y_train会发现它是一组表示每张图片的表示数字的数组，通过numpy的arange()
# 和astype()函数将每个数字转换为一组长度为10的张量，代表的数字的位置是1，其它位置为0.

# 对使用转换后的数据对模型进行训练
model.fit(X_train,Y_train,batch_size=200,epochs=10,shuffle=True,verbose=1,validation_split=0.3)
# 详解
# 其中，batch_size表示每个训练块包含的数据个数，epochs表示训练的次数，shuffle表示是
# 否每次训练后将batch打乱重排，verbose表示是否输出进度log，validation_split指定验证集占比

# 输出对测试集进行测试的结果
print("test set")
scores = model.evaluate(X_test,Y_test,batch_size=200,verbose=1)
print("")
print("The test loss is")
print(scores)
result = model.predict(X_test,batch_size=200,verbose=1)

result_max = np.argmax(result, axis = 1)
test_max = np.argmax(Y_test, axis = 1)

result_bool = np.equal(result_max, test_max)
true_num = np.sum(result_bool)
print("")
print("The accuracy of the model is %f" % (true_num/len(result_bool)))
# 详解
# model.evaluate()计算了测试集中的识别的loss值。
# 通过model.predict()，我们可以得到对于测试集中每个数字的识别结果，每个数字对应一个表示每个数字都是多少概率的长度为10的张量。
# 通过np.argmax()，我们得到每个数字的识别结果和期望的识别结果
# 通过np.equal()，我们得到每个数字是否识别正确
# 通过np.sum()得到识别正确的总的数字个数

# 作者：JackieXiao
# 链接：https://www.jianshu.com/p/6bf2c54a9d60
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。