import schedule
import time
import pywhatkit
import keyboard

def func():
    
    pywhatkit.sendwhatmsg_to_group_instantly("whatsapp_code" , "your message!") 
    time.sleep(3)
    keyboard.press_and_release('ctrl+w')
    
  
schedule.every(1).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(1)
