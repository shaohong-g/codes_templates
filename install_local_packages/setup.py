from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="TestPackage", # Replace with your username
    version="1.0.0",
    author="Gan Shao Hong",
    author_email="shaohong.g97@gmail.com",
    description="Testing package installation",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="<https://github.com/authorname/templatepackage>",
    packages=['TestPackage'], #find_packages(),
    package_dir={'TestPackage': './TestPackage'},
    classifiers=[
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    # package_data={'': ['static/*.csv']}, # Use either this or include_package_data (reference by MANIFEST.in) (dir is relative to package)
    python_requires='>=3.4',
    install_requires=requirements
)