# jenkins-buddy #

Jenkins buddy to create jenkins easily, require jenkins-job-builder


## Development ##

Debug it locally

	python setup.py sdist && pip uninstall -y jenkins-buddy ; pip install dist/jenkins-buddy-0.0.5.zip
	jenkins-jobs -l debug test job.yaml -o .