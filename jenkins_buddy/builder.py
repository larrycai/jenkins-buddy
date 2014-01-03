#!/usr/bin/env python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# https://github.com/salimfadhley/jenkinsapi

from jenkinsapi.view import View
from jenkinsapi.jenkins import Jenkins
import yaml

import logging
logger = logging.getLogger(__name__)

class Builder(object):
    def __init__(self, jenkins_url, jenkins_user, jenkins_password,
                 config=None, ignore_cache=False, flush_cache=False):
        self.jenkins = Jenkins(jenkins_url, jenkins_user, jenkins_password)
        self.views = self.jenkins.views

    def _loadYAML(self,yamlfile):
        data = yaml.load(open(yamlfile))
        self.view_data = {}
        if data:
            for item in data:
            	if item.keys()[0] == 'views':
            		self.view_data = item["views"]
        else:
        	logger.error("invalid YAML file {0}".format(yamlfile))

    def update_view(self,yamlfile):
    	self._loadYAML(yamlfile)

        view_name = self.view_data["name"]
        #view_type = view["type"]
        jobs = self.view_data["jobs"]
        logger.info('Attempting to create new view %s' % view_name)

        new_view = self.views[view_name]
        if new_view == None:
        	new_view = self.views.create(view_name)
        	if new_view is None:
        		logger.error('View was not created')
        		return
        	else:
        		logger.debug('View has been created')
        else:
        	logger.warning("the view %s already exist" % view_name)

        for job in jobs:
        	logger.info("adding job {0} into view {1}".format(job,view_name))
        	if self.jenkins.has_job(job):
        		new_view.add_job(job)
        	else:
        		logger.warning("can't find job {0}, skipped".format(job))

    def delete_view(self,yamlfile):
    	self._loadYAML(yamlfile)

    	view_name = self.view_data["name"]
    	del self.views[view_name]
    	if self.views[view_name] == None:
    		logger.info("view is deleted")
