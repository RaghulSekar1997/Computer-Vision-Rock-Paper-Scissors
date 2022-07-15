from ctypes.wintypes import RGB
import cv2
import time
from keras.models import load_model
import numpy as np

# create a function for computer's choice
# outputs rock, paper or scissors 

def computer_choice():
    output = 'Scissors'
    a = np.random.randint(0,3)
    if a == 0:
        output = 'Paper'
    elif a == 1:
        output = 'Rock'
    else:
        output = output
    return output

# create a function that computes the winner of the round
def declare_winner(player_choice, computer_choice):
    winner = 'None'
    if (player_choice == 'Rock' and computer_choice =='Paper') or (player_choice == 'Paper' and computer_choice =='Scissors') or (player_choice == 'Scissors' and computer_choice =='Rock'):
        winner = 'Computer'
    elif (player_choice == 'Rock' and computer_choice =='Scissors') or (player_choice == 'Paper' and computer_choice =='Rock') or (player_choice == 'Scissors' and computer_choice =='Paper'):
        winner = 'Player'
    elif player_choice == 'Nothing':
        #print('Nothing was detected, Please try again!')
        winner = winner
    return winner

# create a function that takes as input player's choice and outputs the winner of the round and cpu choice
def rps_game(player_choice):
    computer = computer_choice()
    player = player_choice
    winner = declare_winner(player,computer)
    return winner, computer

# create a function that keeps score
def update_score(computer_score, player_score, winner): 
    if winner == 'Player':
        player_score += 1
    elif winner == 'Computer':
        computer_score += 1
    else:
        player_score = player_score
        computer_score = computer_score
    return (computer_score, player_score)

# function that decodes the model prediction to the corresponding action
def prediction_interpretation(prediction):
    
    if prediction[0][0] > 0.7:
        prediction = 'Paper'

    elif prediction[0][1] > 0.7:
        prediction = 'Rock'

    elif prediction[0][2] > 0.6:
        prediction = 'Scissors'

    else:
        prediction = 'Nothing'
    
    return prediction


