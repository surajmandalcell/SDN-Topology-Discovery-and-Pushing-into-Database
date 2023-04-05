#!/usr/bin/python


"""Simple VLAN topology example

Linear Topology,

Switch1-----Switch2

Switch1-----a1, a2, b1, b2
Switch2-----a3, a4 ,b3, b4

objective:
1. a1,a2,a3,a4, belongs to VLAN 100
2. b1, b2, b3, b4 belongs to VLAN 200

Switch1 to Switch2 connected with 802.1Q TRUNK Links

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController
from time import sleep


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        a1 = self.addHost('a1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        a2 = self.addHost('a2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        a3 = self.addHost('a3', mac="00:00:00:00:00:03", ip="192.168.1.3/24")
        a4 = self.addHost('a4', mac="00:00:00:00:00:04", ip="192.168.1.4/24")

        b1 = self.addHost('b1', mac="00:00:00:00:00:11", ip="192.168.1.11/24")
        b2 = self.addHost('b2', mac="00:00:00:00:00:12", ip="192.168.1.12/24")
        b3 = self.addHost('b3', mac="00:00:00:00:00:13", ip="192.168.1.13/24")
        b4 = self.addHost('b4', mac="00:00:00:00:00:14", ip="192.168.1.14/24")


        #addlink(hostname,switchname,hostport,switchport)
        self.addLink(a1, s1, 1, 1)
        self.addLink(a2, s1, 1, 2)
        self.addLink(a3, s2, 1, 1)
        self.addLink(a4, s2, 1, 2)

        self.addLink(b1, s1, 1, 3)
        self.addLink(b2, s1, 1, 4)
        self.addLink(b3, s2, 1, 3)
        self.addLink(b4, s2, 1, 4)

        self.addLink(s1, s2, 5, 5)



if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    CLI(net)
    net.stop()
