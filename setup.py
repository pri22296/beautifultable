import os

from setuptools import setup
from codecs import open


extras_require = {':python_version<"3.4"': ['enum34']}

this_dir = os.path.abspath(os.path.dirname(__file__))
version_path = os.path.join(this_dir, 'beautifultable', '__version__.py')

about = {}
with open(version_path, 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

download_url = '{}/tarball/{}'.format(about['__url__'],
                                      about['__version__'])

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=['beautifultable'],
    url=about['__url__'],
    download_url=download_url,
    license=about['__license__'],
    keywords='table terminal ascii',
    extras_require=extras_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Printing',
        'Topic :: Text Processing',
    ],
)
