# Python resources

Literal is an object

python3 -m venv .venv
-m tells python to use a module here it tells to use venv module

.venv is the name/directory location

source .venv/bin/activate - to activate the virtual environment replcae .venv with folder name if other name is given
virtual environments are separate from global environment
deactivate - to deactivate the environment


site-packages is the target directory of manually built Python packages. When you build and install Python packages from
source (using distutils, probably by executing python setup.py install), you will find the installed modules in site-packages by default.

pip3 install wheel
wheel helps in downloading and installing other packages

pip3 install requests arrow
pip3 list
pip3 list --not-required # doesnot show dependencies required by installed packages

pip3 uninstall arrow
pip3 help install # gives documentation for pip install
pip3 show requests # details of the library
pip3 install requests==2.0
pip3 install -U requests upgrades requests package
pip3 freeze gives input of requirements.txt
pip3 install -r requirements.txt -r denotes the flag for path of file with requirements
