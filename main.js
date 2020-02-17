var attendees = []
var sum = {}



// Send input data via POST request to cgi script via button onclick
function submitData() {

    // Test if data are valid---meaning sum inputs have to be zero
    var input_sum = 0
    attendees.forEach(attendee => {input_sum += parseInt(document.getElementsByName(attendee)[0].value)})
    if (input_sum !== 0) {
        alert('Please check your inputs. The sum of all inputs has to be 0!')
        return
    }


    // Test if already an entry with this date and return its index, else returns -1
    var index = data.map(entry => entry.date).indexOf(date)


    // Update data array directly, so no reload is needed
    if (index >= 0) {
        console.log('Change Entry')

        // Change corresponding object to new data
        attendees.forEach(
            attendee => data[index][attendee] = parseInt(document.getElementsByName(attendee)[0].value)
        )

       // Remove already drawn history entries (triggers generate_log_entries if you want to show them)
       if (document.getElementsByClassName('generated-entry').length > 0) {
           Array.from(document.getElementsByClassName('generated-entry')).forEach(log_entry => log_entry.remove())
       }
    }
    else {
        console.log('Create Entry')

        // Create a new empty object at the beginning of the data array
	data.unshift({})
	data[0]['date'] = date
	attendees.forEach(
            attendee => data[0][attendee] = parseInt(document.getElementsByName(attendee)[0].value)
	)
    }

    // After updating data array trigger calculations again to show updated results on the page
    loaded()

    // Convert new data object to POST it to the cgi script
    args_cgi = JSON.stringify(data[index])

    // POST updated data
    var xhttp = new XMLHttpRequest()
    xhttp.open("POST", "/cgi-bin/drive_entry.cgi", true)
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && this.status != 200) {
            location.reload(true)
        }
    }
    xhttp.send(args_cgi)
}



/* Show log on the page by removing the `hidden` class from certain elements
 * and adding it to others or resets it to its default
 * Should be bound to a button */
function log_display(state) {
    if (state == "show") {
	if (document.getElementsByClassName('generated-entry').length === 0) {
		generate_log_entries()
	}
        document.querySelectorAll('div.section').forEach(el => el.classList.add('display-none'))
        document.getElementById('log').classList.remove('display-none')
    }
    else if (state == "hide") {
        document.querySelectorAll('div.section').forEach(el => el.classList.remove('display-none'))
        document.getElementById('log').classList.add('display-none')
    }
    else {
        alert('Wrong argument passed to function.')
    }
}

function generate_log_entries() {
    data.forEach(el => {
        entry = document.createElement('tr')
        entry.classList.add('generated-entry')
        entry.innerHTML = `<td>${el.date}</td>`
        attendees.forEach( attendee => {
            if (el[attendee] > 0) {
                entry.innerHTML += `<td class='driver'>${el[attendee]}</td>`
            }
            else if (el[attendee] < 0) {
                entry.innerHTML += `<td class='passenger'>${el[attendee]}</td>`
            }
            else {
                entry.innerHTML += `<td class='hidden'>${el[attendee]}</td>`
	    }
        })
    
        position = document.getElementById('table-header')
        position.parentNode.append(entry)
    })
}


function analyze_data() {
    sum       = {'René':0,'Matthias':0,'Yvette':0,'saved_trips':0}

    // Loop through data, so every loop evaluates one log entry/day
    data.forEach(entry => {
        // Loop attendees
        attendees.forEach( attendee => sum[attendee] += entry[attendee] )

        /* Find out how many trips were saved by summing all negative entries (which means how many times anybody has been a pessenger).
         * So inside the loop for through all log entries all values are determined, then only the negative ones are taken in consideration
         * and the sum of the resulting array is created */
        sum.saved_trips += -1 * Object.values(entry)
                                  .filter(value => value < 0)
                                  .reduce((a,b) => a+b)
    })
}



// Evaluate driving history (by calculating counts of being driver - pessenger) and add a class to style the result accordingly
function analyze_data_print() {
    attendees.forEach( attendee => {
        document.querySelector(`#summary td[name=${attendee}]`).innerHTML = sum[attendee]

        if      ( sum[attendee] > 0 ) { document.querySelector(`#summary td[name=${attendee}]`).className = "number positive" }
        else if ( sum[attendee] < 0 ) { document.querySelector(`#summary td[name=${attendee}]`).className = "number negative" }
        else                          { document.querySelector(`#summary td[name=${attendee}]`).className = "number"               }
    })
}



/* Gets the current date in the form of YYYY-MM-DD and inserts it into the form
 * Calculates for everybody `driving - pessenger` and write it on the
 * Should be executed when the site finished loading */
function loaded() {
    // Fill the array 'attendees' with all carpool attendees via the name of the input fields
    attendees = []
    document.querySelectorAll('input[type=number][name][value]').forEach(el => {attendees.push(el.name)})

    // Print date of last entry to page
    document.getElementById("p-last-entry").innerText = data[0].date

    // Generate todays date as YYY-MM-DD
    today         = new Date()
    year          = today.getYear()+1900
    month         = ("0" +(today.getMonth()+1)).slice(-2)
    day           = ("0" +today.getDate()).slice(-2)
    date          = `${year}-${month}-${day}`
    td_date.value = date

    analyze_data()
    analyze_data_print()
    document.querySelector('#summary td[name=savings]').innerHTML = sum.saved_trips
}

// TODO?
// // get array of unique keys
// a = []
// data.forEach( entry =>
//     Object.keys(entry).forEach( el =>
//             a.includes(el) || a.push(el)
//     )
//)
