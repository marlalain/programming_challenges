const fetch = require('node-fetch')
const url = 'https://randomuser.me/api/?inc=name'

fetch(url)
    .then(res => res.json())
    .then(json => {
        const results = json.results[0]

        console.log('First Name:', results.name.first)
        console.log('Last Name:', results.name.last)
    })
