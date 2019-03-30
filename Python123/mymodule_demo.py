import mymodule
mymodule.say_hi()
print('Version',mymodule.__version__)

from mymodule import say_hi,__version__
say_hi()
print('Version',__version__)