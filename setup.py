from setuptools import setup
import sys

version = '0.1.2'
install_requires = []

if sys.version_info < (3, 4):
    install_requires.append('enum34')

setup(name='beautifultable',
      version=_version,
      description='Utility package to print visually appealing ASCII tables to terminal',
      install_requires=install_requires,
      long_description=open('README.rst', 'rt').read(),
      author='Priyam Singh',
      author_email='priyamsingh.22296@gmail.com',
      packages=['beautifultable'],
      url='https://github.com/pri22296/beautifultable',
      download_url='https://github.com/pri22296/beautifultable/tarball/{}'.format(_version),
      keywords='table terminal ascii',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Topic :: Printing',
          'Topic :: Text Processing',
      ],
)
