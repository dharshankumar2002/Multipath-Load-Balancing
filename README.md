# Multipath-Load-Balancing

Method of managing incoming traffic by distributing and sharing load fairly among multiple routes from source to destination hosts

<br>
<p align="left">
  <img src="./Topology Diagrams/topology_diagram1.png" width="500" alt="example network topology">
</p>


This network has 4 different paths available from host1 to host8. 
<pre>
Paths:
------
Path1 – {S1-S2-S4-S7}
Path2 – {S1-S2-S4-S6-S7}
Path3 – {S1-S2-S3-S4-S7}
Path4 – {S1-S2-S3-S4-S6-S7}
</pre>

Usually packets will be transferred from host1 to host8 using any one of these 4 paths. <br>
But in case of this algorithm, we will split the packets into any 2 paths to reduce the transfer time.
<br>
<hr style=\"border:0.5px solid gray\"> </hr>
<br>

## How to use this code?

Open a linux/Ubuntu terminal \
<a href="https://www.brianlinkletter.com/2014/12/how-to-install-mininet-sdn-network-simulator/">Install mininet</a>
<pre>
>> sudo apt-get install git
>> git clone git://github.com/mininet/mininet
>> git checkout -b 2.2.0b3
>> ~/mininet/util/install.sh -a
</pre>

<a href="https://www.howtoinstall.me/ubuntu/18-04/ryu-bin/">Install ryu controller</a>
<pre>
>> sudo apt install ryu-bin
</pre>
<br><br>

Open new command window & load your mininet model in it
<pre>
>> sudo mn --custom ex_simple.py --topo simple_topo --controller=remote
</pre>

Open another command window & start the ryu-controller in it \
Run ryu-controller using your ryu_multipath.py code
<pre>
>> ryu-manager --observe-links ryu_multipath.py
</pre>
<br>

Ping from one host to another host in mininet
<pre>
mininet> h1 ping h2 -c4
</pre>

Now, see check the packets entering input port & packets leaving output ports \
The no. of packets will be splited into 2 ports to balance load
<pre>
mininet> sh ovs-ofctl dump-ports s1
</pre>

<hr style=\"border:0.5px solid gray\"> </hr>
<br>

## How this code works?

Algorithm will
1. Find all possible path between source & destination hosts using DFS(Depth First Search)
2. Find 2 most optimal paths out of all the available paths
3. Install the corresponding flow entries from ryu controller to switch's group table using OpenFlow protocol

<hr style=\"border:0.5px solid gray\"> </hr>
<br>

## Examples: Other Network Topologies 

<p align="left">
  <img src="./Topology Diagrams/topology_diagram3.png" width="300" alt="example network topology">
  <img src="./Topology Diagrams/topology_diagram4.png" width="350" alt="example network topology">
  <img src="./Topology Diagrams/topology_diagram2.png" width="400" alt="example network topology">
</p>
