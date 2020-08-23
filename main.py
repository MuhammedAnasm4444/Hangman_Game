import pygame
import math
import random
# display setup
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

#button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH -  (RADIUS * 2 + GAP) * 13)/2)
starty = 400
A = 65
for i in range(26):
	x = startx + GAP * 2 + ((RADIUS*2 + GAP) * (i % 13))
	y = starty + ((i//13) * (GAP + RADIUS * 2))
	letters.append([x, y, chr(A + i), True])


# Fonts 
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# Setting images
images = []
for i in range(7):
	image = pygame.image.load("Hangman" + str(i)+ ".png")
	images.append(image)


#game variables
hangman_status = 0
again = False
not_again = False
words = ['PYTHON','GAME','DOOR','CHICKEN', 'MUTTON']
word = random.choice(words)
guessed = []


# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)




def draw():
	win.fill(WHITE)
	# draw TITLE
	text = TITLE_FONT.render("HANGMAN", 1, BLACK)
	win.blit(text, (WIDTH/2- text.get_width()/2, 20))
	
	# DRAW word
	display_word = ""
	for letter in word:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "
	text = WORD_FONT.render(display_word, 1, BLACK)
	win.blit(text, (400, 200))



	# load buttons
	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(win,BLACK, (x, y) , RADIUS, 3)
			text = LETTER_FONT.render(ltr, 1, BLACK)
			win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))



	win.blit(images[hangman_status], (150, 100))
	pygame.display.update()

def reset():
	global hangman_status
	global guessed
	global words
	global letters
	global word
	for i in range(len(buttons)):
		letters[i][4] = True

	hangman_status = 0
	guessed = []
	word = random.choice(words)
def display_message(message):
	

	win.fill(WHITE)
	text = WORD_FONT.render(message, 1, BLACK)
	again_text = LETTER_FONT.render("Play Again", 1, BLACK )
	win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
	




	pygame.display.update()
	pygame.time.delay(5000)
		



		
def main():       
	# Game Loop

	
	global again
	


	global hangman_status


	FPS = 60
	clock = pygame.time.Clock()
	run = True

	while run:
		clock.tick(FPS)
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()

				for letter in letters:
					x, y, ltr, visible = letter
					if visible:
						dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
						if dis < RADIUS:
							letter[3] = False
							guessed.append(ltr)
							if ltr not in word:
								 hangman_status += 1


		draw()
		won = True                  
		for letter in word:
			if letter not in guessed:
				won = False
				break
		if won:
			display_message("You WON!")
			break
		
				
		 
			

			
		if hangman_status == 6:
			display_message("You LOST!")
			break
			
main()




	
		
pygame.quit()





