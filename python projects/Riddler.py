print("Welcome to Riddler")
print("where you will try your best to solve 5 riddles")
print("Oh! I forgot to tell you that the answers are single worded")
playing = input("Do you dare to continue? ")
if playing.lower() != "yes":
    quit()
else:
    score = 0

    ques = input("What number of month(s) of the year has 28 days?(in words) ")
    ans = "twelve"
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
