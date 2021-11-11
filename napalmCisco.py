from napalm1 import get_network_driver
import json


#list ip
listip = [
    '1.1.1.1',
    '2.2.2.2'
]


for ipAddress in listip:
    
    print('list ip is'+str(ipaddress))
    devices = get_network_driver('ios')
    conects = devices(ipAddress, 'admin', 'cisco')
    conects.open()
    
    output = conects.get_interfaces()
    print(json.dumps(output, sort_keys=True, indent=4))
   
    output.close()
