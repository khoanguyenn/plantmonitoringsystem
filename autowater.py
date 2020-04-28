//auto_water
# External module import
import datetime
import time
import main
init = False
def get_last_watered():
 try:
 f = open("storage/last_watered.txt", "r")
 return f.readline()
 except:
 return "NEVER!"

def auto_water(delay = 2):
 print("Press CTRL+C to exit")
 try:
 while True:
 print("Entered the loop")
 time.sleep(delay)
 main.sendAndReceive('Led Off')
 main.sendAndReceive('Pump Off')
 storeLastWatered()
 dry = int(main.sendAndReceive('Moisture')) == 0 #True if dry
 print(dry)
 if dry:
 pump_on()
 except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
 main.sendAndReceive('Stop')
def pump_on(delay = 1):
 main.sendAndReceive('Led On')
 main.sendAndReceive('Pump On')
 storeLastWatered()
 time.sleep(delay)
def storeLastWatered():
 f = open("storage/last_watered.txt", "w")
 now = datetime.datetime.now()
 dateString = now.strftime("%A, %d %B %Y %X")
 f.write("Last watered: {}".format(dateString))
 f.close()
