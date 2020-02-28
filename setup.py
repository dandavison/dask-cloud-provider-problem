from setuptools import find_packages
from setuptools import setup


setup(
    name="dask-cloudprovider-problem",
    author="Dan Davison",
    author_email="dandavison7@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
