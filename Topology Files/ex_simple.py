"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dictS with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "ring topology example."
    def build( self ):
        "Create custom topo."
        
        # Add hosts
	h1 = self.addHost('h1')
	h2 = self.addHost('h2')

	#Add switches
	s1 = self.addSwitch('s1')
	s2 = self.addSwitch('s2')
	s3 = self.addSwitch('s3')
	s4 = self.addSwitch('s4')
	s5 = self.addSwitch('s5')

	# Add links
	self.addLink( h1, s1 )
	self.addLink( s1, s2 )
	self.addLink( s1, s3 )
	self.addLink( s3, s5)
	self.addLink( s5, s4 )
	self.addLink( s1,s2 )
	self.addLink( s2, s4 )
	self.addLink( s4, h2 )

topos = { 'simple_topo': ( lambda: MyTopo() ) }
















