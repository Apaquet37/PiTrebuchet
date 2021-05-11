from flask import Flask, render_template, request

from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo,Device
from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = Servo(18)
servo2 = Servo(21)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
		servo.max()
		servo2.max()
		sleep(1)
		msg = request.form.get("submitBtn")
	else:
		servo.min()
		servo2.min()
		msg = "No click yet."
	return render_template("index.html", msg=msg)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)

