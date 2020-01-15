#!/usr/bin/env bash

# Website File
file_website=/home/rho/drive_history/driving_history.html

# Get Query String from URL
read args

# Parse Arguments from Query String
args=$(echo "${args}" | tr '+=' ' ')

#echo ${args[0]}

log_write() {
    shortName=$2
    firstName=$3
    lastName=$4
    activity=$5
    count=$6

    if grep "`date +%Y-%m-%d`" $file_website; then
        sed "/`date +%Y-%m-%d`/a <li title=\"$activity\" class=\"${shortName}_${activity}_${count} ${activity}\">$firstName $lastName ($count)</li>" -i $file_website
    else
        sed "/id='log'/a <p>`date +%Y-%m-%d`<ul>\n<li title=\"$activity\" class=\"${shortName}_${activity}_${count} ${activity}\">$firstName $lastName ($count)</li>\n</ul></p>" -i $file_website
    fi
}

cat << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Driving Log</title>
    <link rel="icon" type="image/svg+xml" href="images/car.svg">
    <style>
        body {
            text-align:  center;
            font-family: sans-serif;
            font-size:   48pt;
            margin-top:  40vh;
            background-color: LimeGreen;
            color: white;
        }
    </style>
</head>
<body onload="window.location=document.referrer">
    `log_write ${args}`
</body>
</html>
EOF

#<body onload="alert('Saved');window.location=document.referrer">
