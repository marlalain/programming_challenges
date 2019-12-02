/* eslint-disable no-undef */

// TODO Die if you touch the border
// TODO Fix the bug where you do a 180°

let snake, food, poison, pos, dead
let points = 0
let fps = true
const size = 20

setup = () => {
	createCanvas(500, 300)
	frameRate(10)
	snake = new Snake()
	food = pick_location()
	poison = pick_location()
}

pick_location = () => {
	let cols = floor(width / size)
	let rows = floor(height / size)

	pos = createVector(floor(random(cols)), floor(random(rows)))
	pos.mult(size)
	return pos
}

draw = () => {
	background(113)

	if (!dead) {
		if (snake.eat(food, true)) {
			food = pick_location()
			poison = pick_location()
			points += 10
		} else if (snake.eat(poison, false)) {
			food = pick_location()
			poison = pick_location()
			points -= 10
		}

		snake.update()
		snake.show()

		text(points, 10, 15)

		fill(250, 10, 10)
		rect(food.x, food.y, size, size)
		fill(10, 250, 10)
		rect(poison.x, poison.y, size, size)
		if (points < 0) dead = true
		if (snake.check_death()) dead = true
	} else {
		snake = new Snake()
	}
}

keyPressed = () => {
	if (keyCode === UP_ARROW || key == "w" || key == "k") {
		snake.dir(0, -1)
	} else if (keyCode === DOWN_ARROW || key == "s" || key == "j") {
		snake.dir(0, 1)
	} else if (keyCode === RIGHT_ARROW || key == "d" || key == "l") {
		snake.dir(1, 0)
	} else if (keyCode === LEFT_ARROW || key == "a" || key == "h") {
		snake.dir(-1, 0)
	} else if (keyCode === BACKSPACE) {
		if (fps) {
			frameRate(60)
			fps = false
		} else {
			frameRate(10)
			fps = true
		}
	}
}
