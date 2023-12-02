from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
C = 21
CSHARP = 20
D = 16
DSHARP = 26
E = 19
F = 13
FSHARP = 6
G = 5
GSHARP = 11
A = 17
ASHARP = 8
B = 25


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(CSHARP, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(DSHARP, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(FSHARP, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(GSHARP, GPIO.OUT)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(ASHARP, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)


@app.route("/redled_on", methods=["POST"])
def led_on_r_red():
     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(1)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)

     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(1)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)

     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(G, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(G, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(C, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(C, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(D, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(D, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(2)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)

     GPIO.output(F, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(F, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(F, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(F, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(F, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(F, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(F, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(F, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(F, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(F, GPIO.LOW)
     time.sleep(0.5)

     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)

     GPIO.output(D, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(D, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(D, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(D, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(E, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(E, GPIO.LOW)
     time.sleep(0.5)

     GPIO.output(D, GPIO.HIGH)
     time.sleep(1)
     GPIO.output(D, GPIO.LOW)
     time.sleep(0.5)
     GPIO.output(G, GPIO.HIGH)
     time.sleep(1)
     GPIO.output(G, GPIO.LOW)
     time.sleep(0.5)
     return "ok"

@app.route("/redled_off", methods=["POST"])
def led_off_r_red():
    GPIO.output(C, GPIO.LOW)
    return "ok"

@app.route("/yellowled_on", methods=["POST"])
def led_on_r_yellow():
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(F, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(F, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(E, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(E, GPIO.LOW)
    time.sleep(1)

    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(G, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(G, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(F, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(F, GPIO.LOW)
    time.sleep(1)

    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(A, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(A, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(G, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(G, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(F, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(F, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(E, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(E, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(GSHARP, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GSHARP, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(GSHARP, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GSHARP, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(G, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(G, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(DSHARP, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(DSHARP, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(F, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(F, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(DSHARP, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(DSHARP, GPIO.LOW)
    time.sleep(0.5)
    return "ok"

@app.route("/yellowled_off", methods=["POST"])
def led_off_r_yellow():
    GPIO.output(CSHARP, GPIO.LOW)
    return "ok"

@app.route("/led_on", methods=["POST"])
def led_on():
    GPIO.output(E, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(E, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(E, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(E, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(C, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(E, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(E, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(D, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(C, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(C, GPIO.LOW)
    return "ok"

@app.route("/led_off", methods=["POST"])
def led_off():
    GPIO.output(CSHARP, GPIO.LOW)
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="Ashley Kulcsar")