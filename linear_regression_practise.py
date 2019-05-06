import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
xs = np.array([10, 9, 2, 15, 10, 16, 11, 16], dtype=np.float64)
ys = np.array([95, 80, 10, 50, 45, 98, 38, 93], dtype=np.float64)

for i in range(len(xs)):
    plt.scatter(xs[i], ys[i])
plt.show()

x_mean = np.sum(xs)/np.size(xs)
y_mean  = np.sum(ys)/np.size(ys)
xy_mean = np.sum(xs*ys)/np.size(xs)

x_mean_square = x_mean*x_mean
x_square_mean = np.sum(xs*xs)/np.size(xs)

m = ((x_mean * y_mean) - xy_mean)/(x_mean_square - x_square_mean)

b = y_mean - (m*x_mean)

print('equation of line is: ', m , 'x +', b)

predict = [ m * x + b for x in xs]
print(predict)

plt.scatter(xs, ys, c='blue', label = 'data')
plt.plot(xs, predict, c='red', label = 'regression line')
plt.legend(loc = 4)
plt.show()

predict_x = 20
predict_y = m * predict_x + b
print('x: ',predict_x, ' y: ',predict_y)