#!/usr/bin/python

import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.node import OVSSwitch, RemoteController


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        centerSwitch = self.addSwitch('s1', dpid='0000000000000001')
        for i in range(6):
            host = self.addHost('h%s' % (i + 1))
            self.addLink(host, centerSwitch, bw=10)


if __name__ == '__main__':
    os.system("sudo mn -c")

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

    # Set the OpenFlow version for the switch
    net.get('s1').cmd('ovs-vsctl set Bridge s1 protocols=OpenFlow13')

    # Set the controller for the switch
    net.get('s1').cmd('ovs-vsctl set-controller s1 tcp:127.0.0.1:6633')

    # Start the CLI
    CLI(net)

    # Stop Mininet
    net.stop()
