import os
from shellcat_modules.banners import banner_andro, preter_banner, main_banner, warning, rat_banner
from shellcat_modules.pwncat_lib import shell_build
import random
import shutil
from sys import exit
import yaml

# COLORS
cyan = '\x1b[0;36m'
green = '\x1b[0;32m'
oke_green = '\x1b[0;92m'
light_green = '\x1b[1;32m'
white = '\x1b[1;37m'
red = '\x1b[1;31m'
yellow = '\x1b[0;33m'
BlueF = '\x1b[1;34m'
RESET = "\x1b[0m"
orange = '\x1b[38;5;166m'
Blue = '\033[1;34m'
Green_light = '\033[1;32m'
# End Set-Colors


def main():
    try:
        while True:
            check_config_file()  # Checking configuration file exists
            read_config_file()  # Reading path to save payloads
            cons_cl()  # Clear Console
            main_banner()  # Printing Menu Banner

            shell = input(f'''{white}
{green}┌─[{red}ShellCat{green}]──[{red}~{green}]─[{orange}0xB5ff{green}]{green}:
└─────►{orange} ''')

            while not shell in ['1', '2', '3', '4', '5', 6]:
                print(f'{white}[{cyan}+{white}]{red} Option Invalid!{Green_light}')
                shell = input(f'''{white}
{green}┌─[{red}ShellCat{green}]──[{red}~{green}]─[{orange}0xB5ff{green}]{green}:
└─────►{orange} ''')

            else:
                if shell == '1':
                    shell_build()  # Building shell with module pwncat_lib.py

                elif shell == '2':
                    os.system('cd microsploit_src;bash Microsploit')
                    clean_dir_path()
                    main()

                elif shell == '3':
                    os.system('cd BruteSploit;bash Brutesploit')
                    clean_dir_path()
                    main()

                elif shell == '4':
                    cons_cl()  # Clear console
                    warning()  # Don't UPLOAD TO ANTIVIRUS
                    print_banner()  # print random banner
                    print(f' {white}[{green}+{white}]{green} T H A N K S    F O R    U S I N G \n'
                          f'\t{white}S {red}H {BlueF}E {yellow}L {cyan}L {oke_green}- {orange}C {red}A {BlueF}T ')
                    exit(0)

                elif shell == '5':
                    cons_cl()  # Clear console
                    main_banner()  # Printing menu-banner

                elif shell == '6':
                    clean_dir_path()  # Clearing files from the directory for saving

    except KeyboardInterrupt:
        print(f'\n{white}[{red}!{white}]{green} Ctrl+C Detected. Exiting...')


def clean_dir_path(): # The cleaning function it`self
    if check_config_file(): # Checking conf file IF --> TRUE --> READING -- > DELETING TREE FILES
        with open('config.yaml', 'r') as f:
            config_data = yaml.load(f, Loader=yaml.FullLoader)

        path_to_clean = config_data.get('savedir')

        if path_to_clean:

            try:
                shutil.rmtree(path_to_clean)
                print(f'{white}[{Blue}+{white}]{Blue} Directory is Cleaned!')

            except:
                print(f'{white}[{red}-{white}]{red} Directory cleaning FAIL!')

        else:
            print(f'{white}[{red}-{white}]{red} Directory not found in config file!')


def read_config_file():
    global payload_save  # For save payloads
    if check_config_file():
        with open('config.yaml', 'r') as f:
            config_data = yaml.load(f, Loader=yaml.FullLoader)

        payload_save = config_data.get('savedir')
    return payload_save




def check_config_file(): # checking config_file itself
    if os.path.exists('config.yaml'):
        print(f'{cyan}[OK]')
        return True
    else:
        saving_directory()


def saving_directory(): # function for create conf file
    cons_cl()
    rat_banner()
    while True:
        shell = input(f'''{white}
{green}┌─[{red}ShellCat{green}]──[{red}~{green}]─[{orange}0xB5ff{green}]{green}:
└─────►{orange} ''')
        if os.path.exists(shell):
            config = {'savedir': shell}
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file)
            break
        else:
            print(f'{white}[{light_green}+{white}] {yellow}Path not found!')


def print_banner(): # random banner printing
    numeric = ['1', '2']
    rand_num = random.choice(numeric)
    if rand_num == '1':
        cons_cl()
        banner_andro()
    elif rand_num == '2':
        cons_cl()
        preter_banner()
    else:
        pass


def cons_cl(): # clear console
    os.system('clear')


