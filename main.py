import time   #importing time module
from plyer import notification  # importing plyer module for Desktop notification

if __name__=="__main__":
        while True:
            notification.notify(
                title="Hey Please Drink WATER!",
                message="The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men,About 11.5 cups (2.7 liters) of fluids a day for women",
                app_icon="C:\\Users\\SCI\\OneDrive\\Desktop\\Gaurav Joshi Codes\\PY proj\\Drink Water Reminder\\icon.ico",
                timeout=5  #Time till the notification exists on the screen
            )
            time.sleep(10)
