set url="http://127.0.0.1:5001/"
start chrome %url%

cd \Users\Brand\Desktop\v1gp-master
set FLASK_APP=huw_recommend.py
python -m flask run --port 5001
start http://127.0.0.1:5000/
