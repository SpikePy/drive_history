function submitData(formData) {
    sum = 0
    Array.from(document.getElementsByClassName('input-person')).forEach(el => {sum += parseInt(el.value)})
    if (sum !== 0) {
        alert('Please check your inputs. The sum of all inputs has to be 0!')
        return
    }

    args = Array.from(formData).join(';').replace(/,/g,'=')

    // alert(args)

    var xhttp = new XMLHttpRequest()
    xhttp.open("POST", "/cgi-bin/drive_entry.cgi", true)
    xhttp.onreadystatechange = function () {
        if(this.readyState === XMLHttpRequest.DONE && this.status == 200) {
            location.reload(false)
        }
    }
    xhttp.send(args)
}


/*
 Show log on the page by removing the `hidden` class from certain elements
 and adding it to others
 Should be bound to a button
*/
function logShow() {
    document.getElementById('button_logShow').classList.add('display-none')
    document.getElementById('evaluation').classList.add('display-none')
    document.getElementById('interaction-area').classList.add('display-none')
    document.getElementById('log').classList.remove('display-none')
}

/*
 Undo the effects of `logShow()` so the display-none classes are reset
 like when you initially opened the site
 Should be bound to another button
*/
function logHide() {
    document.getElementById('button_logShow').classList.remove('display-none')
    document.getElementById('interaction-area').classList.remove('display-none')
    document.getElementById('evaluation').classList.remove('display-none')
    document.getElementById('log').classList.add('display-none')
}

// Evaluate driving history (by calculating counts of being driver - pessenger) and add a class to style the result accordingly
function evaluate(shortName) {
    sum = 0
    Array.from(document.getElementsByClassName(shortName)).forEach(el => sum += parseInt(el.getAttribute('data-value')))

    if      ( sum > 0 ) { document.getElementById("eval-" +shortName).className = "number eval-positive" }
    else if ( sum < 0 ) { document.getElementById("eval-" +shortName).className = "number eval-negative" }
    else                { document.getElementById("eval-" +shortName).className = "number"               }

    document.getElementById("eval-" +shortName).innerHTML = sum
}

/*
 Gets the current date in the form of YYYY-MM-DD and inserts it into the form
 Calculates for everybody `driving - pessenger` and write it on the
 Should be executed when the site finished loading
*/
function loaded() {
    document.getElementById("p-last-entry").innerText = data[0].date

    today         = new Date()
    year          = today.getYear()+1900
    month         = ("0" +(today.getMonth()+1)).slice(-2)
    day           = ("0" +today.getDate()).slice(-2)
    date          = `${year}-${month}-${day}`
    td_date.value = date

    evaluate("ren")
    evaluate("mat")
    evaluate("yve")

    saved_trips = 0
    Array.from(document.getElementsByClassName('passenger')).forEach(el => saved_trips += parseInt(el.getAttribute('data-value')))
    document.getElementById("eval-savings").innerHTML = Math.abs(saved_trips)
}
