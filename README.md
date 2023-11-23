# swPLC
swPLC is a software PLC developed in [node-red](https://nodered.org/) with a light and clean dashboard to monitor the PLC status and the memory registers set via Modbus TCP.

![swPLC dashboard](https://github.com/br1pro/swPLC/blob/main/Pictures/swPLC_dashboard.png)

# How it works
swPLC can be programmed via modbusTCP, it listen for ModbusTCP commands on port TCP502 (it can be customized in node-red configuration). 
The swPLC has four Holding registers (address from 0 to 3) that can be set with integer values (0–65535) and five Coil Registers that can be set with 0 or 1 bits values.
More Registers can be added if needed.

# Dashboard
The dashboard shows the registers current value:
- Coil Registers are showed on left side of the dashboard, each register value is showed (1/0)
- Holding Registers are showed in the middle of the dashboard, each register value is showed with a gauge chart (gauge values can be customized)


