#! Must keep all the project file in the same directory.

Before run the project, the user must set these variable:
  - Environment variable & prjcre source:
    - source <absolute path to prjcre.sh - a file in .prjcre>
    - export PRJCRE_CONFIG=<absolute path to .prjcre project directory>
    ! Notes: This 2 lines must be in the user terminal file. For example, if the user using zsh on mac then they will need to this 2 lines in .zshrc

  - Change the name of config+template.json to config.json then fill in the information in the config.json file. Instruction on what information need is in the file itself

  - For this program to work, the user also need to manually install virtualenv for python and python3 must be install in the local machine. Additionally, chrome driver is need. User can download chrome driver from this site: https://chromedriver.chromium.org/downloads
