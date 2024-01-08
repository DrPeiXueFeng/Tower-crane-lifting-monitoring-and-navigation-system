from machine import Pin
import time
import network
import socket
import json

"""
echo脚会由0变为1此时MCU开始计时，当超声波模块接收到返回的声波时，echo由1变为0此时MCU停止计时
然后再通过声音的传输速度是340m/s就可以计算出距离，切记要除以2，毕竟声音是来回的距离
"""
global t1
global t2


def do_connect():
    """链接WIFI"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('TZJC', 'Tz@080414JC')
        i = 1
        while not wlan.isconnected():
            print("正在链接...{}".format(i))
            i += 1
            time.sleep(1)
    print('network config:', wlan.ifconfig())  # 路由器分配的ip地址，子网掩码，默认网关，DNS


def measure():
    # 告诉芯片要开始测试了
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # 检测回响信号，为低电平时，测距完成
    while echo.value() == 0:
        # 开始不断递增的微秒计数器 1
        t1 = time.ticks_us()
    print("---------------------")
    print(t1)
    # 检测回响信号，为高电平时，测距开始
    while echo.value() == 1:
        # 开始不断递增的微秒计数器 2
        t2 = time.ticks_us()

    # 计算两次调用 ticks_ms(), ticks_us(), 或 ticks_cpu()之间的时间，这里是ticks_us()
    # 这时间差就是测距总时间，在乘声音的传播速度340米/秒，除2就是距离
    # 例如 t2-t1=12848此时单位是us，转换为秒就是12848 / 1000000 此时单位是秒，此时如果乘以340计算出的单位是米，
    # 然后再乘以100就是厘米，因此，直接 用12848/10000即可
    t3 = time.ticks_diff(t2, t1) / 10000
    print(t3, t2 - t1)

    # 这里返回的是：开始测距的时间减测距完成的时间*声音的速度/2（来回）
    return t3 * 340 / 2


def measure1():
    # 告诉芯片要开始测试了
    trig1.value(1)
    time.sleep_us(10)
    trig1.value(0)

    # 检测回响信号，为低电平时，测距完成
    while echo1.value() == 0:
        # 开始不断递增的微秒计数器 1
        t1 = time.ticks_us()
    print("---------------------")
    print(t1)
    # 检测回响信号，为高电平时，测距开始
    while echo1.value() == 1:
        # 开始不断递增的微秒计数器 2
        t4 = time.ticks_us()

    # 计算两次调用 ticks_ms(), ticks_us(), 或 ticks_cpu()之间的时间，这里是ticks_us()
    # 这时间差就是测距总时间，在乘声音的传播速度340米/秒，除2就是距离
    # 例如 t2-t1=12848此时单位是us，转换为秒就是12848 / 1000000 此时单位是秒，此时如果乘以340计算出的单位是米，
    # 然后再乘以100就是厘米，因此，直接 用12848/10000即可
    t3 = time.ticks_diff(t4, t1) / 10000
    print(t3, t4 - t1)

    # 这里返回的是：开始测距的时间减测距完成的时间*声音的速度/2（来回）
    return t3 * 340 / 2


def measure2():
    # 告诉芯片要开始测试了
    trig2.value(1)
    time.sleep_us(10)
    trig2.value(0)

    # 检测回响信号，为低电平时，测距完成
    while echo2.value() == 0:
        # 开始不断递增的微秒计数器 1
        t1 = time.ticks_us()
    print("---------------------")
    print(t1)
    # 检测回响信号，为高电平时，测距开始
    while echo2.value() == 1:
        # 开始不断递增的微秒计数器 2
        t5 = time.ticks_us()

    # 计算两次调用 ticks_ms(), ticks_us(), 或 ticks_cpu()之间的时间，这里是ticks_us()
    # 这时间差就是测距总时间，在乘声音的传播速度340米/秒，除2就是距离
    # 例如 t2-t1=12848此时单位是us，转换为秒就是12848 / 1000000 此时单位是秒，此时如果乘以340计算出的单位是米，
    # 然后再乘以100就是厘米，因此，直接 用12848/10000即可
    t3 = time.ticks_diff(t5, t1) / 10000
    print(t3, t5 - t1)

    # 这里返回的是：开始测距的时间减测距完成的时间*声音的速度/2（来回）
    return t3 * 340 / 2


def measure3():
    # 告诉芯片要开始测试了
    trig3.value(1)
    time.sleep_us(10)
    trig3.value(0)

    # 检测回响信号，为低电平时，测距完成
    while echo3.value() == 0:
        # 开始不断递增的微秒计数器 1
        t1 = time.ticks_us()
    print("---------------------")
    print(t1)
    # 检测回响信号，为高电平时，测距开始
    while echo3.value() == 1:
        # 开始不断递增的微秒计数器 2
        t6 = time.ticks_us()

    # 计算两次调用 ticks_ms(), ticks_us(), 或 ticks_cpu()之间的时间，这里是ticks_us()
    # 这时间差就是测距总时间，在乘声音的传播速度340米/秒，除2就是距离
    # 例如 t2-t1=12848此时单位是us，转换为秒就是12848 / 1000000 此时单位是秒，此时如果乘以340计算出的单位是米，
    # 然后再乘以100就是厘米，因此，直接 用12848/10000即可
    t3 = time.ticks_diff(t6, t1) / 10000
    print(t3, t6 - t1)

    # 这里返回的是：开始测距的时间减测距完成的时间*声音的速度/2（来回）
    return t3 * 340 / 2


# 引脚设定
trig = Pin(15, Pin.OUT)
echo = Pin(2, Pin.IN)
trig.value(0)
echo.value(0)
trig1 = Pin(4, Pin.OUT)
echo1 = Pin(16, Pin.IN)
trig1.value(0)
echo1.value(0)

trig2 = Pin(17, Pin.OUT)
echo2 = Pin(5, Pin.IN)
trig2.value(0)
echo2.value(0)
trig3 = Pin(18, Pin.OUT)
echo3 = Pin(19, Pin.IN)
trig3.value(0)
echo3.value(0)


# try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理
def main():
    do_connect()
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_addr = ('192.168.16.244', 8081)
    # 绑定本地信息
    udp_socket.bind(("0.0.0.0", 7780))
    while True:
        try:
            while True:
                a = [round(measure(), 1), round(measure1(), 1), round(measure2(), 1), round(measure3(), 1)]
                print(a)
                send_data = json.dumps(a)
                udp_socket.sendto(bytes(send_data.encode('utf-8')), dest_addr)
                time.sleep(1)

        except NameError:
            pass
        continue

    udp_socket.close()


if __name__ == "__main__":
    main()



