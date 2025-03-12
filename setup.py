from setuptools import setup, find_packages

setup(
    name="prtls_utils",  
    use_scm_version=True, 
    setup_requires=["setuptools_scm"],
    author="Michael Britton",
    author_email="michael.britton@protellus.ca",
    packages=["prtls_utils"],
    install_requires=[
        "django>=5.1.7",
        "asgiref==3.8.1",
        "sqlparse==0.5.3",
        "pytz==2023.3",
        "tzdata==2025.1",
    ],
)