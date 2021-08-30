import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep 
from PIL import Image
from bot_response import response


paperclip = Image.open(r'C:\Users\User\Desktop\DI_Bootcamp\Week7\Day3\WhatsApp_Bot\paperclip.jpeg') 
green_dot= Image.open(r'C:\Users\User\Desktop\DI_Bootcamp\Week7\Day3\WhatsApp_Bot\greendot.png')

xlose = Image.open(r'C:\Users\User\Desktop\DI_Bootcamp\Week7\Day3\WhatsApp_Bot\x.png')


# Mouseclicker
mouse = Controller()

# Instructions for the Bot
class WhatsApp:
    # Define Starting values 
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # Navigate to the geen dots for new message
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen(green_dot, confidence=.6)
            pt.moveTo(position[0:2], duration = self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)

        except Exception as e:
            print('Exception (nav_green_dot): ', e)
    
    # Navigate to the input box( need cursor to move weay from the paperclip overf to the input box)
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen(paperclip, confidence=.6)
            pt.moveTo(position[0:2], duration = self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)


        except Exception as e:
            print('Exception (nav_input_box): ', e)
        
    # Navigate to the message we want to respond to
    def nav_message(self):
        try:
            position = pt.locateOnScreen(paperclip, confidence=.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(30, -60, duration=self.speed)
        except Exception as e:
            print('Exception (nav_message): ', e)
    
    #Copies the message we are going to process 
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(10, 10, duration=self.speed)
        mouse.click(Button.left,1)
        sleep(1)

        # pastes the message we copied
        self.message = pc.paste()
        print('User says: ', self.message)
        
    # CLose response box
    def nav_x(self):
        try:
            position = pt.locateOnScreen(xlose, confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 10, duration=self.speed)  # x,y has to be adjusted depending on your computer
            mouse.click(Button.left, 2)
        except Exception as e:
            print('Exception (nav_x): ', e)

    def send_message(self):
        try:
            # Checks whether the last message was the same
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('You say: ', bot_response)
                pt.typewrite(bot_response, interval=.1)
                # send the message disbale while testing
                pt.typewrite('\n')
              # Assigns the same message
                self.last_message = self.message
            else: 
                print('No new messages')
        
        except Exception as e:
            print('Exception (send_message): ', e)

# Initialises the bot 
run_bot = WhatsApp(speed=.5, click_speed=.4)
run_bot.nav_green_dot()
run_bot.nav_message()
run_bot.get_message()
run_bot.nav_input_box()
run_bot.send_message()
sleep(2)






# Run the programme in a loop

    # Delay between checking for new messages

