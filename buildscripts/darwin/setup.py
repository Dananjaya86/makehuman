"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app

! cd ./buildscripts/darwin before building !
"""


import os
import shutil
from setuptools import setup
import urllib.request
from zipfile import ZipFile

OPENGL_URL = 'http://download.tuxfamily.org/makehuman/build/macos-opengl-wrapper.zip'

DEPENDENCIES = [
'pip',
'cProfile',
'pstats'
]

APP = ['../../makehuman/makehuman.py']
DATA_FILES = ['../../makehuman']
OPTIONS = {'packages': DEPENDENCIES, 'includes': DEPENDENCIES,'iconfile': 'makehuman.icns'}

setup(
    app=APP,
    name='MakeHuman',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

os.mkdir('temp');

print('Downloading OpenGL...');
urllib.request.urlretrieve(OPENGL_URL, './temp/OpenGL-packed.zip');

print('Unpacking OpenGL...');
with ZipFile('./temp/OpenGL-packed.zip', 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall('temp')

print('Copying OpenGL...');
shutil.copytree('./temp/OpenGL', './dist/makehuman.app/Contents/Resources/lib/OpenGL');

print('Cleaning environment...');
shutil.rmtree('build')
shutil.rmtree('temp')

print('Done!');