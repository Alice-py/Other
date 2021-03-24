# encoding=utf-8

import os
import re
import time


class ProtControl:
    def __init__(self, remote_ip, open_port=["8080", "443", "80"], limit_port=["9092", "514"]):
        # self.host = host
        # self.account = account
        # self.passwd = passwd
        self.open_port = open_port
        self.limit_port = limit_port
        self.remote_ip = remote_ip

    def cut_ip(self, host):
        """进行IP判断与切割，返回IP列表，如['192.168.200.185', '192.168.200.186']"""
        ips = list()
        hosts = host.split(";")
        ip_re = re.compile(
            "^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])."
            "(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)."
            "(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)."
            "(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])$")
        for ip in hosts:
            if re.match(ip_re, ip):
                ips.append(ip)
        return ips

    def confirm_status(self):
        print("=" * 100)
        # firewall-cmd --list-all|grep -E "ports|services|rule"|grep -v "forward-ports\|source-ports"
        res = os.popen(
            'firewall-cmd --list-all|grep -E "ports|services|rule"|grep -v "forward-ports\|source-ports"')  # 确认状态
        data = res.read()
        print("端口状态:\n", data)
        print("=" * 100)
        return data

    def change_port(self, data):
        # 开放any端口
        cmd = ""
        for port in self.open_port:
            cmd += "firewall-cmd --permanent --zone=public --add-port={}/tcp\n".format(port)
        output = os.popen(cmd)
        # print(output)

        for port in self.limit_port:
            if port in data:
                # 关闭无需any端口
                output = os.system(
                    "firewall-cmd --zone=public --remove-port={}/tcp --permanent >> /dev/null".format(port))
                print("检测到端口 {} 为打开状态  ——已关闭".format(port))
            # 放行指定IP端口
            remote_ip_list = self.cut_ip(self.remote_ip)
            for ip in remote_ip_list:
                os.system(
                    'firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="{0}" port protocol="tcp" port="{1}" accept" >> /dev/null'.format(
                        ip, port))
                if port == "514": os.system(
                    'firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="{0}" port protocol="udp" port="{1}" accept" >> /dev/null'.format(
                        ip, port))

            print("端口 {} 已打开并限制访问IP为 {}".format(port, self.remote_ip))
        os.popen("systemctl restart firewalld.service")
        time.sleep(3)

    def port_con_main(self):
        port_status = self.confirm_status()
        # print("端口状态:\n", port_status)
        self.change_port(port_status)
        port_status = self.confirm_status()
        # print("端口状态:\n", port_status)


if __name__ == '__main__':
    # remote_ip = "192.168.199.90"
    open_port = ["8080", "443", "80"]  # 放行所有的ip
    limit_port = ["9092", "514"]  # 放行部分的ip
    remote_ip = input("### 请输入接入事件需放行的IP，如需多个请用英文;切开\n### 例：1.1.1.1;2.2.2.2\n### > ")
    ProtControl(remote_ip=remote_ip, open_port=open_port, limit_port=limit_port).port_con_main()
