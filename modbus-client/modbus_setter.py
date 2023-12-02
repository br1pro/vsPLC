"""
Modbus Registry Setter

Description:
    Script to set Modbus registry values.

Author :
	mguyard (https://github.com/mguyard)
Based on the work of :
	br1pro (https://github.com/br1pro)

License:
    This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""


import time
import datetime
import argparse
import random
from ipaddress import ip_address
from pymodbus.constants import Defaults
from pymodbus.client import ModbusTcpClient
import atexit
import signal
import sys

# The class `ConsoleColors` defines constants for different colors that can be used in the console
# output.
class ConsoleColors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'

def print_colored(message, color):
	"""
	The function `print_colored` prints a message in the specified color.
	
	:param message: The message parameter is a string that represents the text that you want to print in
	color
	:param color: The "color" parameter is a string that represents the color you want to use for
	printing the message
	"""
	print(f"{color}{message}{ConsoleColors.RESET}")

# Parsing Arguments
parser = argparse.ArgumentParser(
		prog="Modbus Registry Setter",
		description="Script to set Modbus registry",
		epilog="As simple as that !"
)
parser.add_argument("-i", "--ip", type=ip_address, help="Modbus IP Address", required=True)
parser.add_argument("-r", "--registry", type=int, help="Registry number", required=True)
args = parser.parse_args()



print(" ---- {} - Script Init for registry {} ---- ".format(datetime.datetime.now(), args.registry)) 
time.sleep(0.5)
#Defaults.Timeout = 1
#Defaults.Retries = 1
client = ModbusTcpClient(str(args.ip), timeout=1, retries=1)
client.connect()
time.sleep(0.5)
print(" ---- {} - Connected to Modbus Slave for registry {} ----".format(datetime.datetime.now(), args.registry)) 

read_result=client.read_holding_registers(args.registry,1,1) #add,count,unit
read_value=read_result.registers[int(0)] 
print("{} Reading holding register {} value = {}".format(datetime.datetime.now(), args.registry, read_value))
# The code `write_value=0` initializes the variable `write_value` with a value of 0.
write_value=0
# The line `write_value=random.randint(1,10)` generates a random integer between 1 and 10 and assigns
# it to the variable `write_value`. This random value will be used to write to the Modbus holding
# register specified by the `args.registry` argument.
write_value=random.randint(1,10)
while(True):
	print("{} Writing holding register {} value = {}   --------->  ".format(datetime.datetime.now(), args.registry, write_value), end = " ")
	client.write_register(args.registry,write_value,1)
	read_result=client.read_holding_registers(args.registry,1,1) #add,count,unit
	read_value=read_result.registers[int(0)] 
	print("{} Reading holding register {} value = {}".format(datetime.datetime.now(), args.registry, read_value), end = " ")
	# Checking if the value written to the Modbus holding register (`write_value`) is different from
	# the value read from the same register (`read_value`).
	if (write_value != read_value):
		print_colored("   ---------> Last write HR{} was blocked!".format(args.registry), ConsoleColors.RED)
	else:
		print()
	
	time.sleep(1)
	# The line `write_value=random.randint(1,20)` generates a random integer between 1 and 20 and assigns
	# it to the variable `write_value`. This random value will be used to write to the Modbus holding
	# register specified by the `args.registry` argument.
	write_value=random.randint(1,20)