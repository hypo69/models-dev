"""! OpenAI """

## \file ../src/ai/openai/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


from packaging.version import Version
from .version import __version__,  __doc__, __details__

from .translator import translate
from .model import OpenAIModel

