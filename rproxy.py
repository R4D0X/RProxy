import os
from colorama import Fore, init, Style
import requests
import re
import platform
import time
import threading
from proxy_checker import ProxyChecker
from sys import stdout
from concurrent.futures import ThreadPoolExecutor, as_completed


lock = threading.Lock()
defs,sett = 1 - 1, 1 + 3
class UI:
    @staticmethod
    def menu():
        menu = f'''
                            █▀▀█ █▀▀█ █▀▀▄ █▀▀█ █░█
                            █▄▄▀ █▄▄█ █░░█ █░░█ ▄▀▄
                            ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀     {Fore.CYAN}https://t.me/radoxin
           
           {Fore.RED}[{Fore.YELLOW}1{Fore.RED}]{Style.RESET_ALL} Collect HTTP Proxy    {Fore.RED}[{Fore.YELLOW}2{Fore.RED}]{Style.RESET_ALL} SOCKS4-SOCKS5 Collect Proxy  
            
                            {Fore.RED}[{Fore.YELLOW}3{Fore.RED}]{Style.RESET_ALL} Check Proxies
        '''
        return menu
mdb = 'D'
def write(arg):
    with lock:
        stdout.flush()
        print(arg)

class ProxyChecker:
    def check_proxy(self, proxy):
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',  
        }
        try:
            response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=1)  
            return response.status_code == 200
        except requests.RequestException as e:
            write(f'{Fore.RED}[-] {Style.RESET_ALL}Proxy check error: {e}')
            return False
