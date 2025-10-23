
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
pip install -r requirements.txt


runtest
pytest -q
pytest tests/test_login.py -vv

