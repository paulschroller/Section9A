import numpy as np
import matplotlib.pyplot as plt
import random

#part a)
def costfunc(theta):
    return theta**4 - 8*theta**2 - 2*np.cos(4*np.pi*theta)

def gradientfunc(theta):
    return 4*theta**3 - 16*theta + 8*np.pi*np.sin(4*np.pi*theta)

"""
thetavals = np.linspace(-3,3,1000)
Hvals = costfunc(thetavals)
plt.plot(thetavals,Hvals)
alpha = 0.02
theta0 = -1
guesses1 = [theta0]
lowestval = theta0
plt.plot(guesses1[0],costfunc(guesses1[0]),linewidth=0, marker='o',color="red")
while True:
    nextval = guesses1[-1] - alpha*gradientfunc(guesses1[-1])
    if costfunc(nextval) < costfunc(lowestval):
        lowestval = nextval
    guesses1.append(nextval)
    plt.plot(guesses1[-1],costfunc(guesses1[-1]),linewidth=0,marker='o', color='red')
    if np.abs(guesses1[-1]-guesses1[-2]) < 0.00000001:
        break
    if len(guesses1) > 1000:
        break
    if np.abs(guesses1[-1]) > 5:
        break
plt.savefig("./plots/task3a1")
plt.show()
plt.clf
print(lowestval)


thetavals = np.linspace(-3,3,1000)
Hvals = costfunc(thetavals)
plt.plot(thetavals,Hvals)
alpha = 0.02
theta0 = 0.5
guesses1 = [theta0]
lowestval = theta0
plt.plot(guesses1[0],costfunc(guesses1[0]),linewidth=0, marker='o',color="red")
while True:
    nextval = guesses1[-1] - alpha*gradientfunc(guesses1[-1])
    if costfunc(nextval) < costfunc(lowestval):
        lowestval = nextval
    guesses1.append(nextval)
    plt.plot(guesses1[-1],costfunc(guesses1[-1]),linewidth=0,marker='o', color='red')
    if np.abs(guesses1[-1]-guesses1[-2]) < 0.00000001:
        break
    if len(guesses1) > 1000:
        break
    if np.abs(guesses1[-1]) > 5:
        break
plt.savefig("./plots/task3a2")
plt.show()
plt.clf
print(lowestval)


thetavals = np.linspace(-3,3,1000)
Hvals = costfunc(thetavals)
plt.plot(thetavals,Hvals)
alpha = 0.02
theta0 = 3
guesses1 = [theta0]
lowestval = theta0
plt.plot(guesses1[0],costfunc(guesses1[0]),linewidth=0, marker='o',color="red")
while True:
    nextval = guesses1[-1] - alpha*gradientfunc(guesses1[-1])
    if costfunc(nextval) < costfunc(lowestval):
        lowestval = nextval
    guesses1.append(nextval)
    plt.plot(guesses1[-1],costfunc(guesses1[-1]),linewidth=0,marker='o', color='red')
    if np.abs(guesses1[-1]-guesses1[-2]) < 0.00000001:
        break
    if len(guesses1) > 1000:
        break
    if np.abs(guesses1[-1]) > 5:
        break
plt.savefig("./plots/task3a3")
plt.show()
plt.clf
print(lowestval)
"""

#part b)
steps = 1000
beta = 1
sigma=1
theta0 = -1
guesses = [theta0]
thetavals = np.linspace(-3,3,1000)
Hvals = costfunc(thetavals)
plt.plot(thetavals,Hvals)
plt.plot(guesses[0],costfunc(guesses[0]),linewidth=0,marker='o',color='red')
for i in range(steps):
    nextval = guesses[-1] + random.gauss(0,sigma)
    ratio = np.exp(-beta*(costfunc(nextval) - costfunc(guesses[-1])))
    if ratio >= 1:
        guesses.append(nextval)
        plt.plot(guesses[-1],costfunc(guesses[-1]),linewidth=0,marker='o',color='red')
    elif random.random() < ratio:
        guesses.append(nextval)
        plt.plot(guesses[-1],costfunc(guesses[-1]),linewidth=0,marker='o',color='red')

plt.savefig("./plots/task3b")