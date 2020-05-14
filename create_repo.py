from os import chdir
from sys import exit
from json import load
from subprocess import run

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

import git_repo as gr

with open('config.json') as config_file:
    config = load(config_file)


def create_remote_repo(prj_info):
    chrome_opts = Options()
    chrome_opts.add_argument("--headless")

    driver = webdriver.Chrome(executable_path=config['path']['chrome_driver'], options=chrome_opts)

    try:
        driver.get("https://github.com/login")
        gr.git_login(driver, config['git']['username'], config['git']['password'])
        gr.git_create_repo(driver, prj_info['name'], prj_info['des'])
        print("Successful create remote repository...\n")

    except TimeoutException:
        print("Raise timeout Error... Unable to create remote repository...\n")
        exit(3)

    finally:
        driver.quit()


def create_local_repo(prj_name, is_python=False):
    chdir(config['path']['local_repo'])

    run(['mkdir', prj_name])
    chdir(prj_name)

    run(['git', 'init'])
    run(['touch', 'README.md', '.gitignore', 'config.json'])
    gitignore = open(".gitignore", "w")

    run(['echo', '.DS_Store\nconfig.json'], stdout=gitignore)

    if is_python:
        run(['virtualenv', '-p', config['path']['python3'], '.env'])
        print('Create python3 virtualenv.')
        run(['touch', 'main.py', 'test.py', 'venv_req.txt'])
        run(['echo', 'test.py\n.idea\n.env/\n__pycache__/\n'], stdout=gitignore)
    else:
        pass

    run(['git', 'add', '-A'])
    run(['git', 'commit', '-m', 'initial commit'])

    gitignore.close()


def create_repo(prj_info):
    create_remote_repo(prj_info)
    create_local_repo(prj_info['name'], prj_info['is_python'])

    run(['git', 'remote', 'add', 'origin', f"https://github.com/{config['git']['username']}/{prj_info['name']}.git"])
    run(['git', 'push', '-u', 'origin', 'master'])
