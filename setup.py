from setuptools import setup, find_packages
import os
import re

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'coffeepot', 'vars.py')) as f:
    VERSION = re.search(r'VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', f.read()).group(1)

setup(
    name='coffeepot-http',
    version=VERSION,
    description='A cozy Python server and module for brewing coffee virtually',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Hollo',
    author_email='hollo1234567890e@gmail.com',
    url='https://github.com/DevHollo/CoffeePot',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'coffeepot=coffeepot.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
