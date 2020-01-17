# Show log on the page by removing the `hidden` class from certain elements
# and adding it to others
# Should be bound to a button
function logShow() {
    document.getElementById('button_logShow').classList.add('hidden')
    document.getElementById('evaluation').classList.add('hidden')
    document.getElementById('interaction-area').classList.add('hidden')
    document.getElementById('log').classList.remove('hidden')
}

# Undo the effects of `logShow()` so the hidden classes are reset
# like when you initially opened the site
# Should be bound to another button
function logHide() {
    document.getElementById('button_logShow').classList.remove('hidden')
    document.getElementById('interaction-area').classList.remove('hidden')
    document.getElementById('evaluation').classList.remove('hidden')
    document.getElementById('log').classList.add('hidden')
}

# Gets the current date in the form of YYYY-MM-DD and inserts it into the form
# Calculates for everybody `driving - pessenger` and write it on the
# Should be executed when the site finished loading
function loaded() {
    today         = new Date()
    year          = today.getYear()+1900
    month         = "" +today.getMonth()+1
    day           = "" +today.getDate()
    date          = `${year}-${month}-${day}`
    td_date.value = date

    ren_sum = 0; Array.from(document.getElementsByClassName('ren')).forEach(el => ren_sum += el.value)
    mat_sum = 0; Array.from(document.getElementsByClassName('mat')).forEach(el => mat_sum += el.value)
    yve_sum = 0; Array.from(document.getElementsByClassName('yve')).forEach(el => yve_sum += el.value)
    savings = document.getElementsByClassName('activity_-2').length*2 + document.getElementsByClassName('activity_-1').length

    document.getElementById("eval-ren").innerHTML = ren_sum
    document.getElementById("eval-mat").innerHTML = mat_sum
    document.getElementById("eval-yve").innerHTML = yve_sum
    document.getElementById("eval-savings").innerHTML = savings
}
