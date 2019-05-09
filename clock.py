import gpio
import time

# Using Vitiral's gpio library (Access by Linux sysfs on L4T for Nvidia Jetson TX2)

# GPIO Declaration
bit0 = 388 #Pin 396: Pin 7 in Expansion Header J21

# GPIO Setup 
gpio.setup(bit0, gpio.OUT) #Pin 396: Pin 7 in Expansion Header J21 as OUTPUT

while True:
	value = gpio.read(bit0)
	if value:
		gpio.set(bit0, 0)
	else:
		gpio.set(bit0, 1)
	time.sleep(0.0)

