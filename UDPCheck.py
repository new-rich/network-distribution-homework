import struct

numlist=[0x6660,0x5555,0x8f0c]

def UDPCheck(list):
    sum=0
    for i in range(0,len(list)):
        sum+=list[i]
        sum = (sum >> 16) + (sum & 0xffff)
        print("UDP校验中间结果为", '{:016b}'.format(sum))
    udp_check=0xffff-sum&0xffff
    print("UDP校验和为",'{:016b}'.format(udp_check))
    sum+=udp_check
    sum = (sum >> 16) + (sum & 0xffff)
    print("UDP校验结果为",'{:016b}'.format(sum))
    return sum==0xffff

if UDPCheck(numlist):
    print("校验成功")
else:
    print("校验失败")
