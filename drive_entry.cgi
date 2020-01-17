#!/usr/bin/env bash

# Website File
file_website='/home/rho/drive_history/index.html'
file_data='/home/rho/drive_history/driving_history_data.js'

# Get Parameter from URL Arguments
read args

# Parse Parameter from URL Arguments and Evaluate them
args=$(echo "${args}" | tr '&' ';')
eval $args

# Store data in dedicated file
echo "`date +date_%Y_%m_%d` = [['ren',$ren],['mat',$mat],['yve',$yve]]" >> $file_data

log_write() {
    template_entry="
        <p>$date
            <ul>
                <li class='ren activity_$ren' value='$ren'>René ($ren)</li>
                <li class='mat activity_$mat' value='$mat'>Matthias ($mat)</li>
                <li class='yve activity_$yve' value='$yve'>Yvette ($yve)</li>
            </ul>
        </p>"

    if grep "$date" $file_website > /dev/null; then
        echo "Entry Changed<br>"
        sed "s|.*$date.*|`echo $template_entry`|" -i $file_website
    else
        echo "Entry Added<br>"
        sed "/id='log'/a `echo $template_entry`" -i $file_website
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
    `log_write`
</body>
</html>
EOF


#<body onload="window.location=document.referrer">
# date +%Y-%m-%d
