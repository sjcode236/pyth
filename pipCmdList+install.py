

===What is pip
What is pip
pip is a package manager for the Python programming language. It provides access to a massive repository of 
open source tools and libraries, as well as the ability to manage your own proprietary packages. One of the greatest 
benefits to using a package manager is that it automatically installs the dependencies of any package you install, 
allowing you to more quickly get back to writing some code.

===Installing pip ===============================================
pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org 
pip install instructions are  at  
https://pip.pypa.io/en/stable/installing/
  
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install setuptools
pip --version
 =====OR======
# First get the script:
wget https://bootstrap.pypa.io/get-pip.py
# Then execute it using Python 2.7 and/or Python 3.6:
python2.7 get-pip.py
python3.6 get-pip.py
# With pip installed you can now do things like this:
pip2.7 install [packagename]
pip2.7 install --upgrade [packagename]
pip2.7 uninstall [packagename]
  
===Upgrading pip ===========================================
On Linux or macOS:
    pip install -U pip  OR   pip install --upgrade pip 
On Windows [4]:
    python -m pip install -U pip
===================================================================================
python2.8  install pip/pip2.8 and python 3.6  install pip3/pip3.6
/usr/local/bin/pip3  
python2.7 is  python  and python3.6 is python3
/usr/bin/python -> python2
/usr/local/bin/python3 -> python3.6
======pip commands =================================================================
https://pip.pypa.io/en/stable/reference/pip/
pip3 --help
pip install bar
$ pip3 list
$ pip list --format columns
$ pip show sphinx
$ pip3 show --verbose sphinx

$ pip check
pyramid 1.5.2 requires WebOb, which is not installed.

===Installing python3.6 =====This version has pip already installed =========================================
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
yum -y install  zlib-devel openssl-devel sliteq-devel bzip2-devel      OR
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
# If you are on a clean "minimal" install of CentOS you also need the wget tool:
yum install -y wget

wget http://python.org/ftp/python/2.7.14/Python-2.7.14.tar.xz
tar xf Python-2.7.14.tar.xz
or
curl -O https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
tar xvfz Python-2.7.10.tgz
cd Python-2.7.14
./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared 
make  
make altinstall    OR make install
===============================================================








    
 
  
