from setuptools import setup, find_packages

setup(
    name='statgames',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'scipy>=0.15.0',  # Minimum version required for scipy.special.comb with exact=True
    ],
    url='https://github.com/Konczer/UncertaintyTheory/tree/main/StatisticalGames/Software/Python/statgames',
    author='Jozsef Konczer',
    author_email='konczer.j@gmail.com',
    description='A package for calculating equilibrium quantities for Fisher, Bayesian, and Statistical Games',
)
