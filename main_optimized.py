from turtle import Screen
from enum import Enum
from snake_class import Snake
from food_class import Food
from score_class import Score

class DifficultyLevel(Enum):
    LOW = 0.02
    MEDIUM = 0.01
    HIGH = 0.005


# set up screen size
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")

# create snake at center of screen
snake = Snake()
# create food at random location
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")   
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right") 

def move_snake():
    snake.move()

    game_on = True
    # detect snake eating food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend() 
        score.update()

    # detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        score.game_over()
        game_on = False

    # detect collision with snake itself
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            if segment == snake.head:
                pass
            score.game_over()
            game_on = False
    
    if game_on:
        screen.update()
        screen.ontimer(move_snake, int(DifficultyLevel.MEDIUM.value*1000))

# move snake as game starts
game_on = True
move_snake()

screen.exitonclick()       # exit screen on click
