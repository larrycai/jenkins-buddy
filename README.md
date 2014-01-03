## jenkins-buddy ##

Jenkins buddy to create jenkins easily, require [jenkins-job-builder](http://ci.openstack.org/jenkins-job-builder/)

## How to install ##
 
	$ pip install https://github.com/larrycai/jenkins-buddy/zipball/master
	# or build and install locally
	$ python setup.py sdist ; pip install dist/jenkins-buddy-0.0.5.zip
	# or later
	$ pip install jenkins-buddy (not ready)	
	
## Features ##

Planned to support more modules (a.k.a jenkins plugins) which are not supported as default and create view/slave nodes 

### Some new modules ###

#### ArtifactDeployer Plugin ####

[ArtifactDeployer Plugin](https://wiki.jenkins-ci.org/display/JENKINS/ArtifactDeployer+Plugin) is the popular plugin to deploy the artifacts to other folder

`.YAML` format

    publishers:
      - artifactdeployer: 
          includes: 'buddy-*.tar.gz'
          remote: '/project/buddy'

    $ jenkins-job test job.yaml -o

#### Create View ####

The view can be automatically created/deleted now

Create views and add jobs into the view

    - views:
      name: product-abc-view
      jobs:
          - 'master-build-job'
          - 'master-deploy-job'
          - 'master-start-job'

	$ jenkins-buddy update-view view.yaml
	$ jenkins-buddy delete-view view.yaml

#### Create Slave Node ####

## Development ##

Debug it locally

	$ python setup.py sdist && pip uninstall -y jenkins-buddy ; pip install dist/jenkins-buddy-0.0.5.zip
	$ jenkins-jobs -l debug test job.yaml -o .

How to extend the modules: http://ci.openstack.org/jenkins-job-builder/extending.html#component-interface

### For view featurs ###

[jenkinsapi](https://github.com/salimfadhley/jenkinsapi/) is used instead of [python-jenkins](http://pythonhosted.org/python-jenkins/), since the latter doesn't has the API.