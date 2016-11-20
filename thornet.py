#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import urllib2
from assets.text_styles import *
from assets.program_checks import *


project_page = 'https://github.com/5kyc0d3r/thornet'

categories = ['Wireless Attacks', 'Backdoor Generators', 'Brute Force Attacks',
              'DDoS Attacks', 'System Shell', 'Man In The Middle Attacks']

messages = {'exit': 'Thank you for using Thornet, goodbye!'}

os.system('clear')

print brand
methods = {}
c = 0
for cat in categories:
    c += 1

    if len(cat.split()) == 5:
        cat_split_1 = cat.split()[len(cat.split()) - 5].lower()
        cat_split_2 = cat.split()[len(cat.split()) - 4].lower()
        cat_split_3 = cat.split()[len(cat.split()) - 3].lower()
        cat_split_4 = cat.split()[len(cat.split()) - 2].lower()
        cat_split_5 = cat.split()[len(cat.split()) - 1].lower()
        methods.update({c: cat_split_1 + '_' + cat_split_2 + '_' + cat_split_3 +
                        '_' + cat_split_4 + '_' + cat_split_5})
        globals().update(methods)

    elif len(cat.split()) == 3:
        cat_split_1 = cat.split()[len(cat.split()) - 3].lower()
        cat_split_2 = cat.split()[len(cat.split()) - 2].lower()
        cat_split_3 = cat.split()[len(cat.split()) - 1].lower()
        methods.update({c: cat_split_1 + '_' + cat_split_2 + '_' + cat_split_3})
        globals().update(methods)

    elif len(cat.split()) == 2:
        cat_split_1 = cat.split()[len(cat.split()) - 2].lower()
        cat_split_2 = cat.split()[len(cat.split()) - 1].lower()
        methods.update({c: '%s_%s' % (cat_split_1, cat_split_2)})
        globals().update(methods)

    else:
        cat_split_1 = cat.split()[len(cat.split()) - 1].lower()
        methods.update({c: '%s' % cat_split_1})
        globals().update(methods)


def wireless_attacks(show_brand=True):
    os.system('clear')
    if show_brand:
        print brand
    print category_banner('Wireless Attacks')
    sys.exit(0)


def backdoor_generators(show_brand=True):
    os.system('clear')
    if show_brand:
        print brand
    print category_banner('Backdoor Generators')
    sys.exit(0)


def brute_force_attacks(show_brand=True):
    os.system('clear')
    if show_brand:
        print brand
    print category_banner('Brute Force Attacks')
    sys.exit(0)


def ddos_attacks(show_brand=True):
    os.system('clear')
    if show_brand:
        print brand
    print category_banner('DDoS Attacks')
    sys.exit(0)


def system_shell(show_brand=True):
    if show_brand:
        os.system('clear')
        print brand
        print category_banner('System Shell') + '\n'

    command = raw_input(thornet_input('shell'))

    try:
        if command.split()[0] == 'exit':
            main()
    except IndexError:
        pass

    os.system(command)
    system_shell(show_brand=False)


def man_in_the_middle_attacks(show_brand=True):
    if show_brand:
        os.system('clear')
        print brand
    print category_banner('Man In The Middle Attacks')
    sys.exit(0)


def main():
    try:
        os.system('clear')
        print brand
        print category_banner('Categories')

        for item in numbered_list(categories):
            print item

        cat_input = raw_input(thornet_input('category', newline=True))

        try:
            if cat_input.split()[0].lower() == 'exit':
                print exit_message(messages['exit'])
                sys.exit(0)
        except IndexError:
            main()

        try:
            if int(cat_input) in methods:
                method_name = methods[int(cat_input)]

                try:
                    globals()[method_name]()
                except KeyError:
                    print 'Method %s not implemented.' % method_name
                    main()
                except KeyboardInterrupt:
                    main()

            else:
                main()
        except ValueError:
            main()
    except KeyboardInterrupt:
        print exit_message(messages['exit'])
        sys.exit(1)

if __name__ == '__main__':
    program_not_installed = False
    urllib2.urlopen('https://github.com')
    programs_required = ['aircrack-ng', 'ettercap', 'xterm']
    print '{}{}{} {}'.format(red + bold + '[', green + bold + '*', red + bold + ']',
                             white + bold + 'Checking if required programs are installed....\n')
    for programs in reversed(programs_required):
        is_installed = check(programs)
        if is_installed:
            print '{}{}{} {}{}'.format(red + bold + '[', green + bold + '+', red + bold + ']',
                                       white + bold + programs + '....', green + bold + 'OK.')
        else:
            print '{} {}{}'.format(red + bold + '[-]', white + bold + programs + '....',
                                   red + bold + 'NOT INSTALLED.')
            program_not_installed = True
    if program_not_installed:
        print red + bold + '\n[!] Some required programs were not found on the system. Please install ' \
                           'them to use this script.'
        sys.exit(1)
    else:
        print red + bold + '\n[' + green + bold + '+' + red + bold + '] ' + white + bold + 'All requirements found.'

    main()