def _rock_paper_scissors_game():
    # load model
    model = load_model('keras_model.h5', compile=False)

    # open the camera
    cap = cv2.VideoCapture(0) 
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # initialize computer and player scores
    computer_score = 0
    player_score = 0

    # initialize round counter
    ii = 1

    # define colors in RGB values
    black = RGB(0,0,0)
    blue = RGB(0,0,205)     

    # font to use
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        
        # read and display each frame
        _, frame = cap.read()
        
        # draw a rectangle in order to overlay game title on top of it
        cv2.rectangle(frame, (85, 12) , (546, 48), black, -1)

        # insert text on video 
        cv2.putText(frame, 'Rock-Paper-Scissors', (90, 40), font, 1,  (100,166,209), 2, cv2.LINE_AA)

        cv2.putText(frame, 'Play by pressing P', (5, 470), font, 1, (54.209,78), 1, cv2.LINE_AA)            

        cv2.putText(frame, 'Exit by pressing Q', (400, 470), font, 1, (0,0,225), 1, cv2.LINE_AA)

        
        # check for the key pressed
        k = cv2.waitKey(125)
        
        # set a 3 second timer
        TIMER = int(3)
        
        # set the key for the countdown to begin if 'p' key is pressed
        if k == ord('p'):
            prev = time.time()
                    
            while TIMER >= 0:
                _, img = cap.read()
                resized_frame = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image

                # use trained model to predict player's choice, once countdown goes to 0
                prediction = model.predict(data)

                # decode the model prediction to the corresponding action
                prediction = prediction_interpretation(prediction)
                
                # Display countdown on each frame        
                cv2.putText(img, str(TIMER), (30, 80), font, 3, black, 4, cv2.LINE_AA)
                
                # create rectangle for displaying player choice
                cv2.rectangle(img, (0, 423) , (142, 460), blue, -1)

                cv2.putText(img, f'{prediction}', (10, 450), font, 1, black, 4, cv2.LINE_AA)

                # create rectangle for displaying round no
                cv2.rectangle(img, (485, 25) , (640, 65), blue, -1)

                cv2.putText(img, f'Round {ii}', (490, 55), font, 1, black, 3, cv2.LINE_AA)
                
                cv2.imshow('Rock-Paper-Scissors Game', img)
                
                cv2.waitKey(125)

                # current time
                cur = time.time()
                
                # Update and keep track of Countdown, decrease timer by one for each second that passes
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
                
            # here need to run the game using the functions created above
            winner, cpu_choice = rps_game(prediction)
        
            # use the function that updates scores, to update score
            computer_score, player_score = update_score(computer_score, player_score, winner)
            
            # update round counter
            ii += 1 
        
            # restore the counter after window is closed
            TIMER = int(3) 

            # here need to print outcome of round
            
            # create rectangle for displaying computer choice
            cv2.rectangle(img, (485, 423) , (640, 460), blue, -1)

            cv2.putText(img, 'VS', (280, 460), font, 2, blue, 4, cv2.LINE_AA)
            
            cv2.putText(img, f'{cpu_choice}', (490, 450), font, 1, black, 3, cv2.LINE_AA)
            
            if winner =='None':
                if prediction == 'Nothing':
                    cv2.rectangle(img, (0, 200) , (640, 280), blue, -1)
                    cv2.putText(img, 'Nothing detected', (60, 260), font, 2, black, 4, cv2.LINE_AA)
                else:
                    cv2.rectangle(img, (0, 180) , (640, 280), blue, -1)
                    cv2.putText(img, 'Draw', (200, 260), font, 3, black, 4, cv2.LINE_AA)
            elif winner == 'Player':
                cv2.rectangle(img, (0, 180) , (640, 285), blue, -1)
                cv2.putText(img, f'{winner} wins!', (55, 260), font, 3, black, 4, cv2.LINE_AA)
            else:
                cv2.rectangle(img, (0, 200) , (640, 280), blue, -1)
                cv2.putText(img, f'{winner} wins!', (90, 260), font, 2, black, 4, cv2.LINE_AA)
            
            
            cv2.imshow('Rock-Paper-Scissors Game', img)
            cv2.waitKey(1500)

        cv2.putText(frame, f'Player {player_score}', (85, 75), font, 1, black, 2, cv2.LINE_AA)  
        
        cv2.putText(frame, f'Computer {computer_score}', (355, 75), font, 1, black, 2, cv2.LINE_AA)  

        cv2.imshow('Rock-Paper-Scissors Game', frame)
        
        
        if computer_score == 3:        
            
            # turns the screen black
            cv2.rectangle(frame, (0, 0) , (640, 550), black, -1)
            
            cv2.putText(frame, 'Its over', (55, 160), font, 3, blue, 9, cv2.LINE_AA)
            
            cv2.putText(frame, 'Lost', (170, 320), font, 2, blue, 5, cv2.LINE_AA)
            
            cv2.imshow('Rock-Paper-Scissors', frame)

            cv2.waitKey(4000)
            cv2.destroyAllWindows()  
            break

        elif player_score == 3:
            
            # turns the screen red
            cv2.rectangle(frame, (0, 0) , (640, 550), blue, -1)

            cv2.putText(frame, 'Game Over', (58, 160), font, 3, black, 9, cv2.LINE_AA)

            cv2.putText(frame, 'Congratulations,', (190, 270), font, 1, black, 2, cv2.LINE_AA)
            
            cv2.putText(frame, 'You Win!', (180, 330), font, 2, black, 5, cv2.LINE_AA)
            
            cv2.imshow('Rock-Paper-Scissors', frame)
            
            cv2.waitKey(4000)
            cv2.destroyAllWindows()  
            break
        
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

_rock_paper_scissors_game()