#!/usr/bin/env bash

# Get Query String from URL
read args

# Parse Arguments from Query String
args=$(echo "${args}" | tr '+=' ' ')

#echo ${args[0]}

log_write() {
    if [ $3 -eq 1 ]; then
        echo "Saved"
        sed "/id='log'/a <p>`date`<ul><li class=\"$1$2\">$1 $2</li></ul></p>" -i /home/rho/drive_history/driving_history.html
    elif [ $3 -eq 2 ]; then
        echo "Saved"
        sed "/id='log'/a <p>`date`<ul><li class=\"$1$2\">$1 $2</li><li class=\"$1$2\">$1 $2</li></ul></p>" -i /home/rho/drive_history/driving_history.html
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
