import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()

setuptools.setup(
    name="GraphForce",
    version="0.0.1",
    author="colorful-lollipop",
    author_email="colorful-lollipop@proton.me",
    description="A Knowledge Graph Construction Framework",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/colorful-lollipop/GraphForce",
    platforms="any",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
)
