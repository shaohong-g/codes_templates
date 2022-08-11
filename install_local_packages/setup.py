from setuptools import setup, find_packages


# python -m pip install --upgrade setuptools
# pip install -e .
# pip install -U .

# https://github.com/pypa/sampleproject/blob/main/setup.py
# https://stackoverflow.com/questions/54430694/python-setup-py-how-to-get-find-packages-to-identify-packages-in-subdirectori
# https://stackoverflow.com/questions/24351441/including-nested-modules-in-setup-script

# https://jwodder.github.io/kbits/posts/pypkg-data/
# https://kiwidamien.github.io/making-a-python-package-vi-including-data-files.html
# https://stackoverflow.com/questions/58048482/how-to-access-data-files-specified-in-setup-py-during-runtime
# https://stackoverflow.com/questions/7522250/how-to-include-package-data-with-setuptools-distutils
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
    package_data={'': ['static/*.csv']},
    python_requires='>=3.4',
    install_requires=requirements
)