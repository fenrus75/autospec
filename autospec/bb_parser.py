#!/usr/bin/true
#
# tarball.py - part of autospec
# Copyright (C) 2015 Intel Corporation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import re
from pprint import pprint

bb_dict = {}


def scrape_version(f):
    # remove name_ from beginning and .ext from end
    return f.split('_', 1,)[1].rsplit('.', 1)[0]


def replace_pv(bb_dict):
    for k,v in bb_dict.items():
        if "${PV}" in v:
            bb_dict[k] = v.replace("${PV}", bb_dict.get('version'))


def update_inherit(line, bb_dict):
    if 'inherits' in bb_dict:
       bb_dict['inherits'].append(' '.join(line.split(' ', 1)[1:]))
    else:
       bb_dict['inherits'] = line.split(' ', 1)[1:]


def bb_scraper(bb, specfile):

    global bb_dict

    print(bb)

    bb_dict['version'] = scrape_version(bb)

    expr = ["??=", "?=", ":=", "+=", 
            "=+", ".=", "=.", "="]
