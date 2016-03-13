def isMorning(string):
    date = string.split(" ")
    date = date[1].split(":")
    hour = int(date[0])
    
    if (hour<10) or (hour>22):
        return True
    else:
        return False


