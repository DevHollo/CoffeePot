from setuptools import setup, find_packages
from .vars import VERSION

setup(
    name='coffeepot',
    version=VERSION,
    description='A cozy Python server and module for brewing coffee virtually',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='hollo1234567890e@gmail.com',
    url='https://github.com/DevHollo/coffeepot',
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