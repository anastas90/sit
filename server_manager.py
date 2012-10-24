#!/usr/bin/env python
# -*- coding: utf-8 -*-

# подключаем модуль для работы с сокетами
import socket
import threading
import sys

# хост, на котором будем ждать
# host = "students.ami.nstu.ru"
host = "localhost"
# сервер, на котором будем слушать
port_chat = 20001    # для сервер-чата
port      = 20002    # для сервер-менеджера

class Connect( threading.Thread ):
    def __init__( self, sock, addr ):
        self.sock = sock
        self.addr = addr
        threading.Thread.__init__( self )

    def run( self ):
        while True:
            buf = self.sock.recv( 1024 ) 
            print ' >> incoming : ' + buf

            if buf == 'exit':
                print 'server dies...'
                self.sock.send( "server answers:\n>> connection is closing.." )
                break
            else:
                buf += ' ( length : %s )' % str( len( buf.decode( 'utf-8' ) ) )
                self.sock.send( "server answers:\n>> " + buf )
                print ' << outgoing : ' + buf
             
        self.sock.close( )

# создаём сокет
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# устанавливаем опцию повторного использования порта, 
# чтобы не ждать пока он освободится после останова сервера
s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

# ассоциируем сокет с хостом и портом
s.bind( ( host, port ) )

# указываем количество ожидающих обработки запросов
s.listen( 1 )

# функция accept() переводит приложение в ожидание
# подключения клиента. При успешном коннекте accept
# возвратит кортеж (пару) из объекта соединения и 
# адреса клиента. Полученный объект мы и будем использовать 
# для взаимодействия с клиентом.

while True:
    #try:
        print 'waiting for the connection...'
        sock, addr = s.accept( )
        print 'connected with : ', addr
        Connect( sock, addr ).start()
       
        buf = s.recv( 1024 ) 
        #print ' >> incoming : ' + buf

        if buf == 'exit':
            print 'server dies...'
            s.send( "server answers:\n>> connection is closing.." )
            break
        s.close( )

    #except:
        print 'server catched an exception and dies...'
        sys.exit()

            