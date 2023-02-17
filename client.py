#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        if not data:
                break
        subprocess.call(data, shell=True)
conn.close()