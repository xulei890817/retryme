from setuptools import setup
import RetryMe

version = RetryMe.__version__
url = "https://github.com/xulei890817/retryme"


def readme():
    with open("README.rst", "r") as infile:
        return infile.read()


setup(
    name='AutoRetry',
    version=version,
    packages=['RetryMe'],
    url='',
    license='',
    author='leixu',
    author_email='leixu@g'
                 '',
    description=''
)
