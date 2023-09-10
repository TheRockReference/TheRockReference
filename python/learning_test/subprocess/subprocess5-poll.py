
#******************IN PROGRESS ****************************

import time
import subprocess

p = subprocess.Popen("sleep 10", shell=True)
# Better: p = subprocess.Popen(["sleep", "30"])

i = 0
# Wait until process terminates
while p.poll() is None:
    print(i)
    time.sleep(0.5)
    i = i + 1

# It's done
print("Process ended, ret code:", p.returncode)