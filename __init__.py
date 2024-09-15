"""! AI Suppliers """

## \file ../src/ai/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from packaging.version import Version
from .version import __version__, __name__, __doc__, __details__, __annotations__,  __author__ 

from .gooogle_generativeai import GoogleGenerativeAI
from .openai import OpenAIModel