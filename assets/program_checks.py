import os
import urllib2
import subprocess
from text_styles import *


def update_script():
    return True


def check_for_update():
    version_url = 'https://raw.githubusercontent.com/5kyc0d3r/thornet/master/build'
    repo_version = int(urllib2.urlopen(version_url).read())
    if build < repo_version:
        print exclam_mark('A newer version of Thornet Toolset was found! '
                          '(version %s)' % repo_version)
        update = raw_input(white + bold + '\nWould you like to update?\n(y/N): ').lower()
        if update in ('y', 'yes'):
            print 'Script will now be updated.'
        elif update in ('n', 'no'):
            print 'Update cancelled.'
        else:
            print 'Update ignored.'

    elif build == repo_version:
        print 'Latest version installed.'

    else:
        print 'Wait wut? WTF!!!'

    return True


def check(program, extra_arg=''):
    try:
        devnull = open(os.devnull)
        subprocess.Popen([program, extra_arg], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True
