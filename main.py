from gpio_read import opi_gpio
from print_bmp import label_printing
from canopen_tool import canopen_tool

import time
import datetime
import os

dev_dictionaries = {
    "2309": "ALLCAN-S",
    "2310": "ALLCAN-Q",
    "2313": "BFLS",
    "2318": "ALLCAN-4",
    "2319": "ALLCAN-ENC",
    "2324": "ALLCAN-CMP"
}

bitrate_decide = False

can_net = canopen_tool()

def callback():
    if not bitrate_decide:
        os.system(f"./find_node.sh")
        bitrate_decide = True

    can_net.connect_can_init()
    nodes = can_net.find_node()
    if nodes:
        can_net.add_node(nodes[0])
        dev = can_net.read_unit_type()
        if not dev: return False
        lss = can_net.read_sn()
        if not lss: return False
    else:
        print("find node error")
        return -1

    for k, v in dev_dictionaries.items():
        if k in str(dev):
            msg = f"{dev_dictionaries[k]}/{lss[1]}/{datetime.date.today()}/{lss[0]}.{lss[1]}.{lss[2]}.{lss[3]}"
            label_printing.printing(msg, dev_dictionaries[k], lss[3], datetime.date.today())
            return True
    return False

if __name__ == "__main__":
    opi_gpio.gpio_init(12)
    opi_gpio.read_button_init(12)
    opi_gpio.gpio_init(16)
    opi_gpio.out_init(16)

    while True:
        val = opi_gpio.read_button(12, 1, callback)
        
        if val == None:
            pass
        elif val:
            opi_gpio.light_led(16)
        else:
            opi_gpio.blink_led(16)
        time.sleep(0.1)
        