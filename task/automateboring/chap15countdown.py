import time
import subprocess


timeLeft = 60

while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft -1

subprocess.Popen(['start', '/drip.mp3'], shell=True)
