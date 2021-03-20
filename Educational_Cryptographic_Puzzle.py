import time
import sys
import turtle as t
import tkinter

def welcome():
    introductoryLine = """Heya! Welcome over to this short mystery hunting game, or we can say a 'Puzzle' that is to solved, this 
    \n puzzle is inspired by the famous Cicada3301 that was a mystery a while back and sorted to seek out intelligent minds that within the
    \n internet community. The whole idea behind this project is to give you a feel in puzzle solving and see wheter you'd be interested
    \n in crypto, stegano and so on!:D. This can help you find an inner quality that you may have never imagined of! >.< \n 
    \n We hope that will be an adequate introduction to get you started over! So, here's the level 1 of this puzzle. Good luck decoding it! 
    \nRemember, You are allowed to have only 10 attempts per level, make it count!!
    \n"""
    
    for l in introductoryLine:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)
    
    print(r"myyux?44zuqtfi3|npnrjinf3twl4|npnujinf4htrrtsx4ymzrg4<4<<4LttlqjdNrfljxd756:dqtlt3x{l46755u}2LttlqjdNrfljxd756:dqtlt3x{l3usl5")
    for i in range(20):
        welcome_input = input()
        if welcome_input=="IHDR":
            level1()
            break
        else:
            if i>10:
                print("Perhaps take a break and think again")
                print("Exiting...")
                time.sleep(1)
                exit(0)
            continue
def level1():
    levelOne = """Woo! You've actually passed through that, crazy madlad!, well that was worth a praise if this is your
    \n absolute first time in solving puzzles. This has barely started, buckle up buckaroo, you'll have harder challenges up ahead! Nothing is impossible if
    \n you put your head down to work and think properly, that's how life works :D and... yeah, this puzzle as well. Let's 
    \n see if you can make it to the end of this challenge, lemme mention again, this is just to give you a feel in to encourage you for
    \n these kind of challenges. Students are often considered to absorb concepts easily when they find something fun and interesting! Assuming
    \n that you're a student (older? you're still doing a great job trying out new stuff!  have some more challenges ahead and get yourself
    \n more familiarised with these and go out hunting for puzzles in the real world! \n
    \n Now, let's see if your curious little mind can solve this one, trust me it's harder than it looks! :D \n\n"""
    
    for l in levelOne:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)

    print(r"kwwsv=22gulyh1jrrjoh1frp2gulyh2iroghuv24xLzUxH6PQ|UiStV\Uz}fXtrhL7}XzDDXBxvs@vkdulqj6/2")
    for i in range(20):
        level1_input = input()
        if level1_input == "IHDR":
            trollCheck = """Ahahahaha! Think you could fool me? Think harder, keep trying until you reach your limits!
            \n and maybe, give up on this if you're that desperate in fooling me. You've got a lot to learn :P \n"""
            for l in trollCheck:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(0.02)
        elif level1_input == "318" or level1_input=="317":
            level2()
        else:
            if i>10:
                print("Perhaps take a break and think again")
                print("Exiting...")
                time.sleep(1)
                exit(0)
            continue
def level2():
    levelTwo = """Great Job! You have a great puzzle solving skill, this can be harnessed greatly by doing more of these kinds of puzzles
    \n if you're interested, you can take up courses on stegano to deepen your interests on this field of study :D.
    \n Let's not get too excited... This one'll test your patience alot, and could be painful at times since it is quite different from what you would
    \n have solved earlier, don't worry I hate history as well, Good luck!  \n\n"""

    for l in levelTwo:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)

    print("Jr edfn dqg fkhfn wkh uljkwsdwk wkhuh lv vrphwklqj pruh")
    level2_input = input()
    for i in range(20):
        if level2_input == "7086395789":
            level3()
        else:
            if i>10:
                print("Perhaps take a break and think again")
                print("Exiting...")
                time.sleep(1)
                exit(0)
            continue

def level3():
    levelThree = """You have actually solved that?! That's... that's incredible! You'll enjoy the real world internet mysteries my friend. Now, this one is 
    \n designed to be REALLY challenging and I mean it when I say that, You'll have to spend a considerable amount of time on this one unless you're
    \n a secret pro who solves mysteries randomly while making peanut butter sandwiches... or maybe not, not the sandwiches. Anyways, we hope that you had a great
    \n time if you have solved it and... pity you if you haven't. Let's not get too excited shall we? Below is a website for whatever you may be solving one
    \n Good luck!(>.<)\n"""
    
    for l in levelThree:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)

    print(".... - - .--. ... ---... -..-. -..-. ....- -... -.. ..- .-.. ....- --.. .. --.. .-.-.- --. .. - .... ..- -... .-.-.- .. --- -..-. -.-. ... .. -....- ...- .. - -..-.")
    for i in range(20):
        level3_input = input()
        if level3_input == "2018":
            outro()
            exit(0) 
        else:
            if i>10:
                print("Perhaps take a break and think again")
                print("Exiting...")
                time.sleep(1)
                exit(0)
            continue
    
def outro():
    
    outroIntro = """That's all the challenges I got for today ;-;. You did incredibly well! :D. 
    Here's a fractal flower pattern as a reward (Check the graphics window! >.<)"""
    
    for l in outroIntro:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)
    
    levels = 4

    number_of_petals = 5

    size_of_first_flower = 90



    def center(d,x,y):
        t.goto(x, y-d)
        t.setheading(0)
        t.color("black","goldenrod")
        t.begin_fill()
        t.circle(d)
        t.end_fill()
        t.up()

    def petal(d,npetals,x,y,i,color):
        colors = ["MidnightBlue", "Navy", "MediumBlue", "RoyalBlue", "MediumSlateBlue", "CornflowerBlue"]
        t.down()
        t.color(colors[color%len(colors)])
        t.begin_fill()
        t.goto(x, y)
        t.setheading(360/npetals*i+90)
        t.right(45)
        t.circle(2.5*d,90)
        t.setheading(360/npetals*i+90+180)
        t.right(45)
        t.circle(2.5*d,90)
        t.end_fill()

    def flower(d,npetals,x,y,color):
        for i in range(npetals):
            petal(d,npetals,x,y,i,color)
        center(d,x,y)
        #t.tracer(n=0, delay=0)

    def flowers(n,petals, d, x, y, color):
        flower(d,petals,x,y,color)
        if n>1:

            t.goto(x, y+3/2*d)
            t.setheading(180)
            t.circle(3/2*d,-360/(2*petals))

            for i in range(petals):
                x,y,z= t.xcor(),t.ycor(),t.heading()
                flowers(n-1,petals, d/2, t.xcor(), t.ycor(), color+1)
                t.up()
                t.goto(x,y)
                t.setheading(z)
                t.circle(3/2*d,-360/petals)
        #t.tracer(n=0, delay=0)

    def main ():
        t.up()
        t.speed(-100)
        t.update()
        t.hideturtle()
        flowers(levels, number_of_petals, size_of_first_flower, 0, 0, 0)

        canvas = t.getcanvas()
        canvas.postscript(file="resultat_turtle.ps", colormode='color')
        t.tracer(n=0, delay=0)
        t.update()
    main()
    pass
welcome()



