#!/bin/sh
# Since this is essentially a compat package, we have to
# filter out current releases (which are packaged in wesnoth-unstable)
git ls-remote --tags https://github.com/wesnoth/wesnoth 2>/dev/null|awk '{ print $2; }' |sed -e 's,refs/tags/,,;s,_,.,g' |grep -v '\^{}' |grep '1\.1[68]' |sort -V |tail -n1
