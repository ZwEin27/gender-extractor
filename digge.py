# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-21 09:45:34
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-21 09:54:51

import re

######################################################################
#   Constant
######################################################################

GE_GENDER_NAMES = [
    'trans',
    'transgender',
    'ts',
    'male',
    'female'
]


######################################################################
#   Regular Expression
######################################################################

reg_gender_name = r'\b(?:'+r'|'.join(GE_GENDER_NAMES)+r')\b'
re_gender_name = re.compile(reg_gender_name, re.IGNORECASE)

######################################################################
#   Main Class
######################################################################

class DIGGE(object):

    def __init__(self):
        pass




if __name__ == '__main__':
    text = 'hello world female blah blah'
    print re_gender_name.findall(text)

