import serial
import subprocess

arduino = serial.Serial('COM4', 9600, timeout=1)

while True:
    line = arduino.readline().decode('utf-8').strip()

    if line:
        print("Arduino:", line)

    if line in ["fire", "knock", "default"]:
        print(f"Executing Python script with event: {line}")
        subprocess.run(["python", "request.py", line])
