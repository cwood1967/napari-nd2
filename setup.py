#!/usr/bin/env python
import codecs
import os
from setuptools import setup

def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()

setup(
    name="napari-nd2",
    version="0.0.1",
    author="Chris Wood",
    author_email="cjw@stowers.org",
    maintainer="Chris Wood",
    maintainer_email="cjw@stowers.org",
    description="Open Nikon ND2 files in napari",
    long_description=read("README.rst"),
    python_requires=">=3.6",
    license="MIT",
    py_modules=['napari_nd2_plugin'],
    entry_points={
        "napari.plugin": [
            "nd2reader = napari_nd2_plugin",
        ],
    },
)