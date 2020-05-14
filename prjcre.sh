#!/usr/local/bin/python3

prjcre() {
  cd $PRJCRE_CONFIG
  config=$PRJCRE_CONFIG

  python3=$(jq -r '.path | .python3' 'config.json')
  local_repo=$(jq -r '.path | .local_repo' 'config.json')

  # check for same name prj
  cd $local_repo
  if test -d "$1" ; then
    echo "You have another project with the same name"
    echo "Unable to create the project repository"
    return
  fi

  # setup python3 virtual enviroment
  cd $config
  if test -d ".env" ; then
    source .env/bin/activate
  else
    virtualenv -p $python3 .env
    source .env/bin/activate
    pip install -r venv_req.txt
  fi

  # create project repository
  python main.py $*

  deactivate

  cd $local_repo/"$1"
  open $local_repo/"$1"
}
