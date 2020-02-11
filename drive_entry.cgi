#!/usr/bin/env bash

# Variables
################################################################################
# Path to data file
readonly file_data='/var/www/html/drive_history/data.js'

# Get Parameter from URL Arguments
read -ra url_parameters
readonly url_parameters


# Functions
################################################################################
write_data() {
    # Parse date from url_parameters
    date=`grep -Po '\d{4}.\d{2}.\d{2}' <<< "$url_parameters"`
    echo "<date>$date</date>"

    if before=`grep --quiet "$date" $file_data`; then
        echo "<entry>changed</entry>"

        # Store data in dedicated file
	(sed "s|.*$date.*|    $url_parameters,|" -i $file_data || echo "Error while writing data with sed") &
    else
        echo "<entry>added</entry>"

        # Store data in dedicated file
        (sed "2i\    $url_parameters," -i $file_data || echo "Error while writing data with sed") &
    fi
}


check_url_parameters() {
    # Test if Arguments match Pattern to prevent Misuse
    grep --quiet --perl-regexp '^\{"date":"\d{4}-\d{2}-\d{2}",("\w+":-?\d+,?)*\}$' <<< $url_parameters \
      || { echo 'Error: Arguments do not match defined pattern. Aborting script to prevent misuse.'; exit; }
}


# Body (return some information to see if the POST request was successful)
################################################################################

echo '<response>'
echo "<url_parameters>$url_parameters</url_parameters>"
check_url_parameters
write_data
echo '</response>'
