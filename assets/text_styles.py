# -*- encoding: utf-8 -*-

version = 1.2

purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
white = '\033[0m'
italic = '\033[3m'
bold = '\033[1m'
underline = '\033[4m'

green_block = '\x1b[6;6;42m'  # 2nd 6; --> text-color
no_block = '\x1b[0m'


brand = red + bold + """
        ▄▄▄█████▓ ██░ ██  ▒█████   ██▀███   ███▄    █ ▓█████ ▄▄▄█████▓
        ▓  ██▒ ▓▒▓██░ ██▒▒██▒  ██▒▓██ ▒ ██▒ ██ ▀█   █ ▓█   ▀ ▓  ██▒ ▓▒
        ▒ ▓██░ ▒░▒██▀▀██░▒██░  ██▒▓██ ░▄█ ▒▓██  ▀█ ██▒▒███   ▒ ▓██░ ▒░
        ░ ▓██▓ ░ ░▓█ ░██ ▒██   ██░▒██▀▀█▄  ▓██▒  ▐▌██▒▒▓█  ▄ ░ ▓██▓ ░
          ▒██▒ ░ ░▓█▒░██▓░ ████▓▒░░██▓ ▒██▒▒██░   ▓██░░▒████▒  ▒██▒ ░
          ▒ ░░    ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░░ ▒░ ░  ▒ ░░
            ░     ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░░ ░░   ░ ▒░ ░ ░  ░    ░
          ░       ░  ░░ ░░ ░ ░ ▒    ░░   ░    ░   ░ ░    ░     ░
                  ░  ░  ░    ░ ░     ░              ░    ░  ░

                {}
              {} Thornet version: [{}]
               Project page: {}
""".format(white + bold + underline + italic + 'Automated attacks for faster hacking / cracking.' + white,
           bold + yellow + italic + 'THORNET TOOLSET BY @5kyc0d3r.' + white + red + bold,
           green + str(version) + red,
           green + "https://github.com/5kyc0d3r/thornet" + white
           )


def category_banner(banner_text):
    return red + bold + '[ ' + green + bold + banner_text + red + bold + ' ]'


def thornet_input(text, newline=False):
    if newline:
        return white + bold + '\nthornet (' + red + bold + text + white + bold + ')> ' + green + bold
    else:
        return white + bold + 'thornet (' + red + bold + text + white + bold + ')> ' + white + bold


def numbered_list(my_list):
    nm_list = []
    for x in range(len(my_list)):
        nm_list.append(bold + red + '  [' + green + str(x + 1) + red + bold + '] ' + white + bold + my_list[x])
    return nm_list


def program_info(message, symbol='!', symbol_color=green, text_color=white):
    return red + bold + '[' + symbol_color + bold + symbol + red + bold + '] ' + text_color + bold + message + white


def exit_message(message):
    return green + bold + '\n\n' + message + '\n' + white
