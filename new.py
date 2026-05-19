from numpy import where
from collections import Counter
from sklearn.datasets import make_blobs
from matplotlib import pyplot

x,y=make_blobs(n_samples=5000,centers=5,random_state=2)
print(x.shape)

counter=Counter(y)
print(counter)

for i in range(10):
    print(x[i],y[i])

for label, _ in counter.items():
    row_x=where(y==label)[0]
    pyplot.scatter(x[row_x,0], x[row_x,1], label=str(label))
pyplot.legend()
pyplot.show()