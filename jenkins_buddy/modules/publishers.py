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


"""
Publishers define actions that the Jenkins job should perform after
the build is complete.

**Component**: publishers
  :Macro: publisher
  :Entry Point: jenkins_jobs.publishers
"""


import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base
from jenkins_jobs.errors import JenkinsJobsException
import logging
import sys
import random

# <org.jenkinsci.plugins.artifactdeployer.ArtifactDeployerPublisher plugin="artifactdeployer@0.27">
#    <entries>
#      <org.jenkinsci.plugins.artifactdeployer.ArtifactDeployerEntry>
#        <includes>coco-*.tar.gz</includes>
#        <basedir></basedir>
#        <excludes></excludes>
#        <remote>/project/ecds/ccenv/www/htdocs/repo/eta/infra/coco/redhat</remote>
#        <flatten>false</flatten>
#        <deleteRemote>false</deleteRemote>
#        <deleteRemoteArtifacts>false</deleteRemoteArtifacts>
#        <deleteRemoteArtifactsByScript>false</deleteRemoteArtifactsByScript>
#        <failNoFilesDeploy>false</failNoFilesDeploy>
#      </org.jenkinsci.plugins.artifactdeployer.ArtifactDeployerEntry>
#    </entries>
#    <deployEvenBuildFail>false</deployEvenBuildFail>
#  </org.jenkinsci.plugins.artifactdeployer.ArtifactDeployerPublisher>
def artifactdeployer(parser, xml_parent, data):
    """yaml: archive
    Archive build artifacts

    :arg str artifacts: path specifier for artifacts to archive
    :arg str excludes: path specifier for artifacts to exclude
    :arg bool latest-only: only keep the artifacts from the latest
      successful build

    Example::

      publishers:
        - archive:
            artifacts: '*.tar.gz'
    """
    logger = logging.getLogger("%s:artifactdeployer" % __name__)
    artifactdeployer = XML.SubElement(xml_parent, 'org.jenkinsci.plugins.artifactdeployer.ArtifactDeployerPublisher')
    entries = XML.SubElement(artifactdeployer, 'entries')
    entry = XML.SubElement(entries, 'org.jenkinsci.plugins.artifactdeployer.ArtifactDeployerEntry')
    print data
    XML.SubElement(entry, 'includes').text = data['includes']
    XML.SubElement(entry, 'remote').text = data['remote']
    #XML.SubElement(entry, 'includes').text = data['includes']
    
