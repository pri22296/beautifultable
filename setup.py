from setuptools import setup

setup(name='beautifultable',
      version='0.1.0',
      description='Utility package to print visually appealing ASCII tables to terminal',
      author='Priyam Singh',
      author_email='priyamsingh.22296@gmail.com',
      packages=['beautifultable'],
      url='https://github.com/pri22296/beautifultable',
      keywords='table terminal ascii',
      license='MIT',
      install_requires=[
          'enum34;python_version<"3.4"',
      ],
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
