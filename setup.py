import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("mindustry_launcher/_version.py", encoding="utf-8") as f:
    exec(f.read())

setuptools.setup(
    name="mindustry_launcher",
    version=__version__,
    author="albi-c",
    description="mindustry launcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albi-c/mindustry_launcher",
    project_urls={
        "Bug Tracker": "https://github.com/albi-c/mindustry_launcher/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)
