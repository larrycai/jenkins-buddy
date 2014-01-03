#!/usr/bin/env python
# Copyright (C) 2012 OpenStack Foundation
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

import argparse
import ConfigParser
import logging
import os
import sys

def confirm(question):
    answer = raw_input('%s (Y/N): ' % question).upper().strip()
    if not answer == 'Y':
        sys.exit('Aborted')


def main():
    import jenkins_jobs.builder
    import jenkins_buddy.builder
    import jenkins_jobs.errors
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(help='update or delete views/slave nodes',
                                      dest='command')
    parser_update = subparser.add_parser('update-view')
    parser_update.add_argument('path', help='Path to YAML file')
    parser_update.add_argument('--delete-old', help='Delete obsolete jobs',
                               action='store_true',
                               dest='delete_old', default=False,)
    parser_delete = subparser.add_parser('delete-view')
    parser_delete.add_argument('path', help='Path to YAML file')
    parser.add_argument('-c','--conf', dest='conf', help='Configuration file')
    parser.add_argument('-l', '--log_level', dest='log_level', default='info',
                        help="Log level (default: %(default)s)")
    options = parser.parse_args()

    options.log_level = getattr(logging, options.log_level.upper(),
                                logging.INFO)
    logging.basicConfig(level=options.log_level)
    logger = logging.getLogger()

    conf = '/etc/jenkins_jobs/jenkins_jobs.ini'
    if options.conf:
        conf = options.conf
    else:
        # Fallback to script directory
        localconf = os.path.join(os.path.dirname(__file__),
                                 'jenkins_jobs.ini')
        if os.path.isfile(localconf):
            conf = localconf

    config = ConfigParser.ConfigParser()
    if os.path.isfile(conf):
        logger.debug("Reading config from {0}".format(conf))
        conffp = open(conf, 'r')
        config.readfp(conffp)
    # elif options.command == 'test':
    #     ## to avoid the 'no section' and 'no option' errors when testing
    #     config.add_section("jenkins")
    #     config.set("jenkins", "url", "http://localhost:8080")
    #     config.set("jenkins", "user", None)
    #     config.set("jenkins", "password", None)
    #     config.set("jenkins", "ignore_cache", False)
    #     logger.debug("Not reading config for test output generation")
    else:
        raise jenkins_jobs.errors.JenkinsJobsException(
            "A valid configuration file is required when not run as a test")

    logger.debug("Config: {0}".format(config))

    builder = jenkins_buddy.builder.Builder(config.get('jenkins', 'url'),
                                           config.get('jenkins', 'user'),
                                           config.get('jenkins', 'password'))

    if options.command == "update-view":
        builder.update_view(options.path)
    elif  options.command == "delete-view":
        builder.delete_view(options.path)



if __name__ == '__main__':
    sys.path.insert(0, '.')
    main()