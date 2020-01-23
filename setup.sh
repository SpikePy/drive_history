#!/usr/bin/env bash
(
    cd `dirname $0`

    ln -s $PWD                      /var/www/html/${PWD##*/}
    ln -s $PWD/drive_entry.cgi      /var/www/cgi-bin/
)
