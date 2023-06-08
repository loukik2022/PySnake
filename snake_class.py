from turtle import Turtle

# Sets the position of the turtle along the x-axis. 
# The first turtle at (-20,0), second at (0,0), and third at (20,0) for 3 turtles
START = [(0,0), (-15,0), (-30,0)]     # const variable to intialize snake position as game start
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DIMENSIONS = 15/15
MOVE_DISTANCE = 15

class Snake(Turtle):
    def __init__(self):                   # start point for snake_class program to execute
        super().__init__()
        self.body = []
        self.create_snake()
        self.head = self.body[0]          # snake head

    # Create snake body
    def create_snake(self):
        for pos in START:
            self.add_body_part(pos)

    def add_body_part(self, pos):
        body_part = Turtle("square")
        body_part.color("white")
        body_part.penup()                # avoid traces of snake body_part
        body_part.shapesize(DIMENSIONS)
        #body_part.goto(pos) 
        body_part.speed('fastest')
        self.body.append(body_part)

    # move snake forward
    def move(self):
        for t in range(len(self.body)-1, 0, -1):
            # define next turtle position
            new_x = self.body[t-1].xcor()
            new_y = self.body[t-1].ycor()
            self.body[t].goto(new_x, new_y)  # move current turtle to next turtle position
                      
        self.head.forward(MOVE_DISTANCE)                # move snake forward in its current direction (by 20px)

    # move snake up, down, left and right using keyboard input
    def up(self):   
        if(self.head.heading()!=DOWN):      # snake can't move in reverse direction      
            self.head.setheading(UP)

    def left(self):     
        if(self.head.heading()!=RIGHT):        
            self.head.setheading(LEFT)

    def down(self): 
        if(self.head.heading()!=UP):             
            self.head.setheading(DOWN)

    def right(self): 
        if(self.head.heading()!=LEFT):             
            self.head.setheading(RIGHT)

    def extend(self): 
        self.add_body_part(self.body[-1].position())