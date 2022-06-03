#!/bin/sh

_mod_dir="game/Submods/$(perl -ne 'if (/name="([^"]*)"/) { print $1; exit }' "mod/00_header.rpy")"

# Clear MAS logs
if [ -d build/ddlc/log ]; then
    find build/ddlc/log -type f -iname '*.log' -delete
fi

# Copy .rpy files from mod folder
mkdir -p "build/ddlc/$_mod_dir"
(cd mod; find . -iname '*.rpy' -not -iname '00_source_dist_trap.rpy' -exec cp -r --parents \{\} "../build/ddlc/$_mod_dir" \;)

# Move spritepacks into their respective locations
find spritepacks -mindepth 2 -maxdepth 2 -type d -exec cp -RT \{\} build/ddlc \;

# Move resources into submod folder
(cd res; find . -exec cp -r --parents \{\} "../build/ddlc/$_mod_dir" \;)

# Run build and join build output and spj.log together
build/renpy/renpy.sh build/ddlc compile 2>&1 \
    | tee build/compile.log \
    | perl -ne 'print if (/^game\/mshMod[^\s]*: \w*Warning/ || !/^game\//)' \
    | sed 's/game\/mshMod\///g'
perl -ne 'print if (/^.*!ERROR! T_T.*$/)' build/ddlc/log/spj.log \
    | tee -a build/compile.log

# Scan for errors in log
if grep -Eq '^.*Error:.*$|^File ".*", line .*:.*$' build/compile.log; then exit 1; fi
if tail -n +9 build/ddlc/log/spj.log | grep -Eq '^.*!ERROR! T_T.*$'; then exit 1; fi

find "build/ddlc/$_mod_dir" -type f -iname '*.rpyc' -delete

# Move compiled files to build/out
mkdir -p "build/out/game/Submods"
mv "build/ddlc/$_mod_dir" "build/out/game/Submods"

# Remove submod and spritepack files from build directory
find spritepacks -mindepth 2 -type f -exec sh -c 'rm "build/ddlc/$(echo "$0" | sed -nE '"'s/^.*\/((game|characters)\/.*)/\1/p'"')"' \{\} \;
