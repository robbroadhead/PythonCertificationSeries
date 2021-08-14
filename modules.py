# Examples of python modules __name__, named imports, from x import *, import x as y, dir(module)
# packages
import samples.mymod as sm
import mymod as m
#from mymod import add, multiply, myName
#from mymod import *
from mymod import add as ad, multiply as mu, myName as mn
import samples.mymod2 as sm2

print(dir())
#sm.me()

print(str(ad(2, 3)))

print(str(mu(2, 3)))

print("What is m?:")
print(m.__name__)

# Initial examples
print(mn)
print(sm.myName2)
print(m.myName)
print(str(m.add(2, 3)))
