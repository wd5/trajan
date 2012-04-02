from setuptools import setup, find_packages

version = '0.4dev'

setup(name='trajan',
      version=version,
      description="CMS-tivus for the REST-ivus",
      long_description=open("README.md", "r").read(),
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Web Environment",
          "Framework :: Django",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='CMS, Django, Blog',
      author='Derek Stegelman',
      author_email='dstegelman@gmail.com',
      url='http://github.com/dstegelman/trajan',
      license='MIT',
      packages=find_packages(),
      install_requires = ['django', 'south', 'sorl-thumbnail', 'django-tastypie'],
      include_package_data=True,
      zip_safe=False,
    )