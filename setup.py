import yaml
import sys
import os

setup = os.path.abspath(os.path.dirname(os.path.realpath(__file__))+'/config_files')

def YN(q1,q2,default):
    choice = input(f'{q1} {default} ')
    if choice.lower()=='y':
        return (default)
    else:
        return(input(f'{q2} '))

def run(wd):
    print(setup)
    with open(f'{setup}/user_path_definitions_template.yml') as yml:
        config = yaml.safe_load(yml)
    print('Verify paths for setup or specify custom locations')

    for key,value in config['rootDir'].items():
        value = os.path.abspath(value)
        value = YN(f'Y/N Path to {key}:',f'Specify alternative location for {key}: ',value)
        config["rootDir"][key] = value

    for key,value in config['relDir'].items():
        value = os.path.abspath(f'{wd}/{value}')
        value = YN(f'Y/N Path to {key}:',f'Specify alternative location for {key}: ',value)
        if os.path.isdir(value) == False:
            os.makedirs(value)
        config["relDir"][key] = value

    with open(f'{wd}/config_files/user_path_definitions.yml', 'w') as outfile:
        yaml.dump(config, outfile, default_flow_style=False)

    if os.path.isfile(f'{wd}/.gitmodules'):
        with open('.gitmodules') as f:
            for l in f.readlines():
                if 'path = ' in l:
                    if os.path.isdir(f"{wd}/{l.split('path = ')[1].replace('\n','')}/config_files"):
                        with open(f"{wd}/{l.split('path = ')[1].replace('\n','')}/config_files/user_path_definitions.yml", 'w') as outfile:
                            yaml.dump(config, outfile, default_flow_style=False)
        