#!/usr/bin/env python3

import os
import subprocess
import platform
from colorama import init, Fore, Style
init(autoreset=True)

def install_dependencies():
    try:
        print(f"{Fore.LIGHTCYAN_EX}------------------------------------------------")
        print(f"{Fore.CYAN}[{Fore.YELLOW}-{Fore.CYAN}]{Fore.WHITE} Installing required packages...")
        print(f"{Fore.LIGHTCYAN_EX}------------------------------------------------")
        subprocess.run([get_pip_command(), 'install', '--upgrade', 
                        'requests', 'colorama', 'proxy_checker', 'tqdm', 
                        'tabulate', '--break-system-packages'], check=True)
        print(f"{Fore.LIGHTCYAN_EX}------------------------------------------------")
        print(f"{Fore.CYAN}[{Fore.GREEN}+{Fore.CYAN}]{Style.RESET_ALL} Packages installed successfully.")
        print(f"{Fore.LIGHTCYAN_EX}------------------------------------------------")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.LIGHTCYAN_EX}------------------------------------------------")
        print(f"{Fore.CYAN}[{Fore.RED}x{Fore.CYAN}]{Fore.WHITE} An error occurred while installing packages: {e}")
        print(f"{Fore.LIGHTCYAN_EX}------------------------------------------------")

def get_pip_command():
    if platform.system().lower() == 'windows':
        return 'pip'
    else:
        return 'pip3'

def get_python_command():
    if platform.system().lower() == 'windows':
        return 'python'
    else:
        return 'python3'

def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def main():
    init()
    clear_screen()
    init(autoreset=True)
    print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT} RProxy Installer")

    if os.name != 'nt' and hasattr(os, 'geteuid') and os.geteuid() == 0:
        print(f"{Fore.CYAN}[{Fore.RED}x{Fore.CYAN}]{Style.RESET_ALL} ERROR, YOU MUST RUN THE PROGRAM AS AN ADMINISTRATOR.")
        return

    install_dependencies()

if __name__ == "__main__":
    main()
