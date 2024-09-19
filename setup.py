from setuptools import setup

setup(
    name='mlflow',
    version='0.0.1',
    description='Folk project from mlflow with disabled ssl settings',
    url='git@github.com:fjn-rdcenter/mlflow-no-ssl.git',
    author='FJN',
    author_email='son-tm@fujinet.net',
    license='MIT',
    packages=['mlflow'],
    zip_safe=False
)