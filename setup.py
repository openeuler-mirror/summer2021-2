import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nm",
    version="1.0",
    author="nm",
    description="Nm is a system monitor, and it will send out alarm information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "PyQt5",
        "PyYAML",
    ],
    entry_points={
        'console_scripts': ['nm-config=nmfront.main:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.7',
)
