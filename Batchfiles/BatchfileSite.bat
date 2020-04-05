set url="http://127.0.0.1:5000/"
start chrome %url%
cd \Users\Brand\Desktop\v1gp-master
set FLASK_APP=huw.py
python -m flask run
start http://127.0.0.1:5000/