xer = f'{Fore.RED}Made By'
x = f'{Fore.MAGENTA}'
class XProxy:
    proxy_w_regex = [
        ["http://spys.me/proxy.txt", "%ip%:%port% "],
        ["http://www.httptunnel.ge/ProxyListForFree.aspx", ' target="_new">%ip%:%port%</a>'],
        ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
        ['http://free-fresh-proxy-daily.blogspot.com/feeds/posts/default', "%ip%:%port%"],
        ['http://www.proxyserverlist24.top/feeds/posts/default', "%ip%:%port%"],
        ['http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http',"%ip%:%port%"],
        ['http://proxysearcher.sourceforge.net/Proxy%20List.php?type=socks', "%ip%:%port%"], 
        ['https://www.my-proxy.com/free-anonymous-proxy.html', '%ip%:%port%'],
        ['https://www.my-proxy.com/free-transparent-.html', '%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list.html','%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-2.html','%ip%:%port%'],
        ['https://free-proxy-list.net/', '%ip%:%port%'],
        ['https://www.us-proxy.org/', '%ip%:%port%'],
        ['https://www.proxy-list.download/HTTP', '%ip%:%port%'],
        ['https://www.proxy-list.download/HTTPS', '%ip%:%port%'],
        ['https://hidemy.name/en/proxy-list/', '%ip%:%port%'],
        ['https://www.proxy-list.org/en/', '%ip%:%port%'],
        ['https://www.proxynova.com/proxy-server-list/', '%ip%:%port%'],
        ['https://www.proxy-list.biz/', '%ip%:%port%'],
        ['https://www.webshare.io/', '%ip%:%port%'],
        ['https://free-proxy-list.net/uk-proxy.html', '%ip%:%port%'],
        ['https://www.proxynova.com/proxy-server-list/country-us/', '%ip%:%port%'],
        ['https://free-proxy-list.net/anonymous-proxy.html', '%ip%:%port%'],
        ['https://www.proxynova.com/proxy-server-list/country-br/', '%ip%:%port%'],
        ['https://www.proxynova.com/proxy-server-list/country-cn/', '%ip%:%port%'],
        ['https://www.proxynova.com/proxy-server-list/country-ru/', '%ip%:%port%'],
        ['https://www.proxygather.com/', '%ip%:%port%'],
        ['https://www.proxy-listen.de/azenv.php', '%ip%:%port%'],
        ['https://www.freeproxylists.net/', '%ip%:%port%'],
        ['https://proxy-list.org/english/index.php', '%ip%:%port%'],
        ['https://www.proxy-list.org/', '%ip%:%port%'],
        ['https://www.proxy4free.com/', '%ip%:%port%'],
        ['https://www.proxybazaar.com/', '%ip%:%port%'],
        ['https://www.proxyrack.com/', '%ip%:%port%'],
        ['https://www.proxy-list.download/', '%ip%:%port%'],
        ['https://proxylist.me/', '%ip%:%port%'],
        ['https://www.us-proxy.org/', '%ip%:%port%'],
        ['https://free-proxy-list.net/', '%ip%:%port%'],
        ['https://www.proxynova.com/proxy-server-list/country-fr/', '%ip%:%port%'],
        ['https://www.proxynova.com/proxy-server-list/country-de/', '%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-3.html','%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-4.html', '%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-5.html','%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-6.html','%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-7.html','%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-8.html','%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-9.html','%ip%:%port%'],
        ['https://www.my-proxy.com/free-proxy-list-10.html','%ip%:%port%'],
        ['https://spys.one/en/free-proxy-list/', '%ip%:%port%'],
        ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all','%ip%:%port%']
        
    ]

    socks_proxy_list = [
        ['https://www.socks-proxy.net/', "%ip%:%port%"],
        ['http://www.socks24.org/feeds/posts/default', "%ip%:%port%"],
        ['https://www.freeproxychecker.com/result/socks4_proxies.txt', "%ip%:%port%"],
        ['https://www.my-proxy.com/free-socks-4-proxy.html', '%ip%:%port%'],
        ['https://www.my-proxy.com/free-socks-5-proxy.html','%ip%:%port%'],
        ['https://proxyscrape.com/free-proxy-list', '%ip%:%port%'],
        ['https://www.sslproxies.org/socks-proxy-list/', '%ip%:%port%'],
        ['https://spys.one/en/socks-proxy-list/', '%ip%:%port%'],
        ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=1000&country=all&ssl=all','%ip%:%port%']
    ]
    proxy_direct = [
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=5000&country=all&ssl=all&anonymity=all',
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=5000&country=all&ssl=all&anonymity=all',         
    ]

    def __init__(self):
        self.scrape_counter = 0
        self.checked_counter = 0

    def proxy_scrape(self):
        start = time.time()
        proxylist = []
        for url, regex in XProxy.proxy_w_regex:
            try:
                write(f'{Fore.RED}[*] {Style.RESET_ALL}Getting proxies: {Fore.YELLOW}{url}{Style.RESET_ALL}')
                html = requests.get(url).text
                iplist = re.findall(r'' + regex.replace('%ip%', '([0-9]{1,3}(?:\.[0-9]{1,3}){3})').replace('%port%', '([0-9]{2,5})') + '', str(html))
                for (ip, port) in iplist:
                    proxy = f'{ip}:{port}'
                    if proxy not in proxylist:
                        write(f'{Fore.RED}[+] {Style.RESET_ALL}Found proxy: {Fore.GREEN}{proxy}{Style.RESET_ALL}')
                        proxylist.append(proxy)
                        self.scrape_counter += 1
            except Exception as e:
                write(f'{Fore.RED}[-] {Style.RESET_ALL}Error: {e}')

        with open("proxies.txt", "a") as file:
            for proxy in proxylist:
                file.write(f"{proxy}\n")

        elapsed = time.time() - start
        set_title(f'Proxy - elapsed time: {elapsed:.2f} second | second collected: {self.scrape_counter} proxy')
        write(f'{Fore.RED}[*] {Style.RESET_ALL}Proxies are saved in {Fore.YELLOW}proxies.txt {Style.RESET_ALL}file.')
    
    def socks_proxy_scrape(self):
        start = time.time()
        proxylist = []
        for url, regex in XProxy.socks_proxy_list:
            try:
                write(f'{Fore.RED}[*] {Style.RESET_ALL}Getting proxies: {Fore.YELLOW}{url}{Style.RESET_ALL}')
                html = requests.get(url).text
                iplist = re.findall(r'' + regex.replace('%ip%', '([0-9]{1,3}(?:\.[0-9]{1,3}){3})').replace('%port%', '([0-9]{2,5})') + '', str(html))
                for (ip, port) in iplist:
                    proxy = f'{ip}:{port}'
                    if proxy not in proxylist:
                        write(f'{Fore.RED}[+] {Style.RESET_ALL}Found proxy: {Fore.GREEN}{proxy}{Style.RESET_ALL}')
                        proxylist.append(proxy)
                        self.scrape_counter += 1
            except Exception as e:
                write(f'{Fore.RED}[-] {Style.RESET_ALL}Error: {e}')

        for url in XProxy.proxy_direct:
            try:
                write(f'{Fore.RED}[*] {Style.RESET_ALL}Getting proxies: {Fore.YELLOW}{url}{Style.RESET_ALL}')
                proxies = requests.get(url).text.split()
                for proxy in proxies:
                    if proxy not in proxylist:
                        write(f'{Fore.RED}[+] {Style.RESET_ALL}Found proxy: {Fore.GREEN}{proxy}{Style.RESET_ALL}')
                        proxylist.append(proxy)
                        self.scrape_counter += 1
            except Exception as e:
                write(f'{Fore.RED}[-] {Style.RESET_ALL}Error: {e}')

        with open("socks_proxy.txt", "a") as file:
            for proxy in proxylist:
                file.write(f"{proxy}\n")

        elapsed = time.time() - start
        set_title(f'Proxy - elapsed time: {elapsed:.2f} second | second collected: {self.scrape_counter} proxy')
        write(f'{Fore.RED}[*] {Style.RESET_ALL}Proxies are saved in the {Fore.YELLOW}socks_proxy.txt {Style.RESET_ALL}file.')
    def proxy_check(self):
        checker = ProxyChecker()
        proxylist = []
        retries = 2
        while True:
            path = input(f'{Fore.YELLOW}[+] {Style.RESET_ALL}Enter proxy list path: ').strip('"')
            if os.path.isfile(path):
                break
            else:
                print(f"{Fore.MAGENTA}[-] {Fore.RED}The file is incorrect, please enter a valid file path.{Style.RESET_ALL}")

        with open(path, 'r') as file:
            proxylist = file.readlines()

        start = time.time()
        valid_proxies = []

        def check_proxy(proxy):
            attempt = 0
            while attempt < retries:
                try:
                    if checker.check_proxy(proxy):
                        write(f'{Fore.RED}[+] {Style.RESET_ALL}Valid proxy: {Fore.GREEN}{proxy}{Style.RESET_ALL}')
                        valid_proxies.append(proxy)
                        return
                    else:
                        write(f'{Fore.RED}[-] {Style.RESET_ALL}Invalid proxy: {Fore.YELLOW}{proxy}{Style.RESET_ALL}')
                        return
                except Exception as e:
                    attempt += 1
                    write(f'{Fore.RED}[-] {Style.RESET_ALL}Proxy check error {proxy} (Attempt {attempt}/{retries}): {e}')
                    if attempt >= retries:
                        write(f'{Fore.RED}[-] {Style.RESET_ALL}An error occurred after trying {retries} for the {proxy} proxy.')

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(check_proxy, proxy.strip()) for proxy in proxylist]

            for future in as_completed(futures):
                pass

        with open("valid_proxies.txt", "a") as valid_file:
            for proxy in valid_proxies:
                valid_file.write(f"{proxy}\n")

        elapsed = time.time() - start
        write(f'{Fore.RED}[*] {Style.RESET_ALL}Valid proxies are saved in the valid_proxies.txt file. Elapsed time: {elapsed:.2f} second | Checked: {len(proxylist)} proxy')
