**GL**
=====================

Script for monitoring system resources - cpu or  virtual and swap memory.
***
**Dependencies**
=====================

python3.6<br/>
psutil<br/>
sys<br/>

**Installation**
=====================

git clone https://github.com/iavorskiy/GL.git<br/>
pip3 install psutil

**Examples**
=====================

$ ./gl.py cpu<br/>
system.cpu.user 8476.52<br/>
system.cpu.nice 106.97<br/>
system.cpu.system 5972.0<br/>
system.cpu.idle 100915.69<br/>
system.cpu.iowait 899.21<br/>
system.cpu.irq 0.0<br/>
system.cpu.softirq 12.28<br/>
system.cpu.steal 0.0<br/>
system.cpu.guest 0.0<br/>
system.cpu.guest_nice 0.0<br/>


$ ./gl.py mem<br/>
virtual total 8136495104<br/>
virtual available 3613605888<br/>
virtual percent 55.6<br/>
virtual used 4166733824<br/>
virtual free 1948213248<br/>
virtual active 2444750848<br/>
virtual inactive 2447810560<br/>
virtual buffers 4235264<br/>
virtual cached 2017312768<br/>
virtual shared 39825408<br/>
virtual slab 518299648<br/>
swap total 8321495040<br/>
swap used 208670720<br/>
swap free 8112824320<br/>
swap percent 2.5<br/>
swap sin 7917568<br/>
swap sout 208629760<br/>

**Docker**
=====================


**Build image**
-----------------------------------
For run a script as a docker container you need to build image from Docker file.

git clone https://github.com/iavorskiy/GL.git<br/>
cd GL<br/>
docker build -t GL .<br/>

**Run**
-----------------------------------

docker run --pid=host --volume /:/host  metrics mem<br/>
docker run --pid=host --volume /:/host  metrics cpu<br/>


