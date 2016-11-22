## Thornet Toolset
[![Build Status](https://travis-ci.org/5kyc0d3r/thornet.svg?branch=master)](https://travis-ci.org/5kyc0d3r/thornet)
[![Packagist](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](https://github.com/5kyc0d3r/thornet/blob/master/LICENSE)
[![Packagist](https://img.shields.io/badge/platform-Linux-orange.svg)](#)

![alt text](http://i.imgur.com/826hoc3.png "Thornet Toolset v1.2")

Thornet Toolset allows you to quickly launch all sorts of attacks, including but not limited to, Wi-Fi attacks, Man In The Middle Attacks and DDoS Attacks.

## What is Thornet?

Thornet is an automation tool that was made to launch faster attacks, without having to type in long commands. Thornet does not come with any tools and therefore relies on a set of tools that should be installed on your system before using it (all tools used by Thornet come pre-installed on Kali Linux). Thornet currently does not include every feature of all the tools that are being used by it. Please see the [requirements section](#requirements) to see what tools need to be installed on your system in order to use Thornet.
Thornet was written in Python 2.7 by [@5kyc0d3r](https://github.com/5kyc0d3r).

## Installation
1. Clone the repo & cd into the new folder (thornet)

   ```$ git clone https://github.com/5kyc0d3r/thornet.git && cd thornet```

2. Run the setup.py
   
   ```$ sudo python setup.py install```
   
3. Run Thornet

  At this point, if all of the above commands were successful, then Thornet should now be installed and is ready to execute.
  *Thornet requires root privileges, so run it with sudo if you're not root.*

   ```$ sudo thornet```

## Requirements
* Aircrack-ng
* Ettercap
* xterm
* Git
* Python 2.7
