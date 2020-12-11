import time  #time module
from plyer import notification  #A module which helps us in bringing up the notifications

if  __name__ == "__main__":
    while(True):
        notification.notify(
            title = "Please Drink Water!!!",
            message = "A Glass of water every hour is MUST!!!",
            app_icon = "C:/Users/vamsi rajan/pythonpro/DrinkWaterRemainder/glass.ico",  
            #Cannot directly place C:\Users\vamsi rajan\pythonpro\project1
            timeout = 10
        )
        time.sleep(60*60)  #Notifies us after every hour
