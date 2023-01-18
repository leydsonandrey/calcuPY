from setuptools import setup
setup(
    name = 'calcupy',
    version = '0.1.1',
    packages = ['extension'],
    entry_points = {
        'console_scripts': [
            'calcupy = extension.__main__:main'
        ]
    })
