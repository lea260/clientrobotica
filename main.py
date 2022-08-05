#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!
from pybricks.hubs import EV3Brick
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait, StopWatch

ev3 = EV3Brick()
ev3.speaker.beep(3000, 0.5)
# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

#print('establishing connection...')
client.connect(SERVER)
#print('connected!')
ev3.screen.print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.
mbox.send('hello!')
mbox.wait()
#print(mbox.read())
ev3.screen.print(mbox.read())
wait(2000)