# Rock Paper Scissors 

Using webcam inputs, an  Computer Vision project will build a Rock, Paper, Scissors game. This project's main goal is to show how to use Python flow control.

The decisions and actions that were done at each stage of the project are described in this README.

Technologies used: Teachable-Machine, Python (keras, numpy, cv2, time, random)  Run camera rps.py to play the entire game with a camera.

## Create the Model

Using webcam inputs, Teachable-Machine was used to generate an image model with 4 classes (Rock, Paper, Scissors, Nothing). The number of epochs, learning rate, and batch size were all set to their default values. In order to reduce the possibility of overfitting, the photos that were taken for each class were intended to be different. Right- and left-handed motions were provided by three individuals from varied origins and with varying racial and gender identities. 

The model was downloaded for use in Tensorflow and saved to the repository.

## Install the Dependencies

created a reproducible environment in a virtual setting to manage dependencies. The necessary libraries were installed, and a requirements file was created so that the code could be run by another user or on a different device. Run model.py, a script with Python code, was used to execute the Keras model that was downloaded from Teachable-Machine.

# Create a Rock-Paper-Scissors Game

A script manual_rps.py that asks the user for text input in order to make their choice simulates a manual game of Rock-Paper-Scissors. Using the "random" library, the computer selects a choice at random from the possibilities. For clarity and code maintainability, the code has been written in functions with a single point of responsibility.  The game only proceeds after a valid input has been accepted. The routines developed to run the game as a whole are called via the play() function.

# Rock Paper Scissors Using Camera

The output from the run model.py file was combined with the functions to run the manual RPS game in a new script, which was then recast as a Class with accompanying methods. To make the game more user-friendly, logic and console prompts were added, such as the ability to repeat games until the desired number of victories is achieved (the default wins are set to 3), the provision of scores, and the need for a user prompt before moving on to the next round.

# Overall Reflection
With the help of this project, I was able to show that I could implement logic, write higher-quality code that adhered to PEP8 standards, included classes and methods, and was easier to read and run.