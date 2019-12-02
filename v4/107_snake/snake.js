/* eslint-disable no-undef */

// eslint-disable-next-line no-unused-vars
class Snake {
	constructor() {
		this.x = 0
		this.y = 0
		this.x_speed = 1
		this.y_speed = 0
		this.total = 0
		this.tail = []
		points = 0
		dead = false

		this.update = () => {
			for (let i = 0; i < this.tail.length - 1; i++) {
				this.tail[i] = this.tail[i + 1]
			}
			if (this.total >= 1) {
				this.tail[this.total - 1] = createVector(this.x, this.y)
			}

			this.x += this.x_speed * size
			this.y += this.y_speed * size

			this.x = constrain(this.x, 0, width - size)
			this.y = constrain(this.y, 0, height - size)
		}

		this.check_death = () => {
			for (let i = 0; i < this.tail.length; i++) {
				let piece = this.tail[i]
				let d = dist(this.x, this.y, piece.x, piece.y)
				if (d < 1) return true
				else return false
			}
			// this.tail.forEach(piece => {
			// 	let d = dist(this.x, this.y, piece.x, piece.y)
			// 	if (d < 1) return true
			// 	else return false
			// })
		}

		this.show = () => {
			fill(255)
			noStroke()
			for (let i = 0; i < this.tail.length; i++) {
				rect(this.tail[i].x, this.tail[i].y, size, size)
			}
			rect(this.x, this.y, size, size)
			// this.tail.map(piece => rect(piece.x, piece.y, size, size))
		}

		this.dir = (x, y) => {
			if (this.x_speed * -1 != x) this.x_speed = x
			if (this.y_speed * -1 != y) this.y_speed = y
		}

		this.eat = (pos, food) => {
			let d = dist(this.x, this.y, pos.x, pos.y)
			if (d < 1 && food) {
				this.total++
				return true
			} else if (d < 1 && !food) {
				this.total--
				return true
			} else return false
		}
	}
}
