#!/usr/bin/venv python
# -*- coding:utf-8 -*-

import socket, time, thread
socket.setdefaulttimeout(3)

def socket_port(ip, port):
    """
    input ip and port
    """
    try:
        if port >= 65535:
            print "finish scanning ports"
        s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result =  s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            print ip, u":", port, u"port is in use"
            lock.release()
    except:
        print u"Exception occurs during scanning"

def ip_scan(ip, port=None):
    """
    input ip, scan ip from 0 to 65534 port
    """
    try:
        print u"Starting scanning %s" % ip
        start_time = time.time()
        if port:
            thread.start_new_thread(socket_port, (ip, int(port)))
        else:
            for i in xrange(0, 65534):
                thread.start_new_thread(socket_port, (ip, int(i)))
        print u"Scan completed, time: %.2f" %(time.time() - start_time)
    except:
        print u"Error during scanning"


if __name__ == "__main__":
    url = raw_input("Input ip you want to scan: ")
    if not url:
        url = "127.0.0.1"
    port = raw_input("Input port you want to scan: ")
    ip = url
    if ":" in url:
        ip = url.split(":")[0]
        port = url.split(":")[-1]
    lock = thread.allocate_lock()
    ip_scan(ip, port)
