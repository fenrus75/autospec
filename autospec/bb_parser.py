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

import re


def scrape_version(f):
    # remove name_ from beginning and .ext from end
    return f.split('_', 1,)[1].rsplit('.', 1)[0]


def replace_pv(bb_dict):
    for k, v in bb_dict.items():
        if "${PV}" in v:
            bb_dict[k] = v.replace("${PV}", bb_dict.get('version'))


def update_inherit(line, bb_dict):
    if 'inherits' in bb_dict:
        bb_dict['inherits'].append(' '.join(line.split(' ', 1)[1:]))
    else:
        bb_dict['inherits'] = line.split(' ', 1)[1:]


def clean_values(value):
    # remove beginning and end quote
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]

    return value


def read_in_command(line, depth, buf):
    for c in line:
        if c == '{':
            depth += 1
        if c == '}' and depth > 0:
            depth -= 1
        if c != "\n":
            buf += c
    return buf, depth


def pattern_match_line(line):

    expr = ["??=", "?=", ":=", "+=",
            "=+", ".=", "=.", "="]

    for i, e in enumerate(expr):
        expr[i] = '\\' + '\\'.join(e)

    # Split line to be [Key, expression, value] if in expr list
    expr_pattern = r"(^[A-Z]+[_${}\[\]A-Za-z]*)\s(" + '|'.join(
        expr) + r")\s(\".*\")"

    return re.compile(expr_pattern).search(line)


def write_to_dict(bb_dict, m):

    if len(m.groups()) == 3:
        key = m.group(1)
        value = clean_values(m.group(3))
        expr = m.group(2)

        if key in bb_dict:
            print("TODO: ERROR")

        if expr == '=':
            bb_dict[key] = value

    return bb_dict


def bb_scraper(bb, specfile):

    bb_dict = {}
    todo = []
    bb_dict['version'] = scrape_version(bb)

    with open(bb, 'r') as bb_fp:
        cont = None
        for line in bb_fp:
            # do not parse empty strings and comments
            if line.strip() and not line.strip().startswith('#'):
                line = line.strip()

                # if line is a continuation, append to single line
                if not cont and line[-1] == '\\':
                    cont = ""
                    while 1:
                        cont += line
                        line = next(bb_fp).strip('\n')
                        if line[-1] != '\\':
                            cont += line
                            break

                    line = cont
                    cont = None

                # otherwise if line is a command, create raw string of command
                # TODO: command could be python code
                elif not cont and line.startswith('do_'):
                    cmd_name = line.split('()')[0]
                    cont = ""
                    depth = 0
                    count = 0
                    while 1:
                        count += 1
                        cont, depth = read_in_command(line, depth, cont)
                        if depth == 0:
                            break
                        else:
                            line = next(bb_fp)

                    line = cont
                    cont = None

                if line.startswith('inherit'):
                    update_inherit(line, bb_dict)

                match = pattern_match_line(line)
                if match:
                    bb_dict = write_to_dict(bb_dict, match)
                else:
                    todo.append(line)

    return bb_dict
