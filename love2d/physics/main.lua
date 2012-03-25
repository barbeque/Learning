function love.load()
	world = love.physics.newWorld(0, 0, 650, 650)
	world:setGravity(0, 700) -- gravity is 700 units downward
	world:setMeter(64) -- meters are 64px tall

	objects = {}
	objects.ground = {}
	objects.ground.body = love.physics.newBody(world, 650/2, 625, 0, 0)
	objects.ground.shape = love.physics.newRectangleShape(objects.ground.body, 0, 0, 650, 50, 0) -- 50 tall

	objects.ball = {}
	objects.ball.body = love.physics.newBody(world, 650/2, 650/2, 15, 0)
	objects.ball.shape = love.physics.newCircleShape(objects.ball.body, 0, 0, 20) -- 20 radius centered on body

	love.graphics.setBackgroundColor(104, 136, 248)
	love.graphics.setMode(650, 650, false, true, 0)

	objects.box = {}
	objects.box.body = love.physics.newBody(world, 650/2 + 25, 605, 5, 0)
	objects.box.shape = love.physics.newRectangleShape(objects.box.body, 0, 0, 50, 20, 0)
end

function love.update(dt)
	ballIsOnGround = false
	world:update(dt)

	if love.keyboard.isDown("up") then
		objects.ball.body:applyForce(0, -900)
	elseif love.keyboard.isDown("right") then
		objects.ball.body:applyForce(400, 0)
	elseif love.keyboard.isDown("left") then
		objects.ball.body:applyForce(-400, 0)
	end
end

function love.draw()
	-- draw ground
	love.graphics.setColor(72, 160, 14)
	love.graphics.polygon("fill", objects.ground.shape:getPoints())

	-- draw ball
	love.graphics.setColor(193, 47, 14)
	love.graphics.circle("fill", objects.ball.body:getX(), objects.ball.body:getY(), objects.ball.shape:getRadius(), 20)

	-- draw box
	love.graphics.setColor(128, 0, 128)
	love.graphics.polygon("fill", objects.box.shape:getPoints())
end

