#----------------------------------import required packages-------------------------------------
import tkinter
import pygame
from pygame.locals import *
import action as action
import speech_recognition as sr
import pyaudio
import pyttsx3
import random
import enchant
from tkinter import *
from random import choice
import time
import os


#************************************************************************************************

#---------------------------------global variable and set properties for functions---------------

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

#*************************************************************************************************

with open('list_of_word.txt') as file:
    all_words = [line.strip() for line in file]

words=[choice(all_words)for n in range(10)]

#print(words)
turn = 10


#--------------------------------------------------------------------------------------------------
#print(enchant.list_dicts())

def msg(audio):
    engine.say(audio)
    engine.runAndWait()

def up():
    screen.update_idletasks()
    screen.update()

def spekk(source):
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    return command


#***************************************************************************************************

#---------------------------------------------------------------------------------------------------
def onClick(param):
    pass


try:
    with sr.Microphone() as source:

        print()
        print()

        print('\t\t\t\t\t\t\t\t* * * * * * * * * * * * * * Welcome To Gaming Zone * * * * * * * * * * * * * *')

        print()
        print()

        msg("Welcome To Gaming Zone ")
        print()
        print('Please Tell Me Your Name:')
        msg('Please Tell Me Your Name:')

        catch = spekk(source)

        print('Hello-' + catch + ' Hope Your Doing Well')
        msg('Hello' + catch + 'Hope Your Doing Well')

        print('\t\t\t\t\t\t\t\t\t\t\t\t\tWhich Game do you want to play...!!')
        msg('Which Game do you want to play')

        print('Game List')
        print()
        print('1. Guess The Word',end='')
        msg('Guess The Word')

        print('\t\t\t\t\t\t2. Snake & Apple',end='')
        msg('Snake and Apple')

        print('\t\t\t\t\t\t3. Tic Tac Toe')
        msg('Tic Tac Toe')

        print('Press 1 to play Guess The Word Game')
        msg('Press 1 to play Guess The Word Game')
        print()
        print('Press 2 to play Snake & Apple Game')
        msg('Press 2 to play Snake & Apple Game')
        print()
        print('Press 3 to play Tic Tac Toe')
        msg('Press 3 to play Tic Tac Toe')
        print()
        print('Enter your choice:')
        msg('Enter your choice:')
        choice = input()

        done=0
        if choice == '1':
            while turn > 0:
                if turn>0:
                    print('Write any alphabet/word to play the game')
                    msg('Write any alphabet/word to play the game')
                    letters = input()
                    #print(letters)
                    for word in words:
                        if letters == word:

                            print('\t\t\t\tHurrah!! You get the word',end='')
                            msg('Hurrah!! You get the word')
                            print('\t\t\t\tHurrah!! You get the word',end='')
                            msg('Hurrah!! You get the word')
                            print('\t\t\t\tHurrah!! You get the word')
                            msg('Hurrah!! You get the word')

                            done+=1
                            break
                        else:
                            for letter in word:
                                print(letter if letter in letters else '_', end='')
                        print()
                    turn -= 1
                if turn == 0:
                    print("Aww..!!you loss the game")
                    msg("Aww..!!you loss the game")
                if done==1:
                    break
