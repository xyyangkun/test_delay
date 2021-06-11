#!/usr/bin/python3
#--coding:utf8----

# server 接收分组数据，返回结果，让客户端计算延时
import socket
import binascii
import struct

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
# create udp server
def create_udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    return s

def recv_data(s):
    data,addr = s.recvfrom(2024)
    #print("recv addr:",  addr, "recv data len:", len(data),  "data:",data)
    _len = struct.unpack("I", data[0:4])

    #print("recv data len:", _len[0])

    # 返回的是tuple类型
    _end = _len[0] + 4
    # 截取数据
    _buf = data[4:_end]
    # 组成 "7s" 这样的字符串
    format = str(_len[0])+"s"
    _str = struct.unpack(format, _buf)
    
    return addr
    # 接收的数据是tuple, 将其中的byte使用decode转为字符串, 自动删除末尾的0
    #print("type:", type(_str[0]), "recv str:", _str[0].decode())


if __name__=='__main__':
    s = create_udp_server()
    count = 0
    addr =''
    while True:
        count += 1
        addr = recv_data(s)
        #print("count = ", count)
        if count == 200:
        #if count == 1: 
            break

    #接收100次返回数据
    s.sendto("abc".encode(), addr)


    s.close()



