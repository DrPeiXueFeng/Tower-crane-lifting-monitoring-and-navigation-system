from machine import Pin
import network
import socket
import time
import json

def do_connect():
    """链接WIFI"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('1215', 'Tz@080414JC')
        i = 1
        while not wlan.isconnected():
            print("正在链接...{}".format(i))
            i += 1
            time.sleep(1)
    print('network config:', wlan.ifconfig())#路由器分配的ip地址，子网掩码，默认网关，DNS

def main():
    # 链接wifi
    do_connect()
    # 创建UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(("0.0.0.0", 7788))
    while True:
        dest_addr = ('192.168.3.9', 8080)
        a1 = Pin(13, Pin.IN)
        a2 = Pin(12, Pin.IN)
        a3 = Pin(27, Pin.IN)
        a4 = Pin(26, Pin.IN)
        a5 = Pin(25, Pin.IN)
        a6 = Pin(33, Pin.IN)
        a7 = Pin(32, Pin.IN)
        a8 = Pin(35, Pin.IN)
        a9 = Pin(23, Pin.IN)
        a10 = Pin(2, Pin.IN)
        a11 = Pin(4, Pin.IN)
        a12 = Pin(18, Pin.IN)
        a13 = Pin(19, Pin.IN)
        count = 0
        a = [a1.value(), a2.value(), a3.value(), a4.value(), a5.value(), a6.value(), a7.value(), a8.value(), a9.value(), a10.value(), a11.value(), a12.value(), a13.value()]
        time.sleep(0.01)
        b = [a1.value(), a2.value(), a3.value(), a4.value(), a5.value(), a6.value(), a7.value(), a8.value(), a9.value(), a10.value(), a11.value(), a12.value(), a13.value()]
        if b != a:
            for i in range(100):
                c = [a1.value(), a2.value(), a3.value(), a4.value(), a5.value(), a6.value(), a7.value(), a8.value(), a9.value(), a10.value(), a11.value(), a12.value(), a13.value()]
                if c == b:
                    time.sleep(0.001)
                    continue
                if c != b:
                    a = c
                    b = [a1.value(), a2.value(), a3.value(), a4.value(), a5.value(), a6.value(), a7.value(), a8.value(), a9.value(), a10.value(), a11.value(), a12.value(), a13.value()]
                    break#过滤快速闪动不稳定的传感器数值（数据预处理）
            send_data = json.dumps(b)
            udp_socket.sendto(bytes(send_data.encode('utf-8')), dest_addr)
        if b == a:
            continue
            
    udp_socket.close()
    

if __name__ == "__main__":
    main()


