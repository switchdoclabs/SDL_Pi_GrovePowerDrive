#
#
# SDL_Pi_GrovePowerDrive example
# Raspberry Pi Driver for the SwitchDoc Labs GrovePowerDrive 
#
# SwitchDoc Labs
# April  2017
#
# Version 1.1

# assumes device is plugged into GPIO Pin 4/5 (D4/D5 of Pi2Grover board)

import  SDL_Pi_GrovePowerDrive
import time

GPIO_Pin_PowerDrive_Sig1 = 4
GPIO_Pin_PowerDrive_Sig2 = 5


myPowerDrive = SDL_Pi_GrovePowerDrive.SDL_Pi_GrovePowerDrive(GPIO_Pin_PowerDrive_Sig1, GPIO_Pin_PowerDrive_Sig2, True, True)
	
print "turning Pin %i off" % GPIO_Pin_PowerDrive_Sig1
myPowerDrive.turnOffPowerDrive(1)

time.sleep(60)

myPowerDrive.turnOffPowerDrive(2)

print "turning Pin %i off" % GPIO_Pin_PowerDrive_Sig2

time.sleep(60)

print "turning Pin %i on" % GPIO_Pin_PowerDrive_Sig1
myPowerDrive.turnOffPowerDrive(1)

print "turning Pin %i off" % GPIO_Pin_PowerDrive_Sig2
myPowerDrive.turnOffPowerDrive(2)



		
