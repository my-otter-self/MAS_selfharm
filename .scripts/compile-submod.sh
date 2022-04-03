#!/bin/sh
mkdir -p "ddlc-mas/game/mshMod"
find -not \( -path "./renpy" -prune -o -path "./ddlc-mas" -prune \) -iname "*.rpy" -exec cp --parents \{\} "ddlc-mas/game/mshMod" \;
renpy/renpy.sh "ddlc-mas" compile 2>&1 | tee compile.log | perl -ne 'print if (/^game\/mshMod[^\s]*: \w*Warning/ || !/^game\//)'
if grep -Eq '^.*Error:.*$|^File ".*", line .*:.*$' compile.log; then exit 1; fi
find "ddlc-mas/game/mshMod" -type f -not -iname "*.rpyc" -delete
mkdir -p "game/Submods"
mv "ddlc-mas/game/mshMod" "game/Submods/$(perl -ne 'printf $1 if /name="([^"]*)"/' "00_header.rpy")"
