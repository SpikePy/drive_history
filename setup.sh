#!/usr/bin/env sh
(
    cd `dirname $0`

    ln -s driving_history.html /var/www/html/
    ln -s add_drive.cgi /var/www/cgi-bin/
    #ln analyze.cgi /var/www/cgi-bin/
)
