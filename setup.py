from setuptools import setup, find_packages

setup(

    name='MYPACKAGE',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    licence='MIT',
    description='EDSA example python package',
    long_description =open('readme.MD').read(),
    install_requires = ['numpy'],
    url= 'https://github.com/<NAHHARM>/MYPACKAGE>',
    author='<LENOVO>',
    author_email='<nahhar1993@gmail.com>'

)