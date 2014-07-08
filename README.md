# css2json.py

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
