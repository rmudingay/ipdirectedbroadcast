# ipdirectedbroadcast

ipdirectedbroadcast is a Python script that will help simulate EPICS v3 channel access protocol ip directed broadcast. It is a tool that can be used to stress test a network, especially one with ip directed broadcast enabled.

Install

```
# Clone the git repo
git clone https://github.com/rmudingay/ipdirectedbroadcast

# Install python dependancies
pip install os-sys
pip install sockets
pip install multiprocessing

# change director and edit the file
cd ipdirectedbroadcast

```

bcAddress = broadcast_addr                    # L3 directed broadcasts addresses
bcPort    = 5064                              # udp destination port to use
bcCount   = 10000000                          # how many datagrams shall we send
bcRate    = 14                                # Herz (Rate)
bcSize    = 48                                # bytes (payload for udp segment)

```
# run the command as follows and substitute BROADCAST_ADDR with the example destination address 1.2.3.255
python ipdirectedbroadcast BROADCAST_ADDR
```
