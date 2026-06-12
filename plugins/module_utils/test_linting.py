#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Test file with intentional linting issues."""

# Bad imports (wrong order, unused)
import sys
import os
from typing import Dict
import json
import boto3
from ansible.module_utils.basic import AnsibleModule

# Unused import
import datetime

# Bad formatting - long line
def really_long_function_name_that_exceeds_line_length(param1, param2, param3, param4, param5, param6, param7, param8):
    """This line is way too long and should be wrapped."""
    pass

# Unused variable
def function_with_unused_var():
    unused_variable = "this is never used"
    x = 1
    return x

# Bad spacing
def bad_spacing( x,y,z ):
    return x+y+z

# Missing docstring and bad naming
def f(x):
    return x*2

# Should use f-string
def old_string_formatting():
    name = "test"
    return "Hello %s" % name

# Complexity issue - deeply nested
def complex_function(a, b, c, d):
    if a:
        if b:
            if c:
                if d:
                    if a > 5:
                        if b > 10:
                            if c > 15:
                                return True
    return False
