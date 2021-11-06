import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
fh.close()

setuptools.setup(
    name="phish-detector",
    version="1.0.0",
    author="ElijahGives",
    author_email="elijahgives13@gmail.com",
    description="A discord webhook client written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElijahGives/phish-detector",
    license="LICENSE",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
         "Operating System :: OS Independent",
     ],
    packages=["phish_detector"],
)