import winsound
import time

print('Heads up: Your device is veing infected!')
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
for i in range(20):
  time.sleep(1)
  for j in range(i):
    winsound.Beep(frequency, duration)

print('Message recieved  from kernel: Hahaha, that was fun!')
