#!/usr/bin/env bash

# Variables
################################################################################
# Path to data file
readonly file_data='/var/www/html/drive_history/data.js'

# Get Parameter from URL Arguments
read -ra data
readonly data


# Functions
################################################################################
write_data() {
    # Parse date from data
    date=`grep -Po '\d{4}.\d{2}.\d{2}' <<< "$data"`
    echo "<date>$date</date>"

    if before=`grep --quiet "$date" $file_data`; then
        echo "<entry>changed</entry>"

        # Store data in dedicated file
	(sed "s|.*$date.*|    $data,|" -i $file_data || echo "Error while writing data with sed") &
    else
        echo "<entry>added</entry>"

        # Store data in dedicated file
        (sed "2i\    $data," -i $file_data || echo "Error while writing data with sed") &
    fi
}

write_data_all() {
    echo -en "data = $data" > $file_data
}

check_data() {
    # Test if Arguments match Pattern to prevent Misuse
    grep --quiet --perl-regexp '^\{"date":"\d{4}-\d{2}-\d{2}",("[\wé]+":-?\d+,?)*\}$' <<< $data \
      || { echo 'Error: Arguments do not match defined pattern. Aborting script to prevent misuse.'; exit; }
}


# Body (return some information to see if the POST request was successful)
################################################################################

echo '<response>'
echo "<data>$data</data>"
#check_data
#write_data
write_data_all
echo '</response>'
