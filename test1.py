import time
 
        
from Motor import *            
PWM=Motor()          


from Ultrasonic import *
ultrasonic=Ultrasonic()                

try:
   while True:
       data=ultrasonic.get_distance()   #Get the value
       print ("Obstacle distance is "+str(data)+"CM")
       if(data<10):
           PWM.setMotorModel(-1000,-1000,-1000,-1000)   #Back
           print ("The car is going backwards")  
           time.sleep(1)
        else:
           PWM.setMotorModel(1000,1000,1000,1000)       #Forward
           print ("The car is moving forward")
           time.sleep(1)
                
except KeyboardInterrupt:
    print ("\nEnd of program")
