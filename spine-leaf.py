from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class SpineLeafTopology(Topo):
   "Spine Leaf topology with m spine switches, n leaf switches and o hosts, with one host per leaf"

   def __init__(self, mSpines=2, nLeaf=3, hHost=2,  **opts):
       """Init.
           mSpines: number of spine switches
           nLeaf: number of leaf switches
           hHosts: number of hosts per leaf switch
       """
       super(SpineLeafTopology, self).__init__(**opts)

       spines={}
       leaf={}
       h=1
       # Add mSpines
       for i in irange(1, mSpines):
           spines[i] = self.addSwitch('spine%s' % (i))
       # Add nLeaf
       for i in irange(1, nLeaf):
           leaf[i] = self.addSwitch('leaf%s' % (i))
       # Connect Leaf to every Spine
       for i in irange(1,len(spines)):
           for j in irange(1,len(leaf)):
              self.addLink('leaf%s' % (j), 'spine%s' % (i))
       #Add Hosts and Connect Hosts to Leafs
       for i in irange(1, nLeaf):
        for ho in irange(1,(hHost)):
         name=('host%s' % (h))
         h=h+1
         self.addHost('%s'% (name))
         self.addLink('%s'%(name),'leaf%s' % (i))

def simpleTest():
   "Create and test a simple network"
   topo = SpineLeafTopology(mSpines=2, nLeaf=1, hHost=4)
   net = Mininet(topo)
   net.start()
   print "Dumping host connections"
   dumpNodeConnections(net.hosts)
   print "Testing network connectivity"

if __name__ == '__main__':
   # Tell mininet to print useful information
   setLogLevel('info')
   simpleTest()
