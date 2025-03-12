from setuptools import setup, find_packages

setup(
    name="prtls_utils",  
    version="0.2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django==4.2.20",
        "asgiref==3.7.2",
        "sqlparse==0.5.0",
        "pytz==2023.3"
    ],
)
