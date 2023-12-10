#!/usr/bin/python

import os, sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from mininet.node import Host, RemoteController

class TreeTopo( Topo ):
    "Tree topology"

    def build( self ):
        # Read ring.in
        # Load configuration of Hosts, Switches, and Links
        # You can write other functions as you need.

        # Add hosts
        # > self.addHost('h%d' % [HOST NUMBER])

        # Add switches
        # > sconfig = {'dpid': "%016x" % [SWITCH NUMBER]}
        # > self.addSwitch('s%d' % [SWITCH NUMBER], **sconfig)

        # Add links
        # > self.addLink([HOST1], [HOST2])
		with open("ring.in", "r") as source_file:
			N, M, L = map(int, source_file.readline().split())
            # according to star.in, there are 8 hosts, 5 switches and 12 links

			# add hosts:
	    		for i in range(1, N + 1):
				hostId = "h{}".format(i)
				self.addHost(hostId)

			# add switches:
	    		for i in range(1, M + 1):
				switchId = "s{}".format(i)
				sconfig = {"dpid": "{:016x}".format(i)}
				self.addSwitch(switchId, **sconfig)
		
			# add links:
	    		for _ in range(L):
				link = source_file.readline().strip()
				node1, node2 = link.split(",")
				self.addLink(node1, node2)
        
                    
topos = { 'sdnip' : ( lambda: TreeTopo() ) }

if __name__ == '__main__':
    sys.path.insert(1, '/home/sdn/onos/topos')
    from onosnet import run
    run( TreeTopo() )