import sys
from turtle import Screen 
#defined by me libraries
from snake_class import Snake
from food_class import Food
from score_class import Score

sys.tracebacklimit = 0
SLOW = 1
FAST = 2


# setup screen of 600x600 px size with black background having title: Snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")

speed = 2          # game difficulty
snake = Snake()    # create snake at center of screen
food = Food()      # create food at random location
score = Score()    # Keep track of no of times snake eats food

screen.listen()
screen.onkey(snake.up, "Up")   
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right") 

# move snake as game starts
game_on = True
head = snake.head
# head.color("blue")
while game_on:
    screen.update()            # update screen once per game loop
    delay = int(1000 / speed)
    screen.ontimer(lambda: None, delay)       # program sleep for 0.01 sec, or we can say it lag by 0.01 sec to update screen
    snake.move()

    # detect snake eating food
    if (head.distance(food)<15):
        food.refresh()
        snake.extend() 
        score.update()

    # detect snake collision with wall
    if (head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280):
        score.game_over()
        game_on = False

    # detect snake collision with itself
    for segment in snake.body[1:]:
        if (head.distance(segment)<10):
            if(segment==head): pass
            score.game_over()
            game_on = False
    
screen.exitonclick()       # exit screen on click