## jenkins-buddy ##

Jenkins buddy to create jenkins easily, require [jenkins-job-builder](http://ci.openstack.org/jenkins-job-builder/)

## How to install ##
 
	$ pip install https://github.com/larrycai/jenkins-buddy/zipball/master
	# or build and install locally
	$ python setup.py sdist ; pip install dist/jenkins-buddy-0.0.5.zip
	# or later
	$ pip install jenkins-buddy (not ready)	
	
### Features ###

Planned to support more modules (a.k.a jenkins plugins) which are not supported as default and create view/slave nodes 

#### Some new modules ####

* [ArtifactDeployer Plugin](https://wiki.jenkins-ci.org/display/JENKINS/ArtifactDeployer+Plugin)

    publishers:
      - artifactdeployer: 
          includes: 'buddy-*.tar.gz'
          remote: '/project/buddy'

#### Create View ####

#### Create Slave Node ####

## Development ##

Debug it locally

	$ python setup.py sdist && pip uninstall -y jenkins-buddy ; pip install dist/jenkins-buddy-0.0.5.zip
	$ jenkins-jobs -l debug test job.yaml -o .

How to extend the modules: http://ci.openstack.org/jenkins-job-builder/extending.html#component-interface