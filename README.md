# Project to track who was driving when

## Notes
- get all variables with a certain regex:
`Object.keys(window).toString().match(/date_\d\d\d\d_\d\d_\d\d/g)`
- get data from variables searched via regex:
`Object.keys(window).toString().match(/date_\d\d\d\d_\d\d_\d\d/g).forEach(el => {console.log(el, eval(el))})`
- get values of first array element from variables searched via regex:
`Object.keys(window).toString().match(/date_[_\d]+/g).forEach(el => {console.table(el, eval(el)[0])})`
