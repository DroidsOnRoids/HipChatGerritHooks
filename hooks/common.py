#!/usr/bin/env python3

import argparse
import configparser
import json
import os
import urllib.error
import urllib.request
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project')
    parser.add_argument('--author')
    parser.add_argument('--is-draft', dest='isDraft')
    parser.add_argument('--Verified', dest='verifiedScore')
    parser.add_argument('--Code-Review', dest='codeReviewScore')
    parser.add_argument('--change-url', dest='changeUrl')
    parser.add_argument('--change-owner', dest='changeOwner')
    parser.add_argument('--change', dest='changeId')
    parser.add_argument('--reviewer')
    return parser.parse_known_args()


def parse_config(hook_name):
    section = os.path.basename(hook_name)
    config = configparser.ConfigParser()
    config.read(os.getenv('GERRIT_SITE') + '/etc/hipchat.config')
    section_config = config[section] if config.has_section(section) else {}
    return config['general']['auth_token'], section_config


def perform_request(url, message, success_log_message, color=None):
    data = {'message': message, 'notify': True, 'message_format': 'text', 'color': color}
    params = json.dumps(data).encode('utf8')
    request = urllib.request.Request(url, data=params, headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(request)
        print(success_log_message)
    except urllib.error.HTTPError as e:
        print(e.read())


def is_email_matching(regex, email_address):
    return re.match(regex, email_address) is not None

