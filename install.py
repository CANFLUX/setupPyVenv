import subprocess
import sys
import os

setup = os.path.dirname(os.path.realpath(__file__))
setup = os.path.abspath(os.path.split(setup)[0]+'/config_files')
wd = os.getcwd()


def YN(q1,q2,default):
    choice = input(f'{q1} {default} ')
    if choice.lower()=='y':
        return (default)
    else:
        choice = input(f'{q2} ')
        if choice.lower() == 'y':
            return('')
        else:
            sys.exit('Exiting install.py')

wd = YN('Y/N install dependencies as a virtual environment in:','Y/N install dependencies in your base Python installation: ',wd)

if sys.platform.startswith("darwin"): 
    req = 'requirements_unix.txt'
elif sys.platform.startswith("win"): 
    req = 'requirements_windows.txt'

cmd=['pip install -r', req]

if wd == '':
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(proc.stderr)
else:
    proc = subprocess.run(["python", "-m", "venv", ".venv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(proc.stderr)
    proc = subprocess.run(['.\.venv\Scripts\activate'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(proc.stderr)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(proc.stderr)
    
import setup
setup.run(wd)