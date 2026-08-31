import time  # Importing the time module to measure the time taken for the typing test
import random # Importing the random module to select a random sentence for the typing test

sentences = ["Hii My Name is Ishant Bhardwaj", 
            "I am a student of B.Tech Computer Science", 
            "I am in my 3rd year of engineering", 
            "I love coding and problem solving",
            "Python is my favorite programming language"
]


def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0
    return accuracy

def typing_test(): 
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")


    print(test_sentence)
    input("Press Enter when you are ready...")
    start_time = time.time()
    user_input = input("\nStart typing:\n")
    end_time = time.time()
    time_taken = end_time - start_time 
    time_taken_minutes = time_taken / 60
    word_count = len(test_sentence.split(" ")) #what is teh use of split here? the use of split here is to break the test_sentence into individual words and count them. The split(" ") method splits the string into a list of words based on spaces, and then len() counts the number of words in that list. This is important for calculating the typing speed in words per minute (WPM).
    

    print("Results:")
    print(f"Time taken: {time_taken} seconds")
    print(f"Time taken: {time_taken_minutes:.2f} minutes")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {word_count / (time_taken / 60):.2f} words per minute")
    accuracy = measure_accuracy(user_input, test_sentence)
    # print(f"Accuracy: {accuracy:.2f}%")

typing_test()
