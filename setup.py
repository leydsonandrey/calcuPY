from setuptools import setup

setup(
    name = 'calcupy',
    version = '0.1.1',
    author='Andrey Duarte',
    author_email='sureandrey@gmail.com',
    url='https://github.com/SureAndrey/calculadora-python',
    packages = ['extension'],
    entry_points = {
        'console_scripts': [
            'calcupy = extension.__main__:main'
        ]
    }
)
