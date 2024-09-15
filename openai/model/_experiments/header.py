﻿"""! Модуль управления моделью OpenAI 
"""
## \file ../src/ai/openai/model/_experiments/header.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
ffmpeg: Path = Path( __root__ , 'bin' , 'ffmpeg' , 'bin' , 'ffmpeg.exe') 
sys.path.append (__root__)   
sys.path.append (ffmpeg)