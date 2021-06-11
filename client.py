#!/usr/bin/python3
#--coding:utf8----

import socket
import binascii
import struct
import time

HOST = '172.20.2.3'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
send_addr=(HOST, PORT)
# create udp server
def create_udp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s

def send_data(s):
    _buf = ''
    # 长度1400 
    _buf_len = 1400
    _buf += binascii.b2a_hex(struct.pack("I", _buf_len)).decode()

    # 创建发送buffer, 将自负床放到byte中，byte长度一定
    _str_buf="abcd1234".encode()
    print("type:", type(_str_buf))
    # 分配内存
    _send_data = bytearray(_buf_len)

    print("len:", len(_str_buf))
    # 这样复制会保留字符串后面没有使用的0 .总长400后面没有占用完，会有很多0
    _send_data[:len(_str_buf)] = _str_buf

    hex_send_buf   = binascii.b2a_hex(_send_data).decode()

    # 如果要删除后面的的0，可以直接这样操作
    #hex_send_buf   = binascii.b2a_hex(_str_buf).decode()


    # 拼接结构：4字节长度 + 数据
    _buf += hex_send_buf

    # 将hex类型的数据转换为bin类型
    bin_buf = binascii.a2b_hex(_buf)
    
    # 发送数据
    s.sendto(bin_buf, send_addr)


if __name__=='__main__':
    s = create_udp_client()
    start = time.time()
    # 1400*200
    #for i in range(0, 200):
    for i in range(0, 1):
        print("send ", i, "times")
        send_data(s)


    # 接收server返回数据
    data,addr = s.recvfrom(1024)
    end = time.time()
    print("time past:", end - start)
    print("client addr:", addr, " recv data:", data)

    s.close()

