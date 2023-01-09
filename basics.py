import numpy as np

print('Hi!\nI include Numpy!\nFor some Help run:\n- basics_info()\n- detlef()')
#planets Mein Vater erklärt mir jeden Sonntag unseren Nachthimmel
Names=['Sun', 'Merkur', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptun']
def basics_info():
    print('Parameter included:\nGraviticional constants Gc and µ\nAstonomical Unit au\nSemi-Major_axis of Planets(Heliocentric) ap\nPlanet Radius R')
    print('np.pi is already pi, same for sin cos & tan')
    print('includes Ammount Strokes with sign()\n')
    print('includes format funktion for 6digits with fun()\n')
    print('includes Velocity calculation for Circular orbits with v_circular(x,y),')
    print('  x=planet number or mu of Central body')
    print('  y= Semi-major-axis or with Orbit height\n')
    print('calculates amount of a vector with amount(x)\n')
    print('calculates  A x B with cross(a,b)\n')
    print('rounding is possible with truncate([value],[digits])')
    
    print("")
def detlef():
    x=np.size(Names)
    print('The Indices are in the Order of the Solarsytem')
    i=0
    while i<x:
        print(str(i)+'='+Names[i])
        i=i+1
    return
#some basic functions
pi=np.pi
def sin(x): 
    return np.sin(x)
def cos(x): 
    return np.cos(x)
def tan(x): 
    return np.tan(x)
def sign(x):
    if np.size(x)>1:
        print('Warning:\nsign() may be disfunctional for this task, please check, ignore if okay')
    store=x**2
    x=store**0.5
    return x
def fun(x):
    return format(x,'.5')
#constants

#Day
d_sederial=86164.09053083288 #s

#Speed of light in Vacuum
c0=299792.458 #km/s
# Gravitational constant km^3/(kg*s^2)
Gc=6.6743*10**(-20)

#Standard gravitational acceleration on Earth’s surface
g0=9.80665 #m/s^2
J2=0.00108263 # J2 Term earth
#Astronomical unit
auc = 149597870.700 #km


#Parameters
mu=np.linspace(0,2,9) # µ of Planets
mu[0]= 132712439935.5 #µ_sun km^3/s^2
mu[1]=22032.1 
mu[2]=324858.8        
mu[3]=398600.4     
mu[4]=42828.3
mu[5]=126711995.4
mu[6]=37939519.7
mu[7]=5780158.5
mu[8]=6871307.8

R=np.linspace(0,2,9) #radius Planets
R=[696000, 2439.7, 6051.8, 6378.14, 3397, 71492, 60268, 25559, 24764, 1737.4] #km
ap_au=np.linspace(0,2,9) # Semi Major axis planets
ap=np.linspace(0,2,9)
ap_au=np.array([0, 0.387099, 0.723336, 1.000003, 1.523710, 5.202887,  9.536676,  19.189165, 30.069923])
I=1
ap=ap_au*auc
#some shorts for Earth and sun

ms=mu[0]
me=mu[3]
Re=R[3]




def v_circular(x,y):
    mue=x
    if x<np.size(Names):
        if y<R[x]:
            y=R[x]+y
        mue=mu[x]
    v_circular=(mue/y)**0.5
    print(fun(v_circular)+'km/s')
    return v_circular
    
def amount(x):
    i=0
    tmp=0
    for i in x:
        tmp=sign(i)**2+tmp
    tmp=tmp**0.5
    print('Amount is: '+fun(tmp))
    return tmp

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n* multiplier)/multiplier

def r2d(x): return np.rad2deg(x)