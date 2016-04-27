from setuptools import setup

__version__ = '2.1.0'

setup(
    name='pytify',
    version=__version__,
    description='Spotify Remote. Search, start and navigate through songs.',
    long_description=open('README.rst').read(),
    url='https://github.com/AustinRF2918/pytify',
    author='Austin Fell (Orignal Creator)-> Bjarne Oeverli',
    author_email='AustinRF2918@yahoo.com (Original Author)bjarne.oeverli@gmail.com',
    license='MIT',
    keywords='spotify pytify spotty song search curses',
    packages=['pytify'],
    install_requires=['requests'],
    entry_points={'console_scripts': ['spotty=pytify.cli:main']},
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console :: Curses',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Terminals',
        ],
)
