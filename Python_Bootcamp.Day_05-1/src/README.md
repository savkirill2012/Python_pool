# Day05
## Requirements
- Python 3.9 or higher
- Create virtual enviroments
## Create and activate virtual enviroments
```
python3 -m venv Task2/venv
source venv/bin/activate
pip install -r Task2/requirements.txt
```

## Task2
Run Flask app
```
python3 src/Task2/task2.py
```
Open `http://localhost:8888/`.


In new terminal

Show all uploaded files
```
python3 src/Task2/screwdriver.py list
```
Upload new file
```
python3 src/Task2/screwdriver.py upload 'path-to-file'
```