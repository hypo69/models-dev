"""! Темплейты даля создания новых сущностей (новый поставщик) 

@todo
    1. получить данные:
        - имя поставщика. Например, `aliexpress`
        - вебсайт поставщика. 
        - имя/пароль (если требуются для входа на сайт)
    1. создать диркторию поставщика в директории `src.suppliers`
обновить записи в престашоп и гугл таблице
"""
...
## \file ../src/ai/openai/bots/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from packaging.version import Version
from .version import __version__, __name__, __doc__, __details__, __annotations__,  __author__ 

from .discord_bot_trainger import *
from .chatterbox import recognizer, text_to_speech


