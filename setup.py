from setuptools import setup, find_packages
import pkg

setup(
    name='pkg',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/cupen/pkg',
    license='MIT',
    author='cupen',
    author_email='cupen@foxmail.com',
    description='package manager wapper for humans.',

    entry_points={
        "console_scripts": [
            "pkg=pkg:main",
        ],
    },
)
