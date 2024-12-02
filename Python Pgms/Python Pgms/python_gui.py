Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.moveTo(10,10)
>>> pyautogui.moveTo(10,10,2)
>>> 
>>> pyautogui.moveTo(10,100,2)
>>> pyautogui.moveTo(1280,720)
>>> pyautogui.moveTo(1280,720,2)
>>> pyautogui.moveTo(2000,720,2)
>>> pyautogui.moveTo(1880,720,2)
>>> 
>>> pyautogui.moveTo(1280,720,0.2)
>>> pyautogui.moveTo(1280,720)
>>> pyautogui.moveTo(1280,720)
>>> pyautogui.MINIMUM_SLEEP
0.05
>>> pyautogui.MINIMUM_SLEEP(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    pyautogui.MINIMUM_SLEEP(2)
TypeError: 'float' object is not callable
>>> pyautogui.MINIMUM_SLEEP
0.05
>>> pyautogui.moverel(100,100,2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pyautogui.moverel(100,100,2)
AttributeError: module 'pyautogui' has no attribute 'moverel'
>>> pyautogui.movRel(100,100,2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    pyautogui.movRel(100,100,2)
AttributeError: module 'pyautogui' has no attribute 'movRel'
>>> pyautogui.moveRel(100,100,2)
>>> pyautogui.size()
Size(width=1920, height=1080)
>>> pyautogui.movRel(1920,1080,2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    pyautogui.movRel(1920,1080,2)
AttributeError: module 'pyautogui' has no attribute 'movRel'
>>> pyautogui.moveRel(1920,1080,2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    pyautogui.moveRel(1920,1080,2)
  File "C:\Users\sanju\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pyautogui\__init__.py", line 586, in wrapper
    returnVal = wrappedFunction(*args, **kwargs)
  File "C:\Users\sanju\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pyautogui\__init__.py", line 1301, in moveRel
    _mouseMoveDrag("move", None, None, xOffset, yOffset, duration, tween)
  File "C:\Users\sanju\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pyautogui\__init__.py", line 1487, in _mouseMoveDrag
    failSafeCheck()
  File "C:\Users\sanju\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pyautogui\__init__.py", line 1710, in failSafeCheck
    raise FailSafeException(
pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.
>>> clrscr()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    clrscr()
NameError: name 'clrscr' is not defined
>>> clearscreen
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    clearscreen
NameError: name 'clearscreen' is not defined
>>> clr()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    clr()
NameError: name 'clr' is not defined
>>> quit()
>>> import pyautogui
>>> pyautogui.position()
Point(x=948, y=542)
>>> pyautogui.click(948,542)
>>> pyautogui.click(948,542,5)
>>> pyautogui.position()
Point(x=1301, y=50)
>>> pyautogui.click(1301,50)
>>> pyautogui.click()
>>> pyautogui.position()
Point(x=104, y=321)
>>> pyautogui.dragRel(104,400,2)
>>> pyautogui.dragRel(104,400,2)
>>> pyautogui.dragRel(104,600,2)
>>> pyautogui.dragRel(600,104,2)
>>> pyautogui.dragRel(104,400,2)
>>> pyautogui.displayMousePosition()
Press Ctrl-C to quit.
X:  978 Y:  521 RGB: (167, 144, 182)
X:  905 Y:  380 RGB: (  0,   0,   0)
X: 1117 Y:  558 RGB: (255, 255, 255)
X:  729 Y:  726 RGB: (  0,   0,   0)
X: 1740 Y:  281 RGB: (255, 255, 255)
X: 1740 Y:  281 RGB: (255, 255, 255)
X: 1740 Y:  281 RGB: (255, 255, 255)
X: 1740 Y:  281 RGB: (255, 255, 255)
X: 1919 Y: 1075 RGB: ( 38,  38,  38)
X: 1919 Y: 1079 RGB: ( 87,  87,  87)
X: 1919 Y: 1079 RGB: ( 87,  87,  87)
X: 1919 Y: 1079 RGB: ( 87,  87,  87)
X: 1919 Y: 1079 RGB: ( 87,  87,  87)
X: 1919 Y:    0 RGB: ( 66,  66,  66)
X: 1919 Y:    0 RGB: ( 66,  66,  66)
X:    0 Y:   23 RGB: ( 44,  47,  51)
X:    0 Y:    0 RGB: ( 30,  33,  37)
X:    0 Y:  898 RGB: (154, 149, 150)
X:    0 Y: 1079 RGB: ( 57,  61,  63)
X:    0 Y: 1079 RGB: ( 53,  66,  72)
X:    0 Y: 1079 RGB: ( 53,  66,  72)
X: 1058 Y:  532 RGB: (255, 255, 255)
X:  958 Y:  539 RGB: (176, 176, 176)
X:  952 Y:  539 RGB: (194, 194, 194)
X:  952 Y:  539 RGB: (194, 194, 194)
X:  952 Y:  539 RGB: (194, 194, 194)
X:  946 Y:  529 RGB: (252, 252, 252)
X:  947 Y:  531 RGB: (251, 251, 251)
X:  947 Y:  531 RGB: (251, 251, 251)

>>> pyautogui.dragTo(104,400,2)
>>> pyautogui.dragRel(104,400,2)
>>> pyautogui.dragRel(104,400,2)
>>> pyautogui.dragTo(104,400,2)
>>>   0 RGB: ( 66,  66,  66)
X: 1919 Y:    0 RGB: ( 66,  66,  66)
X:    0 Y:   23 RGB: ( 44,  47,  51)
X:    0 Y:    0 RGB: ( 30,  33,  37)
SyntaxError: unexpected indent
>>> 
>>> pyautogui.click(100,100); pyautogui.dragTo(104,400,2)
>>> pyautogui.position()
Point(x=463, y=221)
>>> pyautogui.click(463,221);pyautogui.typewrite('hey sanju',0.2)
>>> pyautogui.click(463,221);pyautogui.typewrite('hey','left','right','right','sanjju',2)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    pyautogui.click(463,221);pyautogui.typewrite('hey','left','right','right','sanjju',2)
  File "C:\Users\sanju\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pyautogui\__init__.py", line 586, in wrapper
    returnVal = wrappedFunction(*args, **kwargs)
TypeError: typewrite() takes from 1 to 4 positional arguments but 6 were given
>>> pyautogui.click(463,221);pyautogui.typewrite(['hey','right','left','left','sanju'],1)
>>> pyautogui.click(463,221);pyautogui.typewrite(['ab','right','left','left','122'],1)
>>> pyautogui.hotkey('ctrl','a')
>>> pyautogui.screenshot()
<PIL.Image.Image image mode=RGB size=1920x1080 at 0x400EA00>
>>> pyautogui.screenshot('D:\\Pictures\\Screenshots\\example.png')
<PIL.Image.Image image mode=RGB size=1920x1080 at 0x400EA30>
>>> 