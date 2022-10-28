points = 0

def test():
    addpoint = input("type ""add"" to add a point")
    if addpoint == "add":
        global points
        points += 1
        print(points)
        if points == 3:
            print("It's 3")
    else:
        print("asd")
    return
test()
test()
test()