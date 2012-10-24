#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import socket
import sys

# $hostname 
# host = "students.ami.nstu.ru"
host = "localhost"
port = 20002
 
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
try:
    s.connect( ( host, port ) )
except:
    print 'error: server doesn\'t exists'
    sys.exit(1)

while  True:
    buf = ''
    while len(buf) == 0:
        buf = raw_input( "\nenter some command, please:\n>> " )

    if buf == 'exit':
        print 'client dies...'
        s.send( buf )
        result = s.recv( 1024 )
        print result
        break
s.close()
