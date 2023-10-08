from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="KD_Classification",
    version="1.0.0",
    author="dibyendubiswas1998",
    author_email="dibyendubiswas1998@gmail.com",
    description="Kidney Disease Classification Web App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dibyendubiswas1998/Kidney-Disease-Classification.git",
    packages=["src"],
    license="GNU",
    python_requires=">=3.8",
    # install_requires=[
    #     'pandas',
    #     'scikit-learn',
    #     'nltk',
    #     'tensorflow',
    # ]
)
