import os
from setuptools import setup,find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "jenkins-buddy",
    version = "0.0.5",
    author = "Larry Cai",
    author_email = "larry.cai@gmail.com",
    description = ("Jenkins buddy to create jenkins easily, require jenkins-job-builder"),
    license = "OSI",
    keywords = "jenkins, plugin",
    url = "http://github.com/larrycai/jenkins-buddy",
    packages=find_packages(),    
    long_description=read('README.md'),
    install_requires=["jenkins-job-builder>=0.6.0"],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    entry_points={
        'console_scripts': [
            'jenkins-buddy=jenkins_buddy.cmd:main', # this will be added for more
        ],
        'jenkins_jobs.publishers': [
            'artifactdeployer=jenkins_buddy.modules.publishers:artifactdeployer',
        ],
    }
)
