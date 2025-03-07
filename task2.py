import numpy as np
import matplotlib.pyplot as plt

#part A
def eulermethod(e,Tf,N):
    times = np.linspace(0,Tf,N)
    q1vals = [1-e]
    q1dotvals = [0]
    q2vals = [0]
    q2dotvals = [((1+e)/(1-e))**0.5]
    for i in range(1,N):
        deltat = times[i]-times[i-1]
        q1dotdot = -q1vals[-1]/((q1vals[-1]**2 + q2vals[-1]**2)**1.5)
        q2dotdot = -q2vals[-1]/((q1vals[-1]**2 + q2vals[-1]**2)**1.5)
        nextq1 = q1vals[-1] + deltat*q1dotvals[-1]
        nextq2 = q2vals[-1] + deltat*q2dotvals[-1]
        nextq1dot = q1dotvals[-1]+deltat*q1dotdot
        nextq2dot = q2dotvals[-1] + deltat*q2dotdot
        q1vals.append(nextq1)
        q2vals.append(nextq2)
        q1dotvals.append(nextq1dot)
        q2dotvals.append(nextq2dot)
    return times, q1vals, q2vals

e=0.6
Tf=200
iter=100000
times0, q1vals0, q2vals0 = eulermethod(e,Tf,iter)
plt.plot(q1vals0, q2vals0)
plt.title("Explicit Euler Method")
plt.xlabel("q1")
plt.ylabel("q2")
plt.savefig("./plots/task2a")
plt.show()
plt.clf


#part B
def symplecticeuler(e,Tf,N):
    times = np.linspace(0,Tf,N)
    q1vals = [1-e]
    q1dotvals = [0]
    q2vals = [0]
    q2dotvals = [((1+e)/(1-e))**0.5]
    for i in range(1,N):
        deltat = times[i]-times[i-1]
        Hq1 = q1vals[-1]/((q1vals[-1]**2 + q2vals[-1]**2)**1.5)
        Hq2 = q2vals[-1]/((q1vals[-1]**2 + q2vals[-1]**2)**1.5)
        nextq1dot = q1dotvals[-1]-deltat*Hq1
        nextq1 = q1vals[-1] + deltat*nextq1dot
        nextq2dot = q2dotvals[-1]-deltat*Hq2
        nextq2 = q2vals[-1] + deltat*nextq2dot
        q1dotvals.append(nextq1dot)
        q2dotvals.append(nextq2dot)
        q1vals.append(nextq1)
        q2vals.append(nextq2)
    return times, q1vals, q2vals

e=0.6
Tf=200
iter=400000
times, q1vals, q2vals = eulermethod(e,Tf,iter)
plt.plot(q1vals, q2vals, color="blue", label="Symplectic")
plt.plot(q1vals0, q2vals0,color="red",label="Explicit")
plt.title("Explicit vs Symplectic Euler Method")
plt.xlabel("q1")
plt.ylabel("q2")
plt.savefig("./plots/task2b")
plt.legend()
plt.show()
plt.clf