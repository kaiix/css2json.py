# css2json.py

[![PyPI version]][PyPI]

Convert style sheets to json. Python clone of kesla/css2json

### Install

```pip install css2json```

### Usage

```
>>> import css2json
>>> css2json.css2json("""
... p {
...     color: #222;
...     margin: 10px;
... }
... """)
'{"p": {"color": "#222", "margin": "10px"}}'
>>>
```


[PyPI version]:    https://img.shields.io/pypi/v/css2json.svg?style=flat
[PyPI]:            https://pypi.python.org/pypi/css2json