#%%
import time
import keyboard
import random
# Create a 30x10 game board

width = 15
height = 7
board = [[' ' for _ in range(width)] for _ in range(height)]
snake = [(5,6),(5,5)]
apple = (5,8)


# initiate input with two (move to the right)
direction = "right"

#%%
# Function to print the game board
def print_board(board):
    for i in range(width+2):
        print("_",end="")
    print()
    for row in board:
        print("|",end='')
        for cell in row:
            print(cell, end='')
        print("|")
    for i in range(width+2):
        print(" ͞",end="")
    print()
#%%

def update_board_with_snake(board,snake, removed_element):
    for cell in snake:
        board[cell[0]][cell[1]] = 'X'
    # only do, if an element was removed
    if not (removed_element[0] == -1 and removed_element[1] == -1):
        board[removed_element[0]][removed_element[1]]=" "
#%%

def update_board_with_apple(board,apple):
    board[apple[0]][apple[1]] = 'O'
#%%

def get_user_input(direction):
    if keyboard.is_pressed('w'):
        direction = "up"
    elif keyboard.is_pressed('s'):
        direction = "down"
    elif keyboard.is_pressed('a'):
        direction = "left"
    elif keyboard.is_pressed('d'):
        direction = "right"
    return direction
#%%

def update_snake(snake,direction,apple):
    head = snake[0]
    if direction == "up":
        new_head = (head[0]-1,head[1])
    if direction == "down":
        new_head = (head[0]+1,head[1])
    if direction == "left":
        new_head = (head[0],head[1]-1)
    if direction == "right":
        new_head = (head[0],head[1]+1)
    # print(new_head)

    # check for apple
    if new_head[0] == apple[0] and new_head[1] == apple[1]:
        apple = create_new_apple()
        removed_element = (-1,-1)
    else:
        removed_element = snake.pop()

    # check for collision with snake itself
    if new_head in snake:
        game_running = False
    else:
        game_running = True

    # check for collision with wall
    if new_head[0] < 0 or new_head[1] < 0:
        game_running = False
    if new_head[0] >= height or new_head[1] >= width:
        game_running = False

    snake.insert(0,new_head)

    
        
    
    return snake, removed_element, apple, game_running
#%%
def create_new_apple():
    new_apple = (random.randint(1,height-1), random.randint(1,width-1))
    if new_apple in snake:
        return create_new_apple()
    else:
        return new_apple
#%%
def print_game_over(snake):
    print("################################")
    print("GAME OVER")
    print("Your score is: " + str(len(snake)))
    print("################################")
if __name__ == "__main__":
    # update_board_with_snake(board,snake,(-1,-1))
    # update_board_with_apple(board,apple)
    # print_board(board)
    game_running = True
    while game_running:
        time.sleep(0.5)    
        direction = get_user_input(direction)
        # print(direction)
        # update_snake(snake, direction)
        snake, removed_element, apple, game_running = update_snake(snake, direction,apple)
        if(game_running):
            update_board_with_snake(board,snake, removed_element)
            update_board_with_apple(board,apple)
            print_board(board)
        else:
            print_game_over(snake)

