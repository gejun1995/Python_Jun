import os
import random
import re
import urllib.error
import urllib.request


def make_folder(folder_name):
    folder_name = folder_name
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    os.chdir(folder_name)


def get_full_proxy_ip_list(proxy_ip_url, user_agent_list):
    user_agent = random.choice(user_agent_list)
    header = {'User-Agent': user_agent}
    req = urllib.request.Request(url=proxy_ip_url, headers=header)
    try:
        response = urllib.request.urlopen(url=req)
    except urllib.error.HTTPError as e:
        print("get_proxy_ip_list: " + str(e))
        get_full_proxy_ip_list()
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
        print("get proxy ip: " + full_ip)
    return full_proxy_ip_list


def open_url(url):
    # random proxy ip
    # proxy = random.choice(full_proxy_ip_list)
    # proxy_support = urllib.request.ProxyHandler({'http': proxy})
    # opener = urllib.request.build_opener(proxy_support)
    # rllib.request.install_opener(opener)
    # random user agent
    user_agent = random.choice(user_agent_list)
    header = {'User-Agent': user_agent}
    req = urllib.request.Request(url=url, headers=header)
    try:
        response = urllib.request.urlopen(url=req)
    except urllib.error.HTTPError as e:
        print("open_url: " + str(e))
        open_url()
    html = response.read()
    return html


def get_img_addrs_list(url):
    html = open_url(url).decode('utf-8')
    print("get img address html")
    print(html)
    # pattern = r'data-actualsrc="(.*?)">'
    pattern = r'https:[\w./-]*.jpg'
    img_re = re.compile(pattern, re.S)
    img_addrs_list = img_re.findall(html)
    print("img address:")
    print(img_addrs_list)
    return img_addrs_list

def get_ans_addrs_list(url):
    html = open_url(url).decode('utf-8')
    print("get ans address html")
    print(html)
    #pattern = r'https:[\w./-]*/answer/\d*'
    pattern = r'https://www.zhihu.com/question/267707433/answer/\d*'
    ans_re = re.compile(pattern, re.S)
    ans_addrs_list = ans_re.findall(html)
    print("answer address:")
    print(ans_addrs_list)
    return ans_addrs_list

def download_zhihu_imgs(url):
    make_folder(folder_name='zhihu_imgs_downloads')
    ans_addrs_list = get_ans_addrs_list(url)
    img_url_list=[]
    for ans_url in ans_addrs_list:
        img_addrs_list = get_img_addrs_list(ans_url)
        for img_url in img_addrs_list:
            img_url_list.append(img_url)
    print("img_url_list")
    print(img_url_list)
    filename = 1
    for img_url in img_url_list:
        img = open_url(img_url)
        filename += 1
        with open(str(filename) + ".jpg", 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    url = "https://www.zhihu.com/question/267707433"
    # proxy_ip_url = 'http://cn-proxy.com/'
    user_agent_list = [
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
        "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    ]
    # full_proxy_ip_list = get_full_proxy_ip_list(proxy_ip_url=proxy_ip_url, user_agent_list=user_agent_list)

    download_zhihu_imgs(url)
