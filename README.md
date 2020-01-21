# Project to track who was driving when

## Notes
- get all variables with a certain regex:
`Object.keys(window).toString().match(/date_\d\d\d\d_\d\d_\d\d/g)`
- get data from variables searched via regex:
`Object.keys(window).toString().match(/date_\d\d\d\d_\d\d_\d\d/g).forEach(el => {console.log(el, eval(el))})`
- get values of first array element from variables searched via regex:
`Object.keys(window).toString().match(/date_[_\d]+/g).forEach(el => {console.table(el, eval(el)[0])})`

## ToDo
Make 3 accounts with an array of 2 elements which stores the balance of this couple of driver and pessanger:
- ren_mat = [0,0]
- mat_yve = [0,0]
- yve_ren = [0,0]
