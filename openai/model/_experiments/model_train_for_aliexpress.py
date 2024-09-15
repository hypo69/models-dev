## \file ../src/ai/openai/model/_experiments/model_train_for_aliexpress.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header 

from src.settings import gs
from src.ai import OpenAIModel, GoogleGenerativeAI
from src.utils.file import recursive_get_filenames, read_text_file
from src.utils.convertor import csv2json_csv2dict
from src.utils import pprint

product_titles_files:list = recursive_get_filenames(gs.path.data / 'aliexpress' / 'campaigns','product_titles.txt')
system_instruction_path = gs.path.src / 'ai' / 'prompts' / 'aliexpress_campaign' / 'system_instruction.txt'
system_instruction: str = read_text_file(system_instruction_path)
openai = OpenAIModel(system_instruction = system_instruction)
gemini = GoogleGenerativeAI(system_instruction = system_instruction)
for file in product_titles_files:
    ...
    product_titles = read_text_file(file)
    response_openai = openai.ask(product_titles)
    response_gemini = gemini.ask(product_titles)
    ...

...