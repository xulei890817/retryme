#!/usr/bin/env python

# encoding: utf-8

'''
 * Create File logger
 * Created by leixu on 2018/4/23
 * IDE PyCharm
'''

import logging
import sys

import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
