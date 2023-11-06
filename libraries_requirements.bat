@echo off
echo Installing Python libraries...

REM Install the 'requests', 'dnspython', 'colorama', 'argparse', and 'futures' libraries
pip install requests
pip install dnspython
pip install colorama
pip install argparse
pip install futures

echo Python libraries installation complete.
pause