from setuptools import setup, find_packages

setup(
    name='beam_learning_resources',
    version='0.1',
    description='Example Apache Beam Python pipeline',
    author='sunny',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'apache-beam[gcp]==2.68.0',
    ],
    include_package_data=True,
)