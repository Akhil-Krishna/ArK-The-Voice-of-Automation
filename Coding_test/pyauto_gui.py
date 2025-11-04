import pyautogui as py

import pyautogui
sw,sh=py.size()
print(sw,sh)
import time
time.sleep(2)


py.moveTo(500, 500, duration=3, tween=pyautogui.easeOutElastic) 



# print(pyautogui.KEY_NAMES)
# print(pyautogui.alert('This is the message to display.'))

# print(pyautogui.alert('This displays some text with an OK button.'))
# print(pyautogui.confirm('This displays text and has an OK and Cancel button.'))

# print(pyautogui.prompt('This lets the user type in a string and press OK.'))



#pyautogui.screenshot('foo.png')
#py.screenshot()

#print(py.password(text='text', title='title', default='ak', mask='*'))