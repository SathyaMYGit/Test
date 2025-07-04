import pyautogui
import time
import webbrowser

'''print("Move your mouse to Compose button in 5 seconds...")
time.sleep(5)
print(pyautogui.position())//135, y=229'''



# Open Gmail in browser
webbrowser.open("https://mail.google.com/")
time.sleep(10)  # Wait for Gmail to load

# Click on "Compose" button
pyautogui.moveTo(135, 229)  # You need to update this value
pyautogui.click()
time.sleep(3)

# Type recipient email
pyautogui.write('mail2digitalachievers@gmail.com', interval=0.1)
pyautogui.press('tab')  # Go to Subject
pyautogui.press('tab')  # Go to subject field

# Type subject
pyautogui.write('Project is Submitted', interval=0.1)
pyautogui.press('tab')  # Go to body

# Type body message
pyautogui.write('Hi,\n\nI have submitted the project.\n\nThanks,\nSathya Priya', interval=0.1)
time.sleep(1)

# Press Ctrl + Enter to send
pyautogui.hotkey('ctrl', 'enter')
