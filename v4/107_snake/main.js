let snake, food
let points = 0
let fps = true
const size = 20

setup = () => {
	createCanvas(500, 300)
	frameRate(10)
	snake = new Snake()
	pick_location()
}

pick_location = () => {
	let cols = floor(width/size)
	let rows = floor(height/size)
	food = createVector(floor(random(cols)), floor(random(rows)))
	food.mult(size)
}

draw = () => {
	background(113)

	if (snake.eat(food)) {
		pick_location()
		points += 10
	}
	snake.update()
	snake.show()

	text(points, 10, 10)

	fill(250, 10, 10)
	rect(food.x, food.y, size, size)
}

keyPressed = () => {
	if (keyCode === UP_ARROW) {
		snake.dir(0, -1)
	} else if (keyCode === DOWN_ARROW) {
		snake.dir(0, 1)
	} else if (keyCode === RIGHT_ARROW) {
		snake.dir(1, 0)
	} else if (keyCode === LEFT_ARROW) {
		snake.dir(-1, 0)
	} else if (keyCode === BACKSPACE) {
		if (fps) {
			frameRate(60); fps = false
		} else {
			frameRate(10); fps = true
		}
	}
}

class Snake {
	constructor() {
		this.x = 0
		this.y = 0
		this.x_speed = 1
		this.y_speed = 0
		this.total = 1
		this.tail = []

		this.update = () => {
			for (let i = 0; i < this.tail.length-1; i++) {
				this.tail[i] = this.tail[i+1]
			}
			if (this.total >= 1) {
				this.tail[this.total-1] = createVector(this.x, this.y)
			}

			this.x = this.x + this.x_speed * size
			this.y = this.y + this.y_speed * size

			this.x = constrain(this.x, 0, width-size)
			this.y = constrain(this.y, 0, height-size)
		}

		this.show = () => {
			fill(255)
			noStroke()
			for (let i = 0; i < this.tail.length; i++) {
				rect(this.tail[i].x, this.tail[i].y, size, size)
			}
		}

		this.dir = (x, y) => {
			this.x_speed = x
			this.y_speed = y
		}

		this.eat = (food) => {
			let d = dist(this.x, this.y, food.x, food.y)
			if (d < 1) {
				this.total++
				return true
			} else return false
		}
	}
}
