from math import *
import matplotlib.pyplot as plt 
def Projectile_motion(yini,vo,ang,axcom,aycom):
    if aycom == 0:
        print("Error Y component acceleration cannot be zero")
        return 
    vxo = vo*cos(ang*(pi/180))
    vyo = vo*sin(ang*(pi/180))
    t=0
    x=0
    y=yini
    xval=[]
    yval=[]    
    while y >= 0:
        t = t + 0.001
        x = vxo*t + (1/2)*axcom*t**2
        y = vyo*t + (1/2)*aycom*t**2 + yini
        xval.append(x)
        yval.append(y)
    plt.plot(xval,yval)
    z = plt.gca()
    z.set_ylim([0,max(yval)])
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Projectile Motion Simulator")
    