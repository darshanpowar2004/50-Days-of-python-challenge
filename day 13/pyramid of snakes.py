from emoji import emojize
"""
  *
 **
***
"""

def python_snakes(num : int):
    snake_emoji = emojize(":snake:")
    for i in range(0,num):
        for j in range(0,i,-1):
            print(end=" ")
        for k in range(0,i):
            print(snake_emoji,end=" ")
        print("\n")



# python_snakes(7)


from emoji import emojize
def Python_snakes(n: int):
    # the loop to determine the number of rows of the pyramid
    for i in range(0, n):
        # The loop that determines number of columns
        for j in range(n, i, -1):
            # print space between the snake signs
            print(end=" ")
        for k in range(0, i):
            # printing the snake emoji
            print(emojize(':snake:'), end="  ")
        print("\n")
Python_snakes(7)