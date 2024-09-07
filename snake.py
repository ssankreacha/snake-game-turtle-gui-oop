from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")  # Each shape is square and color = white
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # Each segment will follow the either (position) xy
        new_segment.speed("slowest")
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()   # Second to last segment has x changed
            new_y = self.segments[seg_num - 1].ycor()   # Second to last segment has y changed
            self.segments[seg_num].goto(new_x, new_y)   # new segment (based on previous 2 lines) = EACH segment
        self.head.forward(MOVE_DISTANCE)                # Entire segment moves while game is on

    def up(self):   # When down can't go up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self): # When up can't go down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self): # When right can't go left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):    # When left can't go right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
