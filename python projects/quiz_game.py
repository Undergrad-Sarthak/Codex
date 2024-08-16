print("Welcome to quiz")
playing = input("Do you want to start the quiz?")
if playing.lower() != "yes" or playing.lower() != "y":
    quit()
else:
    score = 0
    print("here are the riddles with 1 word answers:")

    ques = input("What number of month(s) of the year has 28 days? ")
    ans = "12"
    if ques.lower() == ans:
        score += 1
        print("correct:", score, "/ 5")
    else:
        print("incorrect:", score, "/ 5")
        print("correct answer ->", ans)

    ques = input("What goes up but never comes down? ")
    ans = "age"
    if ques.lower() == ans:
        score += 1
        print("correct:", score, "/ 5")
    else:
        print("incorrect:", score, "/ 5")
        print("correct answer ->", ans)

    ques = input(
        "I follow you all the time and copy your every move, but you cannot touch me or catch me. What am I? "
    )
    ans = "shadow"
    if ques.lower() == ans:
        score += 1
        print("correct:", score, "/ 5")
    else:
        print("incorrect:", score, "/ 5")
        print("correct answer ->", ans)

    ques = input("The more of this there is, the less you see. What is it? ")
    ans = "darkness"
    if ques.lower() == ans:
        score += 1
        print("correct:", score, "/ 5")
    else:
        print("incorrect:", score, "/ 5")
        print("correct answer ->", ans)

    ques = input("What invention lets you look right through a wall? ")
    ans = "window"
    if ques.lower() == ans:
        score += 1
        print("correct:", score, "/ 5")
    else:
        print("incorrect:", score, "/ 5")
        print("correct answer ->", ans)

    print(score, "is your score.")