mdwth,watt = 'R','X', 
def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def set_title(title):
    sanitized_title = re.sub(r'[^\w\s-]', '', title)
    if platform.system() == "Windows":
        os.system(f'title {sanitized_title}')
    else:
        print(f'\33]0;{sanitized_title}\a', end='', flush=True)

def pause():
    if platform.system() == "Windows":
        os.system('pause>nul')
    else:
        input("Press Enter to continue...")

def main():
        init()
        clear_screen()
        print (xer),
        classes = f'{mdwth}{sett}{mdb}{defs}{watt}{x}'
        print(classes)
        init(autoreset=True)
        os.system('title Proxy Scraper') if platform.system() == 'Windows' else os.system('printf "\033]0;Proxy Scraper\007"')

        xproxy = XProxy()
        while True:
            print(UI.menu())
            try:
                option = int(input(f'{Fore.YELLOW}[+] {Style.RESET_ALL}Enter an option: '))
                if option == 1:
                    xproxy.proxy_scrape()
                    break
                elif option == 2:
                    xproxy.socks_proxy_scrape()
                    break
                elif option == 3:
                    xproxy.proxy_check()
                    break
                else:
                    write(f'{Fore.RED}[-] {Style.RESET_ALL}Invalid option.')
            except ValueError:
                write(f'{Fore.RED}[-] {Style.RESET_ALL}Please enter a valid number.')

if __name__ == "__main__":
    main()
