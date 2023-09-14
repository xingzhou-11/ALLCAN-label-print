import time
import canopen
import threading

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class canopen_tool:
    def __init__(self):
        self.network = None

    def connit_can(self, status):
        try:
            self.network = canopen.Network()
            self.network.connect(channel='can0', bustype='socketcan')
            status[0] = False
        except Exception as e:
            print(e)

    def connit_can_init(self):
        if self.network != None: return False
        status = [True]
        t1 = StoppableThread(target=self.connit_can, args=([status,]))
        t1.start()
        time_out = time.time() + 5
        while t1.is_alive():
            if time.time() > time_out: t1.stop()
            time.sleep(0.2)

        if status[0]: self.network = None
        return status[0]
    
    def find_node(self):
        try:
            self.network.scanner.reset()
            self.network.scanner.search()
        except Exception as e:
            print(e)
            return False

        time.sleep(1)
        return self.network.scanner.nodes

    def add_node(self, node_id):
        self.node = self.network.add_node(node_id, 'objdict.eds')
     
    def read_sn(self):
        try:
            vendorId_hex = self.node.sdo[0x1018][1].data[::-1].hex()
            productCode_hex = self.node.sdo[0x1018][2].data[::-1].hex()
            revisionVersion_hex = self.node.sdo[0x1018][3].data[::-1].hex()
            serialNumber_hex = self.node.sdo[0x1018][4].data[::-1].hex()

            ret = [vendorId_hex, productCode_hex, revisionVersion_hex, serialNumber_hex]
            return ret
        except Exception as e:
            print(e)
            return False

    def read_unit_type(self):
        try:
            return self.node.sdo[0x1009].data
        except Exception as e:
            print(e)
            return False

    def disconnect(self):
        self.network.disconnect()

if __name__ == "__main__":
    can_net = canopen_tool()
    can_net.connit_can_init()
    nodes = can_net.find_node()
    if nodes:
        can_net.add_node(nodes[0])
        print(can_net.read_unit_type()) 

