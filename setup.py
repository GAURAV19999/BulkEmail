from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='bulk-email',
   version='1.0',
   description='Bulk Email Automation',
   license="MIT",
   long_description=long_description,
   author='Sisay Chala',
   author_email='sisayie@gmail.com',
   url="https://github.com/sisayie/BulkEmail",
   packages=['bulk-email'],
   install_requires=['smtplib', 'ssl'], #external packages as dependencies
)