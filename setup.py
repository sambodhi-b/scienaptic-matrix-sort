from setuptools import setup, find_packages

requirements = [
    'numpy',
]

dev_requirements = [
    'wheel',
    'pytest',
]

setup(
    name='ScMatSort',
    version='0.1',
    author='Sambodhi Bhattacharyya',
    author_email='sambodhi.b@gmail.com',
    packages=find_packages('src'),
    package_dir={"": "src",},
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements,
        'jedi': ['jedi'],
    },
)
