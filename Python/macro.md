0. pyautoGUI 모듈 설치

```cmd
pip install pyautugui
```

``` py
import pyautogui as pag
```

1. 마우스 명령

마우스 커서 위치 좌표 추출

```py
import pyautogui as pag

x, y = pag.position()
print(x, y) # x = ?, y = ?

pos = pag.position()
print(pos) # Point(x=?, y=?)
```

마우스 위치 이동

``` py
import pyautogui as pag

pag.moveTo(0, 0) # 픽셀 단위 절대 좌표 기준 이동
pag.moveRel(1, 0) # 픽셀 단위 상대 좌표 기준 이동
```

마우스 클릭

``` py
import pyautogui as pag

pag.click() # 현재 위치 클릭
pag.click((100, 100))
pag.click(x = 100, y = 100) # 특정 픽셀 위치 클릭

pag.rightClick()  # 우클릭
pag.doubleClick() # 더블 클릭
```

마우스 드래그

``` py
import pyautogui as pag

pag.dragTo(x = 100, y = 100, duration = 2) # 현재 커서 위치에서 x, y 위치까지 dration 동안 드래그
```

2. 키보드 명령

글자 타이핑

``` py
import pyautogui as pag

pag.typewrite('ABC') # 글자 입력
pag.typewrite('ABC', interval = 1) # interval 만큼 천천히 입력
```

글자가 아닌 다른 키보드 키 누르기

``` py
import pyautogui as pag

pag.press('enter')

""" 누를수 있는 키 목록
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
"""
```

보조키 누른 상태 유지 + 떼기 (ctrl, alt, shift)

``` py
import pyautogui as pag

pag.keyDown('shift') # shift 누르고 누른 상태 유지
pag.kdyUp('shift') # shift 떼기
```

단축키 사용

``` py
import pyautogui as pag

pag.hotkey('ctrl', 'c') # ctrl + c
pag.hotkey('alt', 'f4') # alt + f4
```