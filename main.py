from time import sleep
import emoji

seg = 10

for c in range(0, 10):
  
  print(seg)
  seg = seg - 1
  sleep(1)

print(emoji.emojize("feliz ano novo!!! \U0001f389\U0001f389\U0001f389"))