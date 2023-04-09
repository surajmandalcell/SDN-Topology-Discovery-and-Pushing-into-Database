#!/usr/bin/python


"""Custom topology example

RING Topology(Loop),

Switch1-----Switch2------Switch3-----Switch4-----Switch1


Switch1-----Host1
Switch2-----Host2
Switch3-----Host3
Switch4-----Host4

MAC,IP, Controller, CLI stuff configured

# run RYU SDN STP Application for this topology

ryu-manager ryu.app.simple_switch_stp

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."

    def build(self):
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
    setLogLevel("info")
    topo = SingleSwitchTopo()
    c1 = RemoteController("c1", ip="127.0.0.1")
    net = Mininet(topo=topo, controller=c1, switch=OVSSwitch, autoSetMacs=True)
    net.start()
    # run RYU SDN STP Application for this topology
    net.get("s1").cmd("ovs-vsctl set bridge s1 stp_enable=true")
    net.get("s2").cmd("ovs-vsctl set bridge s2 stp_enable=true")
    net.get("s3").cmd("ovs-vsctl set bridge s3 stp_enable=true")
    net.get("s4").cmd("ovs-vsctl set bridge s4 stp_enable=true")

    CLI(net)
    net.stop()
