import customtkinter as ctk
from settings import *
from random import randint

class Game(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Snake")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

        self.columnconfigure(list(range(FIELDS[0])), weight=1, uniform="a")
        self.rowconfigure(list(range(FIELDS[1])), weight=1, uniform="a")

        self.snake = [START_POS,(START_POS[0]-1,START_POS[1]),(START_POS[0]-2,START_POS[1])]
        self.direction = DIRECTIONS["right"]
        self.bind("<Key>", self.get_input)

        self.place_apple()

        self.draw_frames = []

        self.animate()

        self.mainloop()

    def get_input(self, event):
        match event.keycode:
            case 37: self.direction = DIRECTIONS["left"]
            case 38: self.direction = DIRECTIONS["up"]
            case 39: self.direction = DIRECTIONS["right"]
            case 40: self.direction = DIRECTIONS["down"]
        print(self.direction)

    def animate(self):
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        self.snake.insert(0, new_head)

        self.snake.pop()

        self.draw()

        self.after(250, self.animate)

    def place_apple(self):
        self.apple_pos = (randint(0, FIELDS[0]-1),randint(0,FIELDS[1]-1))
        
    def draw(self):
        if self.draw_frames:
            for frame, pos in self.draw_frames:
                frame.grid_forget()
            self.draw_frames.clear()


        apple_frame = ctk.CTkFrame(self, fg_color=APPLE_COLOR)
        self.draw_frames.append((apple_frame, self.apple_pos))

        for index, pos in enumerate(self.snake):
            color = SNAKE_BODY_COLOR if index != 0 else SNAKE_HEAD_COLOR
            snake_frame = ctk.CTkFrame(self, fg_color=color, corner_radius=0)
            self.draw_frames.append((snake_frame, pos))

        for frame, pos in self.draw_frames:
            frame.grid(column=pos[0], row=pos[1])

Game()