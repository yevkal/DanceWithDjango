How to develop?
git clone https://github.com/yevkal/DanceWithDjango
python3 -m venv venv
. venv/bin/python3 (linux and macos) or venv\Scripts\activate.bat (windows)
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
