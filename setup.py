import os
import codecs
import itertools

from setuptools import setup

install_requires = ["wcwidth"]

extras_require = {
    "dev": ["pandas"],
}

extras_require["all"] = list(
    set(itertools.chain.from_iterable(extras_require.values()))
)

this_dir = os.path.abspath(os.path.dirname(__file__))
version_path = os.path.join(this_dir, "beautifultable", "__version__.py")

about = {}
with codecs.open(version_path, "r", "utf-8") as f:
    exec(f.read(), about)

with codecs.open("README.rst", "r", "utf-8") as f:
    readme = f.read()

download_url = "{}/tarball/{}".format(about["__url__"], about["__version__"])

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=["beautifultable"],
    url=about["__url__"],
    download_url=download_url,
    license=about["__license__"],
    keywords="table terminal ascii",
    extras_require=extras_require,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Printing",
        "Topic :: Text Processing",
    ],
)
