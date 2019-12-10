#!/usr/bin/env sh
(
    cd `dirname $0`

    ln add_drive.cgi /var/www/cgi-bin/
    ln analyze.cgi /var/www/cgi-bin/

    ln driving_history.html /var/www/html/
    ln driving_history.js /var/www/html/
    ln log.html /var/www/html/
)
