import setuptools

setuptools.setup(
    name="sphinx-lectern",
    version="1.0.0",
    author="Ashley Trinh",
    author_email="ashley@hackbrightacademy.com",
    url="https://github.com/bootcampgang/sphinx-lectern",
    python_requires=">=3.6",
    packages=setuptools.find_packages(include=["sphinxlectern", "sphinxlectern.*"]),
    include_package_data=True,
    entry_points={
        "sphinx.html_themes": [
            "revealjs = sphinxlectern.themes",
            "handouts = sphinxlectern.themes",
        ]
    },
)
