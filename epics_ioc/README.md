# RF-AMP-RPIInterface EPICS IOC
The RPI provides with the Python based local UI as well a network based remote control interface. The files in this folder provide a EPICS IOC configuration example which are meant to run within a EPICS softIOC environment.


Before starting, it is required to adapt the RPI hostname in the `startup.script`, also make sure the RPI is in the same network as the PC where you start the iocsh.


To run the local test IOC call: `iocsh startup.script`