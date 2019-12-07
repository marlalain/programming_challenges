// for nodejs:
// let lucas_json = require("./lucas.json")
// console.log(lucas_json)

let lucas, paulo
let ajax = $.getJSON("lucas.json", json => {
	lucas = filter_json(json, "lucas costa")
	paulo = filter_json(json, "P e")
})

filter_json = (json, user) => {
	let messages = []
	// filtering mine messages and media
	messages_old = json.chats.list[0].messages
	messages_old = messages_old.filter(message => message.from == user)
	messages_old = messages_old.filter(message => message.text != "")
	messages_old.forEach(message => {
		if (message.text[0].text === undefined) messages.push(message.text)
		else messages.push(message.text[0].text)
	})
	return messages
}

setup = () => {
	if (ajax.status == 200) {
		console.log(lucas)
		console.log(paulo)
	}
}
draw = () => {}
