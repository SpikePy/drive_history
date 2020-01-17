function logShow() {
    document.getElementById('button_logShow').classList.add('hidden')
    document.getElementById('evaluation').classList.add('hidden')
    document.getElementById('interaction-area').classList.add('hidden')
    document.getElementById('log').classList.remove('hidden')
}

function logHide() {
    document.getElementById('button_logShow').classList.remove('hidden')
    document.getElementById('interaction-area').classList.remove('hidden')
    document.getElementById('evaluation').classList.remove('hidden')
    document.getElementById('log').classList.add('hidden')
}

function loaded() {
    today         = new Date()
    year          = today.getYear()+1900
    month         = "" +today.getMonth()+1
    day           = "" +today.getDate()
    date          = `${year}-${month}-${day}`
    td_date.value = date

    ren = []
    Array.from(document.getElementsByClassName('ren')).forEach(el => ren.push(el.value))
    ren.reduce((a,b) => a + b, 0)

    ren_sum = 0; Array.from(document.getElementsByClassName('ren')).forEach(el => ren_sum += el.value)
    mat_sum = 0; Array.from(document.getElementsByClassName('mat')).forEach(el => mat_sum += el.value)
    yve_sum = 0; Array.from(document.getElementsByClassName('yve')).forEach(el => yve_sum += el.value)
    savings = document.getElementsByClassName('activity_-2').length*2 + document.getElementsByClassName('activity_-1').length

    document.getElementById("eval-ren").innerHTML = ren_sum
    document.getElementById("eval-mat").innerHTML = mat_sum
    document.getElementById("eval-yve").innerHTML = yve_sum
    document.getElementById("eval-savings").innerHTML = savings
}
