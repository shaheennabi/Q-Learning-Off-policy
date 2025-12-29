
class Environment:
    def __init__(self, rows, cols):
        self.rows = rows   
        self.cols = cols 
        self.start = (0,0)
        self.current_state = None
        self.terminal_state = (rows-1, cols-1)




    def reset(self):
        self.current_state = self.start
        return self.current_state
    


    def step(self, action):
        row, col = self.current_state

        if action == 0:  # up
            new_row, new_col = row-1, col
        elif action == 1:  # right
            new_row, new_col = row, col+1
        elif action == 2:  # left
            new_row, new_col = row, col-1
        elif action == 3:  # down
            new_row, new_col = row+1, col
        else:
            raise ValueError("Invalid Action")


        if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
            new_row, new_col = row, col


        next_state = (new_row, new_col)

        if next_state == self.terminal_state:
            reward, done = 0, True
        
        else:
            reward,  done = -1, False


        self.current_state = next_state

        return next_state, reward, done