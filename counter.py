import gpio
import time

# Cleans the mode of each individual GPIO pin
def cleanup(bit):
	print("Cleaning bit setup:")
	for i in range(0,len(bit)):
		gpio.cleanup(bit[i]) 
	print("Cleanup done")

# GPIO Setup for each individual GPIO pin
def setup(bit, num_bits):
	print("Initializing setup:") 
	if len(bit) == num_bits:
		for i in range(0,num_bits):
			gpio.setup(bit[i], gpio.OUT) # Bit vector as OUTPUT
	else:
		print("Error : Non consisten counter length with number of bits")
		exit(-1)
	print("Setup done")

# GPIO Setup verification
def verify(bit):
	print("Verifying output initialization:")
	for i in range(0,num_bits):
		if gpio.mode(bit[i]) == "out":
			continue
		else:
			print("Pin {0} was not initialized as output".format(bit[i]))
			cleanup(bit[0:i])
			exit(-1)
	print("Verification succeed")

# Sending value through the bit vector 
def send_bits(bit, value, num_bits):
	#write_bits = [0]*num_bits
	for i in range(0, num_bits):
		gpio.set(bit[i],int(value[i]))
		#write_bits[i] = int(value[i]) 
	#print(write_bits)

# Reading sent value through the bit vector 
def read_bits(bit, num_bits):
	read_bits = [0]*num_bits
	for i in range(0, num_bits): 
		read_bits[i] = gpio.read(bit[i])
	print(read_bits[::-1]) # Inverse for readability ONLY for Debugging! 

# Using Vitiral's gpio library (Access by Linux sysfs on L4T for Nvidia Jetson TX2)
num_bits = 8

# GPIO Declaration
# Expansion Header J21: 11, 13, 15, 19, 21, 23, 29, 31
#       LSB -----------------------------> MSB 
bits = [466, 397, 255, 429, 428, 427, 398, 298] 

# Initialize setup
setup(bits, num_bits)

# Verify correct initialization
verify(bits)

# Conversion to 2's Complement
datum = 0 + 2**num_bits

# Count and send 
print("Sending: ")
#while True:
for i in range(0,2**num_bits):	
	send_bits(bits, bin(datum)[::-1], num_bits)
	datum += 1
	time.sleep(0.00)
		#read_bits(bits, num_bits)
cleanup(bits)