# *************************************************************supriti's portion **************************************************

        elif choice=='2':
            SIZE = 40
            BACKGROUND_COLOR = (110, 110, 5)


            class Apple:
                def __init__(self, parent_screen):
                    self.parent_screen = parent_screen
                    self.image = pygame.image.load("resources/apple.jpg").convert()
                    self.x = 120
                    self.y = 120

                def draw(self):
                    self.parent_screen.blit(self.image, (self.x, self.y))
                    pygame.display.flip()

                def move(self):
                    self.x = random.randint(1, 24) * SIZE
                    self.y = random.randint(1, 19) * SIZE


            class Snake:
                def __init__(self, parent_screen):
                    self.parent_screen = parent_screen
                    self.image = pygame.image.load("resources/blockpic.png").convert()
                    self.direction = 'down'

                    self.length = 1
                    self.x = [40]
                    self.y = [40]

                def move_left(self):
                    self.direction = 'left'

                def move_right(self):
                    self.direction = 'right'

                def move_up(self):
                    self.direction = 'up'

                def move_down(self):
                    self.direction = 'down'

                def walk(self):
                    # update body
                    for i in range(self.length - 1, 0, -1):
                        self.x[i] = self.x[i - 1]
                        self.y[i] = self.y[i - 1]

                    # update head
                    if self.direction == 'left':
                        self.x[0] -= SIZE
                    if self.direction == 'right':
                        self.x[0] += SIZE
                    if self.direction == 'up':
                        self.y[0] -= SIZE
                    if self.direction == 'down':
                        self.y[0] += SIZE

                    self.draw()

                def draw(self):
                    for i in range(self.length):
                        self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

                    pygame.display.flip()

                def increase_length(self):
                    self.length += 1
                    self.x.append(-1)
                    self.y.append(-1)


            class Game:
                def __init__(self):
                    pygame.init()
                    pygame.display.set_caption("Codebase Snake And Apple Game")

                    pygame.mixer.init()
                    self.play_background_music()

                    self.surface = pygame.display.set_mode((1050, 550))
                    self.snake = Snake(self.surface)
                    self.snake.draw()
                    self.apple = Apple(self.surface)
                    self.apple.draw()

                def play_background_music(self):
                    pygame.mixer.music.load('resources/running.mp3')
                    pygame.mixer.music.play(-1, 0)

                def play_sound(self, sound_name):
                    if sound_name == "crash":
                        sound = pygame.mixer.Sound("resources/crash.wav")
                    elif sound_name == 'ding':
                        sound = pygame.mixer.Sound("resources/ding.mp3")
                    pygame.mixer.Sound.play(sound)

                def reset(self):
                    self.snake = Snake(self.surface)
                    self.apple = Apple(self.surface)

                def is_collision(self, x1, y1, x2, y2):
                    if x1 >= x2 and x1 < x2 + SIZE:
                        if y1 >= y2 and y1 < y2 + SIZE:
                            return True
                    return False

                def render_background(self):
                    bg = pygame.image.load("resources/greenpic.jpg")
                    self.surface.blit(bg, (0, 0))

                def play(self):
                    self.render_background()
                    self.snake.walk()
                    self.apple.draw()
                    self.display_score()
                    pygame.display.flip()

                    # snake eating apple scenario
                    if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                        self.play_sound("ding")
                        self.snake.increase_length()
                        self.apple.move()

                    # snake colliding with itself
                    for i in range(3, self.snake.length):
                        if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                            self.play_sound('crash')
                            raise "Collision Occurred"

                def display_score(self):
                    font = pygame.font.SysFont('arial', 30)
                    score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
                    self.surface.blit(score, (850, 10))

                def show_game_over(self):
                    self.render_background()
                    font = pygame.font.SysFont('arial', 30)
                    line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
                    self.surface.blit(line1, (200, 300))
                    line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
                    self.surface.blit(line2, (200, 350))
                    pygame.mixer.music.pause()
                    pygame.display.flip()

                def run(self):
                    running = True
                    pause = False

                    while running:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    running = False

                                if event.key == K_RETURN:
                                    pygame.mixer.music.unpause()
                                    pause = False

                                if not pause:
                                    if event.key == K_LEFT:
                                        self.snake.move_left()

                                    if event.key == K_RIGHT:
                                        self.snake.move_right()

                                    if event.key == K_UP:
                                        self.snake.move_up()

                                    if event.key == K_DOWN:
                                        self.snake.move_down()

                            elif event.type == QUIT:
                                running = False
                        try:

                            if not pause:
                                self.play()

                        except Exception as e:
                            self.show_game_over()
                            pause = True
                            self.reset()

                        time.sleep(.25)


            if __name__ == '__main__':
                game = Game()
                game.run()

 #********************************************khushi's portion***********************************************

        elif choice=='3':

            def display_board(board):
                print('\n' * 100)
                print("Layout of the Tic Tac Toe")
                print(" 7 | 8 | 9 ")
                print("-----------")
                print(" 4 | 5 | 6 ")
                print("-----------")
                print(" 1 | 2 | 3 \n\n\n\n")

                print("Actual Game")
                print(" {} | {} | {} ".format(board[7], board[8], board[9]))
                print("-----------")
                print(" {} | {} | {} ".format(board[4], board[5], board[6]))
                print("-----------")
                print(" {} | {} | {} ".format(board[1], board[2], board[3]))


            # Function to get the player input for chosing X or O

            def player_input():
                marker = ""
                while marker != "X" and marker != 'x' and marker != 'O' and marker != 'o':
                    marker = input("Player1, what do you want to take 'X' of 'O' : ")

                player1 = marker.upper()
                if marker == 'X' or marker == 'x':
                    player2 = 'O'
                else:
                    player2 = 'X'

                return (player1, player2)


            # Function to place the player's marker on the board at given position

            def place_marker(board, marker, position):
                board[position] = marker


            # Function to check if a player won the match

            def win_check(board, mark):
                if board[1] == board[2] == board[3]:
                    marker = board[1]
                elif board[1] == board[4] == board[7]:
                    marker = board[1]
                elif board[1] == board[5] == board[9]:
                    marker = board[1]
                elif board[2] == board[5] == board[8]:
                    marker = board[2]
                elif board[3] == board[6] == board[9]:
                    marker = board[3]
                elif board[3] == board[5] == board[7]:
                    marker = board[3]
                elif board[4] == board[5] == board[6]:
                    marker = board[4]
                elif board[7] == board[8] == board[9]:
                    marker = board[7]
                else:
                    marker = " "

                return marker == mark


            def choose_first():
                turn = random.randint(0, 1)
                if turn == 0:
                    print("Player 1 will go first")
                    return True
                else:
                    print("Player 2 will go first")
                    return False


            def space_check(board, position):
                return board[position] == " "


            def full_board_check(board):
                return board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[
                    5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " "


            def player_choice(board):
                move = 0
                time.sleep(0.2)
                while move < 1 or move > 9:
                    try:
                        move = int(input("Enter postision of your move (1-9) : "))
                    except:
                        print("Enter Valid Input")
                if space_check(board, move):
                    return move
                else:
                    return False


            def replay():
                play = ""
                while play.lower() != "yes" and play.lower() != "no":
                    play = input("Do you want to play again 'Yes' or 'No' : ")
                    play = play.lower()
                return play == "yes"


            print('Welcome to Tic Tac Toe!')
            time.sleep(0.2)
            while True:
                player1_marker, player2_marker = player_input()
                board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                display_board(board)
                game_on = True
                turn = choose_first()
                ch = input("Press Enter to Start Game")

                while game_on:
                    display_board(board)
                    if full_board_check(board):
                        game_on = False
                        print("Game is Draw")
                    elif turn:
                        print("Player 1 Turn:")
                        turn = False
                        position = False
                        while position is False:
                            position = player_choice(board)
                        if space_check(board, position):
                            place_marker(board, player1_marker, position)
                        if win_check(board, player1_marker):
                            game_on = False
                            display_board(board)
                            print("Winner is Player 1")
                    else:
                        print("Player 2 Turn:")
                        turn = True
                        position = False
                        while position is False:
                            position = player_choice(board)
                        if space_check(board, position):
                            place_marker(board, player2_marker, position)
                        if win_check(board, player2_marker):
                            game_on = False
                            display_board(board)
                            print("Winner is Player 2")

                if not replay():
                    break






        else:
            print('Please choose valid option')

except:
    pass


