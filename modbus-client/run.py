"""
Runner Modbus Registry Setter

Description:
    Script to Run Modbus Registry Setter script.

Author :
	mguyard (https://github.com/mguyard)

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

import argparse
from ipaddress import ip_address
import os
import subprocess
import atexit

parser = argparse.ArgumentParser(
		prog="Modbus Demo",
		description="Script to set random values in multiple registry (0-3)",
		epilog="As simple as that !"
)
# This code block is checking if the environment variable `MODBUS_PLC` is set. If it is not set, it
# adds a required command-line argument `-i` or `--ip` to the parser, which expects an IP address as
# its value. If `MODBUS_PLC` is set, it adds the same command-line argument but with a default value
# of `os.environ.get('MODBUS_PLC')` (the value of the environment variable) and sets `required=False`,
# meaning the argument is optional.
if os.environ.get('MODBUS_PLC', None) == None:
    parser.add_argument("-i", "--ip", type=ip_address, help="Modbus IP Address", required=True)
else:
    parser.add_argument("-i", "--ip", type=ip_address, help="Modbus IP Address", default=os.environ.get('MODBUS_PLC'), required=False)
args = parser.parse_args()

# The `params_list` is a list of dictionaries that contains the parameters for running the
# `modbus_setter.py` script. Each dictionary in the list represents a set of parameters for one
# instance of the script.
params_list = [
    {'ip': str(args.ip), 'registry': 0},
    {'ip': str(args.ip), 'registry': 1},
    {'ip': str(args.ip), 'registry': 2},
    {'ip': str(args.ip), 'registry': 3},
]

# Runs each script in the background
processes = []
for params in params_list:
    command = ['python3', 'modbus_setter.py', f"--ip={params['ip']}", f"--registry={params['registry']}"]
    processes.append(subprocess.Popen(command))

# Function to be executed when exiting the main script
def cleanup():
    print("Stop main script. Stop child scripts.")
    for process in processes:
        process.terminate()

# Registers the cleanup function to be executed on exit
atexit.register(cleanup)

try:
    input("Press Enter to stop the script...\n\n\n")

except KeyboardInterrupt:
    # Intercepts manual interrupt (Ctrl+C) and calls the cleanup function
    cleanup()
