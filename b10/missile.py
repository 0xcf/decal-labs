import sys
from termcolor import cprint
from pyfiglet import figlet_format
cprint(figlet_format('missile!', font='starwars'),
               'yellow', 'on_red', attrs=['bold'])
