#!/bin/sh
perl -ne 'printf $1 if /version="([^"]*)"/' 00_header.rpy
