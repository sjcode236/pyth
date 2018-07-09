

===What is pip
What is pip
pip is a package manager for the Python programming language. It provides access to a massive repository of 
open source tools and libraries, as well as the ability to manage your own proprietary packages. One of the greatest 
benefits to using a package manager is that it automatically installs the dependencies of any package you install, 
allowing you to more quickly get back to writing some code.

===Installing pip 
pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org 
pip install instructions are  at  
https://pip.pypa.io/en/stable/installing/
  
===Upgrading pip
On Linux or macOS:
    pip install -U pip
On Windows [4]:
    python -m pip install -U pip
    
===================================================================================
python2.8  install pip and python 3.6  install pip3
/usr/local/bin/pip3  
python2.7 is  python  and python3.6 is python3
/usr/bin/python -> python2
/usr/local/bin/python3 -> python3.6
========================================================================

https://pip.pypa.io/en/stable/reference/pip/
pip3 --help
pip install bar
$ pip3 list
$ pip list --format columns
$ pip show sphinx
$ pip3 show --verbose sphinx

$ pip check
pyramid 1.5.2 requires WebOb, which is not installed.

===Installing python3.6 =====This version has pip already installed=========================================
https://www.tecmint.com/install-python-in-linux/
==Prior to installing Python in CentOS 7, let’s make sure our system has all the necessary development dependencies:
# yum -y groupinstall development
# yum -y install zlib-devel
To install Python 3.6, run the following steps:
# wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
# tar xJf Python-3.6.3.tar.xz
# cd Python-3.6.3
# ./configure
# make
# make install 

# which python3
# python3 --version

====Installing python2.7.14===================================
https://danieleriksson.net/2017/02/08/how-to-install-latest-python-on-centos/
https://docs.snowflake.net/manuals/user-guide/python-install.html
# Start by making sure your system is up-to-date:
yum update
# Compilers and related tools:
yum groupinstall -y "development tools"  or yum groupinstall -y development
# Libraries needed during compilation to enable all features of Python:
yum install -y zlib-devel openssl-devel sliteq-devel bzip2-devel
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
# If you are on a clean "minimal" install of CentOS you also need the wget tool:
yum install -y wget








    
 
  
