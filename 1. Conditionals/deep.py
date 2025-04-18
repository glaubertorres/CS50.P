def main():
    question = (input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    question = question.casefold().capitalize().strip().replace("-", " ")

    if (question == "42" or question == "Forty two" or question == "forty-two"):
        print ("Yes")

    else:
        print("No")

main()