from setuptools import setup, find_packages

setup(
    name="putils",  
    #version="0.1.0",
    version="0.1.1", # Matching the parent project version
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django==3.2",
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
