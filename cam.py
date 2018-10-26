import os
i=1
while(i<=5):
    os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/pramodh/"+str(i)+".jpg")
    i=i+1
    print("pic taken")
