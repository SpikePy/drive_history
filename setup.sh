#!/usr/bin/env sh
(
    cd `dirname $0`

    ln -s driving_history.html    /var/www/html/index.html
    ln -s driving_history_data.js /var/www/html/driving_history_data.js
    ln -s add_entry.cgi           /var/www/cgi-bin/
)
