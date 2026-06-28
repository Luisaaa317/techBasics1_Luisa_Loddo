#### Where I found the code (link)
In my final project with Celia we wanted to implement a few minigames into our interactive environment.
One idea that we had was creating a memory game since it would allow us to go into an artsy direction and use our own images.
First I used the GitHub search to try and find memory games, however the games I found were not really what I was looking for.
I almost wanted to let go of the idea of researching a memory game and went to look into the repository that was linked in the assignment.
In that repository I found a memory game.
Here's the exact link: https://github.com/geekcomputers/Python/blob/master/Memory_game.py


#### What the programm does and general structure
In general the program creates a very simple memory game by creating cards out of Q&A pairs which are saved in a dictionary. 
The answers are used to create two cards per answer.
Those cards are shuffled and assembled in a 4x4 grid. The user can then interact with the cards and flip them by clicking on them. 
As soon as two cards are flipped the program compares them and adds a point to the score if the two flipped cards are equal. If they are not equal they are flipped back around.
In the end the score is compared to the amount of questions and a final message is displayed.

First the program imports all necessary libraries. Afterward, the code defines constants for colors which are later used to color cards. Then the size of the cards and the window in which the game is played are defined through constants and the window is created.
After that the dictionary with the questions and answers as well as a matching image is created.
After there is a list created that takes the answers from the dictionary and saves them twice each.
The cards are then shuffled using the random library and a 4x4 grid is created which gives 16 possible positions for the cards.
Following that the functions "display_text" and "draw_cards" are defined. 
To start the game all cards are flipped face down and an empty list for the cards that are later flipped around is created. The score is set to zero.
After that follows the main game loop. All cards are drawn using the "draw_cards" function and the current score is displayed. 
The main loop checks multiple event types. It checks whether the user has ended the game and if the user has clicked on a card. 
If the user has clicked on a card and that card was not face up yet the card is flipped around and added to the "flipped_cards" list.
As soon as two cards are flipped they are compared. If its a match the score goes up by one point. 
As soon as the score reaches the amount of questions that are in the dictionary a final message is displayed and the game loop is ended.

####  Function analysis

1. What does this function do?
The "draw_cards" function is responsible for drawing all cards on the screen and draw them differently depending on if they face up or down.

2. What are the inputs and outputs?
The function takes the answers which are saved as cards in the "cards" list and puts out a drawn card. 
If the card is faced up the answer is displayed in pink letters on a white card.
If the card is faced down the card is displayed as a pink card with a grey border.

3. How does it work (step by step)?
The function starts with a for loop that calls on the enumerate function to get the x and y positions saved in the "card_positions" list and the fitting index of a card.
The function then for example knows that the card with index 1 is saved at position (0,0).
The function then checks if a card with a certain index is flipped up or down by using an if-command. 
If the card is flipped up meaning if visible is true the card is drawn using the draw fucntion from pygame. 
The card is drawn as a white rectangle. 
The size of the card is determined by calling on the constant CARD_SIZE that was defined at the beginning of the code.
To show the answer on the card the function calls on another function called "display_text".
It calls on the previously defined variable "font" and the constant "PINK" to print the answer in a certain font size and color.
Through x+10 and y+30 the answer is displayed on the card.
If the card is flipped face down it is also drawn as a rectangle using pygames draw function.
The card is drawn in light pink with a greay border that is 5 pixels thick.



#### What I can learn from this code (structuring my code, finding clean solutions)
What I will most likely take away is teh structure of the code with the dictionary and the list and using those to create the cards.
I would additionally try to use images to make it a bit more artsy.
I also really liked the implementation of a score and the way that as soon as the score equals to the amount of questions the final message is displayed. 
In my opinion it's a really straight forward solution that saves a lot of unecessary code.
In Celia and Is idea we thought about making the trophy of each minigame a puzzle piece. We could use the same system and display the puzzle piece instead of a final message. 



#### Confusing and difficult parts
I would say I understood the code without much help from the internet since the main elements that the code consists of are elements that we covered in class.
I do not speak French and parts of the code were in French which made it a bit confusing to understand which messages were displayed for the user and if they were positive or negative messages.
However, that was quickly solved with a translator.
One thing that I also found confusing was the fact that in the dictionary there is an image file, but that image is then never used in the code.
I also noticed that the code creates a 4x4 grid which gives the cards 16 possible positions, however there are only 8 cards. I was wondering whether I had understood that correctly and it's an error or if I had simply misunderstood the code. After 

