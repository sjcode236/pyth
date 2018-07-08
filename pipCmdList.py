

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
    
===Installing python3.6 ==============================================================
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
# python3 -V
    
 
  
