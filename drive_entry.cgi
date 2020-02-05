#!/usr/bin/env bash

# Website File
file_website='/home/rho/drive_history/index.html'
file_data='/home/rho/drive_history/driving_history_data.js'

# Get Parameter from URL Arguments
read args

# Test if Arguments match Pattern to prevent Misuse
echo $args | grep --quiet --perl-regexp "^(\w+=-?\d+&?)*(date=\d{4}-\d{2}-\d{2})&?(\w+=-?\d+&?)*$" \
  || { echo 'Error: Arguments do not match defined pattern. Aborting script to prevent misuse.'; exit; }

# Parse Parameter from URL Arguments and Evaluate them
args=$(echo "${args}" | tr '&' ';')
eval $args

activity() {
    if   [ $# -eq 1 ]; then
        case $1 in
                           0 ) echo -n "hidden";;
           [0-9]| [0-9][0-9] ) echo -n "driver";;
          -[0-9]|-[0-9][0-9] ) echo -n "passenger";;
                           * ) echo -n "Error: Can not define activity"; exit
        esac
    else
        echo -n "Error: Can not define activity"; exit
    fi
}


log_write() {
    template_entry="
        <tr>
            <td>$date</td>
            <td class='ren $(activity $ren)' data-person='ren' data-value='$ren'>$ren</td>
            <td class='mat $(activity $mat)' data-person='mat' data-value='$mat'>$mat</td>
            <td class='yve $(activity $yve)' data-person='yve' data-value='$yve'>$yve</td>
        </tr>"

    if grep --quiet "$date" $file_website; then
        echo -n "Entry Changed<br>"
        sed "s|.*$date.*|`echo -n $template_entry`|" -i $file_website &

        # Store data in dedicated file
        sed "s|.*$date.*|date_$date = [['ren',$ren],['mat',$mat],['yve',$yve]]|" -i $file_data &
    else
        echo -n "Entry Added<br>"
        sed "/id='table-header'/a `echo -n $template_entry`" -i $file_website &

        # Store data in dedicated file
        echo "date_$date = [['ren',$ren],['mat',$mat],['yve',$yve]]" >> $file_data &
    fi

    echo -n "$args<br>"
}

cat << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Driving Log</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
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
<body onload="window.location.href = document.referrer + '?' + parseInt(Math.random()*100)">
    `log_write`
</body>
</html>
EOF


#<body onload="window.location.href = document.referrer + '?date=' + new Date().valueOf()">
# date +%Y-%m-%d
