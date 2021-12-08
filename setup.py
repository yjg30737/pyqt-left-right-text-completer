from setuptools import setup, find_packages

setup(
    name='pyqt-left-right-text-completer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Left text, right text Completer. Left text is major target of search.',
    url='https://github.com/yjg30737/pyqt-left-right-text-completer.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)