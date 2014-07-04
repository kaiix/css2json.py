import os
import json as jsonlib

from css2json import css2json

for base in ['simple', 'advanced', 'advanced2', 'comments']:
    with open(os.path.join(os.path.dirname(__file__), 'tests', base+'.css')) as css, \
         open(os.path.join(os.path.dirname(__file__), 'tests', base+'.json')) as json:
        s1 = jsonlib.dumps(jsonlib.loads(css2json(css.read())), sort_keys=True)
        s2 = jsonlib.dumps(jsonlib.load(json), sort_keys=True)
        assert s1 == s2, 'test failed on `%s`' % base

print 'test passed'
