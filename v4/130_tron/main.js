/* eslint-disable no-undef */
let player

// TODO
// Create a 2D array, populate everything with 0, 1 or 2
// 0: Nothing (White)
// 1: Player 1 (Red)
// 2: Player 2 (Blue)

setup = () => {
	createCanvas(400, 400)
	render = new Render()
	player = new Rider()
}
draw = () => {
	background(133)

	player.update()
	player.draw()
}
keyPressed = () => {
	if (keyCode === UP_ARROW) {
		player.dir(0, -1)
	} else if (keyCode === DOWN_ARROW) {
		player.dir(0, 1)
	} else if (keyCode === RIGHT_ARROW) {
		player.dir(1, 0)
	} else if (keyCode === LEFT_ARROW) {
		player.dir(-1, 0)
	}
}

class Rider {
	constructor() {
		this.x = 0
		this.y = 0
		this.xdir = 0
		this.ydir = 0
		this.color = [255, 0, 0]

		this.dir = (x, y) => {
			this.xdir = x
			this.ydirr = y
		}

		this.update = () => {
			this.x += this.xdir
			this.y += this.ydir
		}

		this.draw = () => {
			// code
		}
	}
}

class Render {
	constructor() {
		// TODO make 2D array

		this.create_array = (cols, rows) => new Array(cols).fill(new Array(rows))
	}
}
