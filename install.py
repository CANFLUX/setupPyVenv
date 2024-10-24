import subprocess
import shutil
import sys
import os

wd = os.getcwd()
subprocess.check_call([sys.executable,'-m','pip','install','pyyaml'])
import setup
setup.run(wd=wd)

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

if os.path.isdir(f'{wd}/.venv'):
    if YN('Y/N Use existing .venv in','Y/N Delete existing .venv',wd) == '':
        shutil.rmtree(f'{wd}/.venv')
    
if os.path.isdir(f'{wd}/.venv')==False:
    cfgPath = os.path.abspath(os.path.dirname(os.path.realpath(__file__))+'/config_files')
    if sys.platform.startswith("darwin"): 
        req = cfgPath+'/requirements_unix.txt'
    elif sys.platform.startswith("win"): 
        req = cfgPath+'/requirements_windows.txt'

    cmd=['pip','install','-r', req]

    proc = subprocess.run(["python", "-m", "venv", ".venv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(proc.stderr)
    cmd =[os.path.abspath('./.venv/Scripts/python'),'-m','pip','install','-r', req]
    print(cmd)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(proc.stderr,proc.stdout)
        