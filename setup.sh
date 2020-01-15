#!/usr/bin/env sh
(
    cd `dirname $0`

    ln -s driving_history.html /var/www/html/index.html
    ln -s add_entry.cgi        /var/www/cgi-bin/
)
