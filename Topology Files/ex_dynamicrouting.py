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
        u = self.addSwitch('s1')
        v = self.addSwitch('s2')
        x = self.addSwitch('s3')
        y = self.addSwitch('s4')
        w = self.addSwitch('s5')
        z = self.addSwitch('s6')
        
        # Add links
        self.addLink( h1, u )
        self.addLink( u, v )
        self.addLink( u, x )
        self.addLink( u, w )
        self.addLink( v, w )
        self.addLink( v, x )
        self.addLink( x, w )
        self.addLink( x, y )
        self.addLink( y, w )
        self.addLink( y, z )
        self.addLink( z, w )
        self.addLink( z, h2 )

topos = { 'dynamic_topo': ( lambda: MyTopo() ) }

















