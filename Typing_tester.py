from time import time

# calculating the accuray of input prompt
def typingerror(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if iwords[i] == words[i]:
                if(iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors +=1
    return  errors

# calculate the speed in word per minute
def typingspeed(iprompt,stime,etime):
    global time
    global iwords

    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords/time

    return speed

#     calculate total time elapsed
def timeElapsed(stime,etime):
    time = etime - stime
    return time

if __name__ == '__main__':
    prompt = "Hi, my name is Anjani Kumar, I am a coding instructor."
    print("Type this:- '", prompt,"'")

    # listening to imput Enter
    input("Press ENTER when you are ready!")

    # recording time for input
    stime = time()
    iprompt = input()
    etime = time()

    # gather all the information returned from functions
    time = round(timeElapsed(stime, etime), 2)
    speed = typingspeed(iprompt,stime,etime)
    errors = typingerror(prompt)

    # printing all the required data
    print("Total TIme Elapsed: ", time, "sec")
    print("Your average Typing Speed was: ", speed, "words/minute")
    print("With a total of: ", errors, "errors")