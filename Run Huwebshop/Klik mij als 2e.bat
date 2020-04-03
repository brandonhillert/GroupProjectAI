set url="http://127.0.0.1:5000/"
start chrome %url%

cd \Users\julian\Documents\GitHub\GroupProjectAI\v1gp-master
set FLASK_APP=huw.py
py -m flask run

start url="http://127.0.0.1:5000/"