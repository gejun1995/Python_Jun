import urllib.request
import re
import datetime
import random


def get_proxy_ip_list():
    url = 'http://cn-proxy.com/'
    user_agent_list = [
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
        "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    ]
    user_agent = random.choice(user_agent_list)
    header = {'User-Agent': user_agent}
    req = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(url=req)
    html = response.read().decode('utf-8')
    proxy_ip_list = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', html)
    full_proxy_ip_list = []
    for proxy_ip in proxy_ip_list:
        position = int(html.index(proxy_ip))
        length = len(proxy_ip)
        port_position = position + length
        port = re.findall(r'\d{2,5}', html[port_position:(port_position + 25)])
        full_ip = proxy_ip + ':' + port[0]
        full_proxy_ip_list.append(full_ip)
    print(full_proxy_ip_list)
    filename = 'proxy_ip_list-' + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
    with open(filename, 'w') as f:
        for proxy_ip in full_proxy_ip_list:
            f.write(proxy_ip)
            f.write('\n')


if __name__ == '__main__':
    get_proxy_ip_list()
