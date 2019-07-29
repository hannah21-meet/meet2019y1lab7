import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=800
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake.pos()) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    stamp1 = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(stamp1)

for z in range(START_LENGTH):
    snake.pendown()
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    snake.goto(x_pos, y_pos)
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position
    
snake.direction = "Up"

def up():
    snake.direction="Up" #Change direction to up
    move_snake() #Update the snake drawing 
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!
snake.direction='left'
def left():
    snake.direction='left'
    move_snake()
    print('you pressed the left key')
snake.direction='down'
def down():
    snake.direction='down'
    move_snake()
    print('you pressed the down key')
snake.direction='right'
def right():
    snake.direction='right'
    move_snake()
    print('you pressed the right key')

turtle.onkeypress(up, "Up")
turtle.listen()
# Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(down,"down")
turtle.listen()
turtle.onkeypress(right,"right")
turtle.listen()
turtle.onkeypress(left,"left")
turtle.listen()



def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
            
    if snake.direction=='right':
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved right')
    elif snake.direction=='left':
         snake.goto(x_pos, y_pos - SQUARE_SIZE)
         print('you moved left')

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()


turtle.mainloop()

