# virtual simple PLC
vsPLC is a software PLC developed in [node-red](https://nodered.org/) with a light and clean dashboard to monitor the PLC status and the memory registers set via Modbus TCP.
The vsPLC purpouse is to have a virtual ModbusTCP PLC that can be used in lab to simulate a real PLC.

![swPLC dashboard](https://github.com/br1pro/swPLC/blob/main/Pictures/swPLC_dashboard.png)

# How it works
vsPLC can be programmed via ModbusTCP, it listen for ModbusTCP commands on port TCP/502 (it can be customized in node-red configuration). 
The vsPLC has four Holding Registers (address from 0 to 3) that can be set with integer values (0–255) and five Coil Registers that can be set with 0 or 1 bits values.
Device ID is set to 1. More Registers can be added if needed.

# Dashboard
The dashboard shows the registers current values:
- Coil Registers are showed on left side of the dashboard, each register value is showed (1/0).
- Holding Registers are showed in the middle of the dashboard, each register value is showed with a gauge chart (gauge values can be customized), for each register a historic chart is showed with values registered in the last minute.

# Installation istructions
## Pre-requesites
Node-red need to be installed on the target machine, the following modules need to be installed before importing the vsPLC flow:
- node-red-contrib-modbus
- node-red-contrib-buffer-parser
- node-red-node-random
- node-red-dashboard
  
The procedure to import node-red modules can be find [here](https://nodered.org/docs/user-guide/editor/palette/manager). You can use palette manager to install all the modules. Is suggested to run node-red as a service and to start on boot.
## Installation
Import the vsPLC flow json configuration into node-red, follow node-red instructions [here](https://nodered.org/docs/user-guide/editor/workspace/import-export)

## Docker version
Build the vsplc image and call it "vsplc" in your running docker environment using the following command:
- `docker build https://github.com/br1pro/vsplc.git#:docker -t vsplc`

Run the docker image using the following command:
- `docker run --rm -p 1880:1880 -p 502:502 --name vsPLC vsplc`

Kudos to [mguyard](https://github.com/mguyard) for the support 🙂

# Operation
One the json flow is deployed and started vsPLC is ready to run.
To open the vsPC dashboard open in a browser the page `http://your_machine_ip:1880/ui` (port 1880 is the node-red standard port). 
Https can be enabled in your node-red installation, reference [here](https://nodered.org/docs/user-guide/runtime/securing-node-red).


