# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: test.py

@time: 2018/1/10 17:40

@desc:

'''

from jinja2 import Template
template = Template('Hello {{ name }}!')
print template.render(name='John Doe')