#!/usr/bin/python

import os
import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSSwitch, RemoteController

print("Using Python:", sys.executable)


class MyTopo(Topo):
    "Ring topology with 4 switches and 4 hosts."

    def __init__(self):
        # Init topo
        Topo.__init__(self)

        # Adding Switches to the topology
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")
        s4 = self.addSwitch("s4")

        # Adding Hosts to the topology
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        h3 = self.addHost("h3")
        h4 = self.addHost("h4")

        # Adding Links between Switches
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s1)

        # Adding Links between Switches and Hosts
        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)
        self.addLink(s4, h4)


if __name__ == "__main__":
    os.system("sudo mn -c")

    setLogLevel("info")
    topo = MyTopo()

    # Create controller object and start the controller
    controller = RemoteController('c0', ip='127.0.0.1', port=6633)

    # Start Mininet
    net = Mininet(
        topo=topo,
        link=TCLink,
        controller=controller,
        switch=OVSSwitch,
    )
    net.start()

    net.get('s1').cmd('ovs-vsctl set Bridge s1 protocols=OpenFlow13')
    net.get('s2').cmd('ovs-vsctl set Bridge s2 protocols=OpenFlow13')
    net.get('s3').cmd('ovs-vsctl set Bridge s3 protocols=OpenFlow13')
    net.get('s4').cmd('ovs-vsctl set Bridge s4 protocols=OpenFlow13')

    # Set the controller for the switches
    net.get('s1').cmd('ovs-vsctl set-controller s1 tcp:127.0.0.1:6633')
    net.get('s2').cmd('ovs-vsctl set-controller s2 tcp:127.0.0.1:6633')
    net.get('s3').cmd('ovs-vsctl set-controller s3 tcp:127.0.0.1:6633')
    net.get('s4').cmd('ovs-vsctl set-controller s4 tcp:127.0.0.1:6633')

    # Start the CLI
    CLI(net)

    # Stop Mininet
    net.stop()
