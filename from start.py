import random
import time
import cv2
from keras.models import load_model
import numpy as np

model = load_model(r'C:\Users\nilou\Desktop\AiCore\New model\converted_keras\keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image
    cv2.imshow('frame', frame)

    def play():

        prediction = model.predict(data)
        pool_choices = ["rock", "paper", "scissors"]
        random_index = random.randint(0, 2)
        ai_choice = pool_choices[random_index]

        if prediction[0][0] > 0.5:
            z = "rock"

        elif prediction[0][1] > 0.5:
            z = "paper"

        elif prediction[0][2] > 0.5:
            z = "scissors"

        else:
            z = "nothing"

        if z == ai_choice:
            return (0, z, ai_choice)

        if helper(z, ai_choice):
            return (1, z, ai_choice)

        return (-1, z, ai_choice)

    def helper (human, robot):
        if (human == "rock" and robot == "scissors") or (human == "scissors" and robot == "paper") or (human == "paper" and robot == "rock"):
            return True
        return False

    def real_winner():
        user_count = 0
        ai_count = 0
        while user_count < 3 and ai_count < 3:
            result, z, ai_choice = play()
           #tie
            if result == 0:
                print("You both have chosen {}.\n".format(z))

            elif result ==1:
                user_count += 1
                print("You have chosen {} and the computer has chosen {}. You won!\n".format(z, ai_choice))
            else:
                ai_count += 1
                print("You have chosen {} and the computer has chosen {}. You lost!. \n".format(z, ai_choice))
            print("\n")

        if user_count > ai_count:
            print("You have won 3 rounds!")
        else:
            print("You have lost 3 rounds!")

    real_winner()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()