//website
from flask import Flask, render_template, redirect, url_for
import psutil
import datetime
import water
import main
import os
app = Flask(__name__)
def template(title = "Plant monitoring system", text = ""):
 now = datetime.datetime.now()
 dateString = now.strftime("%A, %d %B %Y")
 timeString = now.strftime("%X")
 templateDate = {
 'title' : title,
 'time' : timeString,
 'date' : dateString,
 'text' : text
 }
 return templateDate
@app.route("/")
def hello():
 templateData = template(text = "Welcome, Khoa")
 return render_template('main.html', **templateData)
@app.route("/last_watered")
def check_last_watered():
 templateData = template(text = water.get_last_watered())
 return render_template('main.html', **templateData)
@app.route("/sensor")
def action():
 status = int(main.sendAndReceive('Moisture'))
 message = ""
 if (status == 0):
 message = "Water me please!"
 else:
 message = "I'm a happy plant"
 templateData = template(text = message)
 return render_template('main.html', **templateData)
@app.route("/wateron")
def action2():
 water.pump_on()
 print('Pump on')
 templateData = template(text = "Watering...")
 return render_template('main.html', **templateData)
@app.route("/wateroff")
def action3():
 main.sendAndReceive("Pump Off")
 main.sendAndReceive("Led Off")
 print('Pump off')
 templateData = template(text = "Turned OFF")
D-1
 return render_template('main.html', **templateData)
@app.route("/auto/water/<toggle>")
def auto_water(toggle):
 running = False
 if toggle == "ON":
 templateData = template(text = "Auto Watering ON")
 for process in psutil.process_iter():
 try:
 if process.cmdline()[1] == 'auto_water.py':
 templateData = template(text = "Already running")
running = True
 except:
 pass
 if not running:
 os.system("python auto_water.py")
 else:
 templateData = template(text = "Auto Watering OFF")
 os.system("pkill -f water.py")
 main.sendAndReceive("Pump Off")
 return render_template('main.html', **templateData)
if __name__ == "__main__":
 app.run(host='0.0.0.0', port=8000, debug=True)