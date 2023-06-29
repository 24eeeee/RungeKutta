import numpy as np
import matplotlib.pyplot as plt


def frange(start, stop=None, step=None):
    start = float(start)
    step = 1. if step is None or step == 0 else float(step)
    stop += step
    c = 0
    while True:
        temp = start + step * c
        if 0 < step and abs(abs(temp - stop) - step) < step:
            break
        elif 0 > step > abs(abs(temp - stop) - step):
            break
        yield temp
        c += 1


def read_data_from_standard_input():
    print("Input m:")
    m = float(input())
    print("Input p:")
    p = float(input())
    print("Input k:")
    k = float(input())

    print("Input y_0:")
    y_0 = float(input())
    print("Input dy_0:")
    dy_0 = float(input())

    print("Input step:")
    h = float(input())
    print("Input x_final:")
    x_n = float(input())

    return m, p, k, y_0, dy_0, h, x_n


def runge_kuttas(m: float, p: float, k: float, x_0: float, y_0: float, dy_0: float, h: float, x_n: float):
    ddy = lambda m, p, k, dy, y: (-p * dy - k * y) / m
    nxt = lambda k1, k2, k3, k4: (k1 + 2 * k2 + 2 * k3 + k4) / 6

    result_x = [x_0]
    result_y = [y_0]
    result_dy = [dy_0]

    for iter_x in frange(x_0, x_n, h):
        k1 = h * result_dy[-1]
        dk1 = h * ddy(m, p, k, result_dy[-1], result_y[-1])

        k2 = h * (result_dy[-1] + dk1 / 2)
        dk2 = h * ddy(m, p, k, result_dy[-1] + dk1 / 2, result_y[-1] + k1 / 2)

        k3 = h * (result_dy[-1] + dk2 / 2)
        dk3 = h * ddy(m, p, k, result_dy[-1] + dk2 / 2, result_y[-1] + k2 / 2)

        k4 = h * (result_dy[-1] + dk3)
        dk4 = h * ddy(m, p, k, result_dy[-1] + dk3, result_y[-1] + k3)

        result_x.append(round(iter_x + h, len(str(h)) - 1))
        result_y.append(result_y[-1] + nxt(k1, k2, k3, k4))
        result_dy.append(result_dy[-1] + nxt(dk1, dk2, dk3, dk4))

    return result_x, result_y, result_dy


m, p, k, y_0, dy_0, h, x_n = read_data_from_standard_input()
x_0 = 0
res_x, res_y, res_dy = runge_kuttas(m, p, k, x_0, y_0, dy_0, h, x_n)
x = np.array(res_x)
y = np.array(res_y)
plt.plot(res_x, res_y, label='y')
plt.plot(res_x, res_dy, label='dy')
plt.xlabel('x')
plt.legend(loc='best')
plt.grid(True)
plt.show()
