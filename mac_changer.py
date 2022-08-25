import subprocess
import optparse

def get_input():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help= "enter your interface in -i")
    parser.add_option("-m", "--mac", dest= "address", help="enter your desired mac here")
    return parser.parse_args()



def change_mac(interface, address):
    subprocess.call(["ifconfig", interface , "down"])
    subprocess.call(["ifconfig", interface , "hw", "ether" , address])
    subprocess.call(["ifconfig", interface , "up"])

(interface,address)= get_input()
change_mac(interface,address)
