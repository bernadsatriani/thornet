import sys
import os
import zipfile
import getpass
import urllib2
import platform
import subprocess
from urllib import urlretrieve
from thornet_info import *


system_user = getpass.getuser()

if platform.system() != 'Linux':
    print red + bold + '[-] ' + 'Sorry but only Linux distributions are supported.' + white
    sys.exit(0)


if os.getuid() != 0:
    print program_info('Are you root? Please run as ', symbol_color=red, text_color=yellow) + red + bold + underline\
          + 'root' + white
    sys.exit(0)

if system_user == 'root':
    cache_dir = '/root/.cache/thornet'
else:
    cache_dir = '/home/%s/.cache/thornet' % system_user


def update_script(repo_version):
    print program_info('Downloading thornet (build %d)....' % repo_version, symbol='+')
    try:
        urlretrieve('https://github.com/5kyc0d3r/thornet/archive/master.zip', '%s/thornet.zip' % cache_dir)
    except IOError:
        print program_info('Download failed.', symbol='-', symbol_color=red)
        sys.exit(1)

    print program_info('Successfully downloaded thornet build %d.' % repo_version, symbol='+')
    print program_info('Executing setup.py....', symbol='+')

    print program_info('Unzipping thornet.zip....', symbol='+')
    zip_ref = zipfile.ZipFile('%s/thornet.zip' % cache_dir, 'r')
    zip_ref.extractall(cache_dir)
    zip_ref.close()

    print program_info('Executing setup.py....', symbol='+')
    print white + bold
    os.chdir('%s/thornet-master' % cache_dir)
    os.system('python setup.py install')
    print program_info('Script updated.', symbol='+')
    print program_info('Restarting....')
    os.execl('/usr/local/bin/thornet', '', '')
    sys.exit(0)


def check_for_update():
    print white + bold + 'Checking for updates....' + white
    version_url = 'https://raw.githubusercontent.com/5kyc0d3r/thornet/master/info/build'
    repo_version = int(urllib2.urlopen(version_url).read())
    if build < repo_version:
        print program_info('A newer version of Thornet Toolset was found! '
                           '(version %s)' % repo_version)
        update = raw_input(white + bold + '\nWould you like to update?\n(y/N): ').lower()
        if update in ('y', 'yes'):
            update_script(repo_version)
        elif update in ('n', 'no'):
            print white + bold + 'Update cancelled.\n' + white
        else:
            print white + bold + 'Update ignored.\n' + white

    elif build == repo_version:
        print green + bold + 'No update available, latest version is already installed.\n' + white

    else:
        print red + bold + 'Wait wut? WTF!!!\n' + white

    return True


def check(program, extra_arg=''):
    try:
        devnull = open(os.devnull)
        subprocess.Popen([program, extra_arg], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True
