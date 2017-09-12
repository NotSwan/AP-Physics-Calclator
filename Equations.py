import numpy as np
import time

Xo = 0.0
Vox = 0.0
ax = 0.0
t = 0.0

def vXf():
    Xf = input('Xf = ')
    float(Xf)
def vXo():
    Xo = input('Xo = ')
    float(Xo)
def vVox():
    Vox = input('Vox = ')
    float(Vox)
def vt():
    t = input('t = ')
    float(t)
def vax():
    ax = input('ax = ')
    float(ax)

def EQ1_solveFor_Xf():
    vXo()
    vVox()
    vt()
    vax()
def EQ1_solveFor_Xo():
    vXf()
    vVox()
    vt()
    vax()
def EQ1_solveFor_Vox():
    vXo()
    vXf()
    vt()
    vax()
def EQ1_solveFor_t():
    vXo()
    vVox()
    vXf()
    vax()
def EQ1_solveFor_ax():
    vXo()
    vVox()
    vt()
    vXf()
def wait():
    time.sleep(0.5)

def equation1():
    if solving == '1' and solving_for == '1':
        print('Solving for Xf needs the Xo, Vox, t, and ax variables')
        wait()
        EQ1_solveFor_Xf()
        Answer = ((Xo) + (Vox)*(t) + (((0.5)*(ax))*(t ** 2)))
        Xf = Answer
        print('Your answer is:')
        print(Xf)

print('Welcome to the AP Physics Calculator!')
wait()
print('Equation 1: Xf = Xo + Vox t + 0.5 ax t^2')
wait()
print('Equation 2: Vf^2 = Vo^2 + 2a DeltaX')
wait()
print('Equation 3: Vf = Vo + a t')
wait()
solving = input('You are solving equation 1 2 or 3?: ')
wait()

if solving == '1':
    print('What variable are you missing to solve this equation?')
    wait()
    print('Variable 1, Xf?')
    wait()
    print('Variable 2, Xo?')
    wait()
    print('Variable 3, Vox?')
    wait()
    print('Variable 4, t?')
    wait()
    print('Variable 5, ax?')
    wait()

solving_for = input('Solve this equation for Variable: ')

equation1()