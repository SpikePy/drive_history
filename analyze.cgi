#!/usr/bin/env sh
log=`cat /var/www/html/driving_history.html`

cat << EOF
  <!DOCTYPE html>
  <html>
    <head>
      <title>Driving - Log</title>
      <meta charset="UTF-8">
      <link rel="stylesheet" type="text/css" href="../html/style.css">
    </head>
    <body>
      <h1>Driving - Log</h1>
      <p>
        <h2>Rene Hoffmann</h2>
        `echo "$log" | grep --only-matching "Rene Hoffmann</li>" | wc -l`
      </p>
      <p>
        <h2>Matthias Rober</h2>
        `echo "$log" | grep --only-matching "Matthias Rober</li>" | wc -l`
      </p>
    </body>
EOF
