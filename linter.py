#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by 
# Copyright (c) 2017 
#
# License: MIT
#

"""This module exports the Solium plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Solium(NodeLinter):
    """Provides an interface to solium."""

    syntax = 'solidity'
    cmd = 'solium -R gcc --file @'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(?:(?P<warning>warning)|(?P<error>error))'
        r'(?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'solidity'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
    config_file = ('--config', '.soliumrc.json')
