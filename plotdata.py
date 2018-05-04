import random
import matplotlib.pyplot as plt


x = [i for i in range(101)]
y = [random.randint(1, 101) for i in range(101)]

plt.plot(x, y)
plt.xlabel('income')
plt.ylabel('mortality')
plt.title('first group before summation -- picture 3')
plt.show()

Y = [[random.randint(1, 101) for i in range(101)] for j in range(10000)]
Y_value = [0 for i in range(101)]
for y in Y:
    Y_value = [Y_value[i] + y[i] for i in range(len(y))]

plt.plot(x, Y_value)
plt.xlabel('income')
plt.ylabel('mortality')
plt.title('first group after summation')
plt.ylim(0, 600000)
plt.show()


x = [i for i in range(101)]
y = [random.randint(int(i/2), int((i+100)/2)) for i in range(101)]

plt.plot(x, y)
plt.xlabel('age')
plt.ylabel('mortality')
plt.title('first group before summation -- picture 3')
plt.show()

Y = [[random.randint(int(i/2), int((i+100)/2)) for i in range(101)] for j in range(10000)]
Y_value = [0 for i in range(101)]
for y in Y:
    Y_value = [Y_value[i] + y[i] for i in range(len(y))]

plt.plot(x, Y_value)
plt.xlabel('age')
plt.ylabel('mortality')
plt.title('first group after summation')
##plt.ylim(0, 00000)
plt.show()
