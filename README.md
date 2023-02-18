# gymnasium-giant-hamster-run

## TODO
1. Create a get_observation function using the MSS library to capture the game screen.
2. Run OpenCV on the result of the get_observation function to process the captured image.
3. Use Tesseract OCR to detect game over screen by checking if the text "Game Over" is present in the processed image.
4. Define a function to set reward for each ongoing frame, based on how long the agent has survived in the game.
5. Use Stable Baseline3 to create a Deep Q-Network (DQN) model to learn how to play the game environment using the observations and rewards.
6. Train the DQN model on the game environment using the processed observations and rewards.
7. Evaluate the performance of the trained DQN model on the game environment.
8. Fine-tune the DQN model and repeat steps 6 and 7 until satisfactory performance is achieved.
9. Save the trained DQN model to be used to play the game environment.
