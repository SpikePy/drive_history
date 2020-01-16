#!/usr/bin/env bash

# Website File
file_website='/home/rho/drive_history/driving_history.html'

# Get Parameter from URL Arguments
read args

# Parse Parameter from URL Arguments and Evaluate them
args=$(echo "${args}" | tr '&' ';')
eval $args

log_write() {
    entry="
        <p>$date
            <ul>
                <li class='ren $ren' value='$ren'>René ($ren)</li>
                <li class='mat $mat' value='$mat'>Matthias ($mat)</li>
                <li class='yve $yve' value='$yve'>Yvette ($yve)</li>
            </ul>
        </p>"

    if grep "$date" $file_website > /dev/null; then
        echo "Entry Changed<br>"
       # sed "s|.*$date.*|`echo $entry`|" -i $file_website
       sed "s|.*$date.*|<p>$date<ul><li class='ren $ren' value='$ren'>René ($ren)</li><li class='mat $mat' value='$mat'>Matthias ($mat)</li><li class='yve $yve' value='$yve'>Yvette ($yve)</li></ul></p>|" -i $file_website
    else
        echo "Entry Added<br>"
        #sed "/id='log'/a `echo $entry`" -i $file_website
        sed "/id='log'/a <p>$date<ul><li class='ren $ren' value='$ren'>René ($ren)</li><li class='mat $mat' value='$mat'>Matthias ($mat)</li><li class='yve $yve' value='$yve'>Yvette ($yve)</li></ul></p>" -i $file_website
    fi

    echo "$args<br>"
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
<body>
    `log_write`
</body>
</html>
EOF


#<body onload="window.location=document.referrer">
# date +%Y-%m-%d
