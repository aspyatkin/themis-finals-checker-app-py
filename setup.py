# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import os


about = {}
about_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'themis', 'finals', 'checker', 'app', '__about__.py')
with io.open(about_filename, 'rb') as fp:
    exec(fp.read(), about)


setup(
    name='themis.finals.checker.app',
    version=about['__version__'],
    description='Themis Finals checker application',
    author='Alexander Pyatkin',
    author_email='aspyatkin@gmail.com',
    url='https://github.com/themis-project/themis-finals-checker-app-py',
    license='MIT',
    packages=find_packages('.'),
    install_requires=[
        'setuptools>=0.8',
        'Flask>=0.11.1,<0.12',
        'redis>=2.10.5,<2.11',
        'hiredis>=0.2.0,<0.3',
        'rq>=0.6.0,<0.7',
        'requests>=2.11.0',
        'python-dateutil>=2.5.3,<2.6',
        'themis.finals.api.auth==1.0.0',
        'themis.finals.checker.result==1.0.0',
        'raven>=5.26.0,<5.27.0',
        'PyJWT>=1.5.0,<1.6.0',
        'cryptography>=1.8.1,<1.9.0',
        'PyYAML>=3.11'
    ],
    namespace_packages=[
        'themis',
        'themis.finals',
        'themis.finals.checker'
    ],
    entry_points=dict(
        console_scripts=[
            'themis-finals-checker-app-worker = themis.finals.checker.app:start_worker'
        ]
    )
)
