import setuptools

setuptools.setup(
    name='sphinx-bootcamp',
    version='1.0.0',
    author='Ashley Trinh',
    author_email='ashley@hackbrightacademy.com',
    python_requires='>=3.6',
    packages=setuptools.find_packages(include=['sphinxbootcamp', 
                                               'sphinxbootcamp.*']),
)