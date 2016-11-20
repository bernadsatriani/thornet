import sys
import os
import urllib2
import subprocess
from text_styles import *


def update_script():
    print exclam_mark('Updating script....')
    os.system('git clone %s' % project_page)
    print exclam_mark('Script updated.', text_color=white)
    sys.exit(0)


def check_for_update():
    print white + bold + 'Checking for updates....' + white
    version_url = 'https://raw.githubusercontent.com/5kyc0d3r/thornet/master/info/build'
    repo_version = int(urllib2.urlopen(version_url).read())
    if build < repo_version:
        print exclam_mark('A newer version of Thornet Toolset was found! '
                          '(version %s)' % repo_version)
        update = raw_input(white + bold + '\nWould you like to update?\n(y/N): ').lower()
        if update in ('y', 'yes'):
            print 'Script will now be updated.'
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
