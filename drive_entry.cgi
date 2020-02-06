#!/usr/bin/env bash
echo '<response>'

# Website File
file_website='/home/rho/drive_history/index.html'
file_data='/home/rho/drive_history/data.js'

# Get Parameter from URL Arguments
read args
echo "<args>$args</args>"
# exit

# Test if Arguments match Pattern to prevent Misuse
echo $args | grep --quiet --perl-regexp "^(\w+=-?\d+;?)*(date=\d{4}-\d{2}-\d{2});?(\w+=-?\d+;?)*$" \
  || { echo 'Error: Arguments do not match defined pattern. Aborting script to prevent misuse.'; exit; }

# Parse Parameter from URL Arguments and Evaluate them
# args=$(echo "${args}" | tr '&' ';') replace '&' with ';' when data are send as url parameters
eval $args

activity() {
    case $1 in
                       0 ) echo -n "hidden";;
       [0-9]| [0-9][0-9] ) echo -n "driver";;
      -[0-9]|-[0-9][0-9] ) echo -n "passenger";;
                       * ) echo -n "Error: Can not define activity"; exit
    esac
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
        echo "<entry>changed</entry>"
        sed "s|.*$date.*|            `echo -n $template_entry`|" -i $file_website &

        # Store data in dedicated file
        sed "s|.*$date.*|    {\"date\":\"$date\",\t\"ren\":$ren,\t\"mat\":$mat,\t\"yve\":$yve},|" -i $file_data &
    else
        echo "<entry>added</entry>"
        sed "/id='table-header'/a\            `echo -n $template_entry`" -i $file_website &

        # Store data in dedicated file
        sed "2i\    {\"date\":\"$date\",\t\"ren\":$ren,\t\"mat\":$mat,\t\"yve\":$yve}," -i $file_data &
    fi

}

log_write

echo '</response>'
