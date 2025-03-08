from setuptools import setup, find_packages

setup(
    name="putils",  
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django==3.2",
        "asgiref==3.7.2",
        "sqlparse==0.4.4",
        "tzdata==2025.1"
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
