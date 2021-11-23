from setuptools import setup, find_packages

setup(
    name='littlekv',
    version='1.0',
    description='A lightweight in-memory key-value store',
    url='https://github.com/J-Obog/littlekv',
    author='JObog',
    author_email='jobogbaimhe@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests', 'examples'])
)