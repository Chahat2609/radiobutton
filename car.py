command=""
while command!="quit":
    commmnad=input(">").lower()
    if command=="Start":
        print("car started")
    elif command=="stop":
        print("car stoped")
    elif command=="help":
        print('''
    start-to start the car
    stop-to stop the car
    quit-to quit
    ''')
   # elif command=="quit":
    #    break
    else:
        print("sorry")
