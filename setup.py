from setuptools import setup, find_packages

setup(
    name="prtls_utils",  
    version="0.1.5",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django==3.2",
        "asgiref==3.7.2",
        "sqlparse==0.4.4",
        "pytz==2023.3"
    ],
)
