from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package",
    version="1.0.0",
    author="Wesley Maik",
    author_email="wesleynamikaze404@gmail.com",
    description="Image processing by Unimed-BH Data Science Bootcamp by Digital Innovation One Inc.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WesleyMaik/bootcamp-data-science-unimed/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)