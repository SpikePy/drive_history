#!/usr/bin/env bash

# Get Query String from URL
read args

# Parse Arguments from Query String
args=$(echo "${args}" | tr '+=' ' ')

#echo ${args[0]}

log_write() {
    if [ $3 -eq 1 ]; then
        echo "Saved\n`date`\n$1 $2"
        sed "/id='log'/a <ul>`date`\n<li>$1 $2</li></ul>" -i /home/rho/drive_history/driving_history.html
    elif [ $3 -eq 2 ]; then
        echo "Saved\n`date`\n$1 $2\n$1 $2"
        sed "/id='log'/a <ul>`date`\n<li>$1 $2</li><li>$1 $2</li></ul>" -i /home/rho/drive_history/driving_history.html
    fi

    (
        cd /home/rho/drive_history/
        git add .
        git commit -m "test" && git push
    )
}

cat << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Driving Log</title>
    <link rel="icon" type="image/svg+xml" href="images/car.svg">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body onload="alert('Saved');history.back()">
    `log_write ${args}`
</body>
</html>
EOF

