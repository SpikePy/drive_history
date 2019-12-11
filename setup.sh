#!/usr/bin/env sh
(
    cd `dirname $0`

    ln -s driving_history.html /var/www/html/index.html
    ln -s add_drive.cgi        /var/www/cgi-bin/
)
