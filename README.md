SublimeLinter-contrib-solium
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-solium.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-solium)

This linter plugin for [SublimeLinter][docs] provides an interface to [solium](https://github.com/duaraghav8/Solium). It will be used with files that have the [“solidity” syntax](https://packagecontrol.io/packages/Ethereum).

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `solium` is installed on your system. To install `solium`, do the following:

1. Install [Sublime Ethereum Package](https://packagecontrol.io/packages/Ethereum) from package control, for solidity syntax highlighting:
1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).
1. Install [solium](https://github.com/duaraghav8/Solium) by typing the following in a terminal:
   ```
   npm install -g solium
   ```
1. In the root directory of your DApp, run the following:
   ```
   solium --init
   ```

**Note:** This plugin requires `solium` 0.2.2 or later.

### Linter configuration
In order for `solium` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `solium`, you can proceed to install the SublimeLinter-contrib-solium plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `add repository`. Among the commands you should see `Package Control: Add repository`, select it.
2. Paste in the URL of this repo, without the `.git` suffix: https://github.com/alexstep/SublimeLinter-contrib-solium

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
