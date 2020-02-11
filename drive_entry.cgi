#!/usr/bin/env bash

# Variables
################################################################################
# Path to data file
readonly file_data='/home/rho/drive_history/data.js'

# Get Parameter from URL Arguments
# read url_parameters
# readonly url_parameters

# Functions
################################################################################
write_data() {
    if grep --quiet "$date" $file_data; then
        echo "<entry>changed</entry>"

        # Store data in dedicated file
        sed "s|.*$date.*|    {\"date\":\"$date\",\t\"ren\":$ren,\t\"mat\":$mat,\t\"yve\":$yve},|" -i $file_data &
    else
        echo "<entry>added</entry>"

        # Store data in dedicated file
        sed "2i\    {\"date\":\"$date\",\t\"ren\":$ren,\t\"mat\":$mat,\t\"yve\":$yve}," -i $file_data &
    fi
}



# Body
################################################################################

echo '<response>'

# echo url_parameters to see/check them in the requests response
echo "<url_parameters>$url_parameters</url_parameters>"

# Test if Arguments match Pattern to prevent Misuse
echo $url_parameters | grep --quiet --perl-regexp "^(\w+=-?\d+;?)*(date=\d{4}-\d{2}-\d{2});?(\w+=-?\d+;?)*$" \
  || { echo 'Error: Arguments do not match defined pattern. Aborting script to prevent misuse.'; exit; }

# Parse Parameter from URL Arguments and Evaluate them
# url_parameters=$(echo "${url_parameters}" | tr '&' ';') replace '&' with ';' when data are send as url parameters
# eval $url_parameters

# write_data

echo '</response>'
