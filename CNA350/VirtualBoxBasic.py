#This script starts a linux VM, updates, upgrades, clones and prints the IP address to the console
#CNA 350,fall 19
#parker Swift,pdswift@student.rtc.edu

#starts a VM
import virtualbox
import time
vbox = virtualbox.VirtualBox()
print("VM(s):\n + %s" % "\n + ".join([vm.name for vm in vbox.machines]))

vm = vbox.find_machine('UBUNTU NET')
vm.launch_vm_process()
session = vm.create_session()
time.sleep(30)

vm = vbox.find_machine('UBUNTU ALTERNETIVE')
vm.launch_vm_process()
session = vm.create_session()
time.sleep(30)

vm = vbox.find_machine('LB')
vm.launch_vm_process()
session = vm.create_session()
time.sleep(30)

vm = vbox.find_machine('WS01')
vm.launch_vm_process()
session = vm.create_session()
time.sleep(30)

vm = vbox.find_machine('WS02')
vm.launch_vm_process()
session = vm.create_session()
time.sleep(30)

#session.console.keyboard.put_keys('pswift')
#session.UBUNTUNET.keyboard.put_keys(['ENTER'])


#time.sleep(0.5)
#session.console.keyboard.put_keys('pswift')
#session.console.keyboard.put_keys(['ENTER'])

time.sleep(35)

session.console.power_down(),