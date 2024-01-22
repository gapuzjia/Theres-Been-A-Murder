"""
Gapuz, Jianna (100%)

----------------------
Sources:
loops - https://www.youtube.com/watch?v=jSs58VZVLw8&t=197s

"""




repeat = 1
while True:
    while repeat == 1:
        suspicion_level = 0
        strategy_level = 0
        efficiency_level = 0
        print("""

            ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ████████╗██╗  ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
            ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
            ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║       ██║   ███████║█████╗      ██║  ███╗███████║██╔████╔██║█████╗  
            ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║       ██║   ██╔══██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
            ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝       ██║   ██║  ██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
             ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                                                                                """)
        print("                                                                    DO YOU WANT TO PLAY?")
        answer = input("""                                                                            Y/N
                                                                             """).upper().strip()
        while answer != "Y" and answer != "N":
            print("                                                                    DO YOU WANT TO PLAY?")
            answer = input("""                                                                            Y/N
                                                                             """).upper().strip()

        if answer == "Y":
            print("""

        ████████╗██╗  ██╗███████╗██████╗ ███████╗███████╗    ██████╗ ███████╗███████╗███╗   ██╗     █████╗     ███╗   ███╗██╗   ██╗██████╗ ██████╗ ███████╗██████╗ ██╗
        ╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔════╝████╗  ██║    ██╔══██╗    ████╗ ████║██║   ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██║
           ██║   ███████║█████╗  ██████╔╝█████╗  ███████╗    ██████╔╝█████╗  █████╗  ██╔██╗ ██║    ███████║    ██╔████╔██║██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝██║
           ██║   ██╔══██║██╔══╝  ██╔══██╗██╔══╝  ╚════██║    ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║    ██╔══██║    ██║╚██╔╝██║██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗╚═╝
           ██║   ██║  ██║███████╗██║  ██║███████╗███████║    ██████╔╝███████╗███████╗██║ ╚████║    ██║  ██║    ██║ ╚═╝ ██║╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║██╗
           ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝ 

                   """)
            dialogue = input("                                                                        [PRESS ENTER]")
            dialogue = input("The newspapers reported it as homicide.")
            dialogue = input("The killer attacked the victim with a knife, and fled the crime scene.")
            dialogue = input("The police are all over the place, and they're not getting anywhere with the investigation.")
            dialogue = input("Luckily, you like solving murder mysteries as a hobby.")
            dialogue = input("Oh yeah, and remember, this is technically illegal ehem ehem.")
            dialogue = input("You have to keep a low profile, but you also need to get the information needed to solve the crime.")
            dialogue = input("You could go the the police, but you'll get caught right away.")
            dialogue = input("You decide to go to the crime scene first.")
            dialogue = input("                                                                        [PRESS ENTER]")
            dialogue = input("You get to the crime scene.")
            dialogue = input("It's a small apartment on the sixth floor.")
            dialogue = input("You see the landlord.")
            ans = input("""Do you want to talk to him?
    A. Yes
    B. No
    Your choice: """).upper().strip()
            while ans != "A" and ans != "B":
                ans = input("""Invalid input.
Do you want to talk to him?
    A. Yes
    B. No
    Your choice: """).upper().strip()
            if ans == "A":
                suspicion_level = suspicion_level + 4
                dialogue = input("A. Yes.")
                dialogue = input("The landlord is old, so you have to talk a bit louder than usual.")
                dialogue = input("Landlord: Can I help you?")
                dialogue = input("You: Yes, I want to know a bit about the man who was murdered here.")
                dialogue = input("Landlord: Which one?")
                dialogue = input("That shocks you a bit.")
                dialogue = input("You: The most recent one?")
                dialogue = input("Landlord: I cant hear you. Speak louder.")
                ans = input("""Do you want to speak even louder? 
    A. Yes, speak louder 
    B. No, leave the landlord and see what you can find.
    Your choice: """).upper().strip()
                while ans != "A" and ans != "B":
                    ans = input("""Invalid input.
Do you want to speak even louder? 
    A. Yes, speak louder 
    B. No, leave the landlord and see what you can find.
    Your choice: """).upper().strip()
                if ans == "A":
                    suspicion_level = suspicion_level + 5
                    dialogue = input("A. Yes.")
                    dialogue = input("You've been caught.")
                    dialogue = input("You spoke so loud the police could hear you from six blocks away.")
                    print("G A M E  O V E R")
                    state = "ALIVE_GOTAWAY"
                elif ans == "B":
                    strategy_level = strategy_level + 2
                    dialogue = input("B. No.")
                    dialogue = input("You look around the crime scene.")
                    dialogue = input("The police searched hard, but not enough.")
                    dialogue = input("In the corner you see a vial. It has the letters R.T. on it.")
                    dialogue = input("The vial has an address on it.")
                    dialogue = input("You put the vial in your pocket.")
                    dialogue = input("You searched more, but there's nothing else except that.")
                    ans = input("""Where do you want to go next? 
    A. Go home, do some research about the vial. 
    B. Report it to the police. 
    C. Visit the morgue.
    Your answer: """).upper().strip()
                    while ans != "A" and ans != "B" and ans != "C":
                        ans = input("""Invalid input.
Where do you want to go next? 
    A. Go home, do some research about the vial. 
    B. Report it to the police. 
    C. Visit the morgue.
    Your answer: """).upper().strip()
                    # A ARC
                    if ans == "A":
                        strategy_level = strategy_level + 5
                        dialogue = input("A. Go home, do some research. ")
                        dialogue = input("The vial has the address of the local hospital on the vial.")
                        dialogue = input("You try to find out what the initials mean, but you're not in luck.")
                        dialogue = input("You ask your brother for help, since he has a knack for decoding things.")
                        dialogue = input("He went up to his room to see what he can find. ")
                        ans = input("""In the meantime, what do you want to do? 
    A. Report it to the police 
    B. Go to the morgue
    Your answer: """).upper().strip()
                        while ans != "A" and ans != "B":
                            ans = input("""Invalid input.
In the meantime, what do you want to do? 
    A. Report it to the police 
    B. Go to the morgue
    Your answer: """).upper().strip()
                        if ans == "A":
                            strategy_level = strategy_level - 4
                            dialogue = input("A.  Report it to the police ")
                            dialogue = input("You show the police what you found.")
                            dialogue = input("They warned you that you were too close to the crime scene.")
                            dialogue = input("They took the evidence and made you go home.")
                            ans = input("""What do you want to do next? 
    A. Back to the crime scene 
    B. The morgue
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B":
                                ans = input("""Invalid input.
What do you want to do next? 
    A. Back to the crime scene 
    B. The morgue
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level - 2
                                dialogue = input("A. Back to the crime scene ")
                                dialogue = input("You get to the crime scene.")
                                dialogue = input("You see the landlord.")
                                dialogue = input("Landlord: Hey you! Come here or I'll call the police!")
                                ans = input("""I guess you have to talk to him.
Talk to the landlord?
    A. Yes
    Your answer: """).upper().strip()
                                while ans != "A":
                                    ans = input("""You have no other choice.
Talk to the landlord?
    A. Yes
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level - 2
                                    dialogue = input("A.Yes. ")
                                    dialogue = input("The landlord is old, so you have to talk a bit louder than usual. ")
                                    dialogue = input("Landlord: Why are you here again?")
                                    dialogue = input("You: I want to know a bit about the man who was murdered here.")
                                    dialogue = input("Landlord: I can't hear you. Speak louder. ")
                                    dialogue = input("If you leave, he'll call the police for sure.")
                                    ans = input("""Do you want to speak even louder?
You have no other choice. 
    A. Yes, speak louder
    Your answer:""").upper().strip()
                                    while ans != "A":
                                        ans = input("""Do you want to speak even louder?
You have no other choice. 
    A. Yes, speak louder
    Your answer:""").upper().strip()
                                    if ans == "A":
                                        strategy_level = strategy_level - 3
                                        dialogue = input("A.Yes. ")
                                        dialogue = input("You've been caught.")
                                        dialogue = input("You spoke so loud the police could hear you from six blocks away.")
                                        print("G A M E  O V E R")
                                        state = "ALIVE_GOTAWAY"
                            elif ans == "B":
                                strategy_level = strategy_level + 3
                                dialogue = input("B. Visit the morgue ")
                                dialogue = input("You get to the morgue. You see the mortician. ")
                                ans = input("""Do you want to talk to him?
    A. Talk to him about the vial
    B. Ask him about the victim 
    C. Pretend you work there
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B" and ans != "C":
                                    ans = input("""Invalid input.
Do you want to talk to him?
    A. Talk to him about the vial
    B. Ask him about the victim 
    C. Pretend you work there
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level - 2
                                    dialogue = input("A. Talk to him about the vial ")
                                    dialogue = input("You ask him about the vial.")
                                    dialogue = input("He says he does not know.")
                                    dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                    dialogue = input( "The vial with the initials R.T. means Rhabdophis tigrinus, the snake. ")
                                    dialogue = input("It's from the lab, and the mortician stole that vial to poison the victim. ")
                                    dialogue = input("You died, he got away with it. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_GOTAWAY"
                                elif ans == "B":
                                    strategy_level = strategy_level + 2
                                    dialogue = input("B. Ask him about the victim ")
                                    dialogue = input("You: So, how did he die? ")
                                    dialogue = input("Mortician: Who are you? ")
                                    ans = input("""What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                                    while ans != "A" and ans != "B":
                                        ans = input("""Invalid input.
What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                                    if ans == "A":
                                        strategy_level = strategy_level + 4
                                        dialogue = input("A. Pretend you're with the police ")
                                        dialogue = input("You: I'm with the police.")
                                        dialogue = input( "Mortician: like I said last time, stabbed multiple times and bled to death.")
                                        dialogue = input( "You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                        dialogue = input("Mortician: Anything else?")
                                        ans = input("""What do you say?
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                        while ans != "A" and ans != "B":
                                            ans = input("""Invalid input.
What do you say?
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                        if ans == "A":
                                            strategy_level = strategy_level + 5
                                            dialogue = input("A. Go back home. ")
                                            dialogue = input( "You get back home. There's something fishy about the Mortician. ")
                                            dialogue = input("You fall asleep, then your brother wakes you up. ")
                                            dialogue = input("Brother: Rhabdophis tigrinus ")
                                            dialogue = input("You: What are you saying? ")
                                            dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                            dialogue = input("You start to put things together.")
                                            dialogue = input("Tiger keelback is a snake. ")
                                            dialogue = input("The address on the vial is the hospital. Hospitals need snake venom to make antidotes.")
                                            dialogue = input("The Mortician was clearly lying about something. ")
                                            dialogue = input("Then it hits you. ")
                                            dialogue = input( "The Mortician was trying to cover up how the victim died. ")
                                            dialogue = input("He didn't bleed to death, he was poisoned. ")
                                            dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                            dialogue = input("A day after, the Mortician is convicted of murder.")
                                            dialogue = input("You did it again.")
                                            dialogue = input("Till the next murder mystery, which might not be that far.")
                                            print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                            state = "ALIVE_CAUGHT"
                                        elif ans == "B":
                                            strategy_level = strategy_level - 2
                                            suspicion_level = suspicion_level + 3
                                            dialogue = input("B.Talk to him about the vial ")
                                            dialogue = input("You ask him about the vial.")
                                            dialogue = input("He says he does not know.")
                                            dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                            dialogue = input("Luckily, your brother cracked the code and called the police. ")
                                            dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. ")
                                            dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim.")
                                            dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                            print("G A M E  O V E R")
                                            state = "DEAD_CAUGHT"
                                    elif ans == "B":
                                        strategy_level = strategy_level - 3
                                        suspicion_level = suspicion_level + 4
                                        dialogue = input("B. Be honest. ")
                                        dialogue = input("You: The police clearly aren't getting anywhere with the investigation so I'm taking it into my own hands. ")
                                        dialogue = input("The Mortician looks at you.")
                                        dialogue = input("Once you turn your back against him, you feel a sharp stabbing.")
                                        dialogue = input("The Mortician stabbed you in the back, literally.")
                                        dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. ")
                                        dialogue = input( "It's from the lab, and the Mortician stole that vial to poison the victim.")
                                        dialogue = input("The Mortician got away. Oh well.")
                                        print("G A M E  O V E R")
                                elif ans == "C":
                                    strategy_level = strategy_level + 4
                                    dialogue = input("C. Pretend you work there.")
                                    dialogue = input( "So you go around the morgue, acting as if you know what you're doing.")
                                    dialogue = input("You pull up the file of the murder victim, and the Mortician approaches you. ")
                                    dialogue = input("Mortician: That file has been approved. It should be in archives and inaccessible to anyone. Give them to me.")
                                    dialogue = input("You: But how did he die?")
                                    dialogue = input("Mortician: Multiple stabs, bled to death.")
                                    dialogue = input("He walks away with the file. ")
                                    dialogue = input( "You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                    dialogue = input("You know that there is no such rule as archiving autopsy reports. ")
                                    ans = input("""What do you do next?
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                                    while ans != "A" and ans != "B":
                                        ans = input("""Invalid input.
What do you do next?
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                                    if ans == "A":
                                        strategy_level = strategy_level - 2
                                        dialogue = input("A. Talk to him about the vial ")
                                        dialogue = input("You ask him about the vial.")
                                        dialogue = input("He says he does not know.")
                                        dialogue = input("When you turn your back, he stabs repeatedly until you die. ")
                                        dialogue = input("Luckily, your brother cracked the code and called the police.")
                                        dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. ")
                                        dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                        dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                        print("G A M E  O V E R")
                                        state = "DEAD_CAUGHT"
                                    elif ans == "B":
                                        strategy_level = strategy_level + 3
                                        dialogue = input("B. Go back home. ")
                                        dialogue = input("You get back home. ")
                                        dialogue = input("There's something fishy about the Mortician. ")
                                        dialogue = input("You fall asleep, then your brother wakes you up. ")
                                        dialogue = input("Brother: Rhabdophis tigrinus ")
                                        dialogue = input("You: what are you saying?")
                                        dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback.  ")
                                        dialogue = input("You start to put things together.")
                                        dialogue = input("Tiger keelback is a snake.")
                                        dialogue = input("The address on the vial is the hospital.")
                                        dialogue = input("Hospitals need snake venom to make antidotes.")
                                        dialogue = input("The Mortician was clearly lying about something.")
                                        dialogue = input("Then it hits you.")
                                        dialogue = input("The Mortician was trying to cover up how the victim died.")
                                        dialogue = input("He didn't bleed to death, he was poisoned. ")
                                        dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                        dialogue = input("A day after, the Mortician is convicted of murder. ")
                                        dialogue = input("You did it again.")
                                        dialogue = input("Till the next murder mystery, which might not be that far.")
                                        print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                        state = "ALIVE_CAUGHT"
                        elif ans == "B":
                            strategy_level = strategy_level + 2
                            dialogue = input("B. Visit the morgue ")
                            dialogue = input("You get to the morgue. You see the Mortician. ")
                            ans = input("""Do you want to talk to him? 
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B" and ans != "C":
                                ans = input("""Invalid input.
Do you want to talk to him? 
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level - 3
                                suspicion_level = suspicion_level + 4
                                dialogue = input("A. Talk to him about the vial")
                                dialogue = input("You ask him about the vial.")
                                dialogue = input("He says he does not know.")
                                dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus.")
                                dialogue = input("It's the tiger keelback, a venomous snake.")
                                dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                dialogue = input("Luckily, your brother cracked the code and called the police.")
                                dialogue = input("The police caught the Mortician, but you died. Oh well. ")
                                print("G A M E  O V E R")
                                state = "DEAD_CAUGHT"
                            elif ans == "B":
                                strategy_level = strategy_level + 2
                                dialogue = input("B. Ask him about the victim ")
                                dialogue = input("You: so, how did he die?")
                                dialogue = input("Mortician: who are you? ")
                                ans = input("""What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level + 2
                                    dialogue = input("A. Pretend you're with the police")
                                    dialogue = input("You: I'm with the police.")
                                    dialogue = input("Mortician: like I said last time, stabbed multiple times and bled to death.")
                                    dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                    dialogue = input("Mortician: Anything else? ")
                                    ans = input("""What do you say? 
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                    while ans != "A" and ans != "B":
                                        ans = input("""Invalid input.
What do you say? 
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                    if ans == "A":
                                        strategy_level = strategy_level + 4
                                        dialogue = input("A.Go back home. ")
                                        dialogue = input("You get back home. There's something fishy about the Mortician. ")
                                        dialogue = input("You fall asleep, then your brother wakes you up. ")
                                        dialogue = input("Brother: Rhabdophis tigrinus.")
                                        dialogue = input("You: what are you saying? ")
                                        dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                        dialogue = input("You start to put things together")
                                        dialogue = input("Tiger keelback is a snake.")
                                        dialogue = input("The address on the vial is the hospital. Hospitals need snake venom to make antidotes.")
                                        dialogue = input("The Mortician was clearly lying about something. ")
                                        dialogue = input("Then it hits you. ")
                                        dialogue = input("The Mortician was trying to cover up how the victim died. ")
                                        dialogue = input("He didn't bleed to death, he was poisoned. ")
                                        dialogue = input( "You write it all down in an anonymous letter and send it to the police.")
                                        dialogue = input("A day after, the Mortician is convicted of murder. ")
                                        dialogue = input("You did it again. ")
                                        dialogue = input("Till the next murder mystery, which might not be that far.")
                                        print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                        state = "ALIVE_CAUGHT"
                                    elif ans == "B":
                                        strategy_level = strategy_level - 2
                                        suspicion_level = suspicion_level + 2
                                        dialogue = input("B.Talk to him about the vial ")
                                        dialogue = input("You ask him about the vial.")
                                        dialogue = input("He says he does not know.")
                                        dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                        dialogue = input("Luckily, your brother cracked the code and called the police.")
                                        dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake.")
                                        dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim.")
                                        dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                        print("G A M E  O V E R")
                                        state = "DEAD_CAUGHT"
                                elif ans == "B":
                                    strategy_level = strategy_level - 3
                                    dialogue = input("B. Be honest. ")
                                    dialogue = input("You say who you are.")
                                    dialogue = input("You: The police clearly aren't getting anywhere with the investigation so I'm taking it into my own hands. ")
                                    dialogue = input("The Mortician looks at you.")
                                    dialogue = input("Once you turn your back against him, you feel a sharp stabbing.")
                                    dialogue = input("The Mortician stabbed you in the back, literally.")
                                    dialogue = input("Luckily, your brother cracked the code and called the police.")
                                    dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake.")
                                    dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim.")
                                    dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_CAUGHT"
                            elif ans == "C":
                                strategy_level = strategy_level + 4
                                dialogue = input("C. Pretend you work there ")
                                dialogue = input("So you go around the morgue, acting as if you know what you're doing.")
                                dialogue = input("You pull up the file of the murder victim, and the Mortician approaches you. ")
                                dialogue = input("Mortician: That file has been approved. It should be in archives and inaccessible to anyone. Give them to me. ")
                                dialogue = input("You: But how did he die?")
                                dialogue = input("Mortician: multiple stabs, bled to death.")
                                dialogue = input("He walks away with the file. ")
                                dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                dialogue = input("You know that there is no such rule as archiving autopsy reports. ")
                                ans = input("""What do you do next?
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you do next?
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level - 3
                                    suspicion_level = suspicion_level + 3
                                    dialogue = input("A. Talk to him about the vial ")
                                    dialogue = input("You ask him about the vial.")
                                    dialogue = input("He says he does not know.")
                                    dialogue = input("When you turn your back, he stabs repeatedly until you die. ")
                                    dialogue = input("Luckily, your brother cracked the code and called the police. ")
                                    dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus.")
                                    dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim.")
                                    dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_CAUGHT"
                                elif ans == "B":
                                    strategy_level = strategy_level + 4
                                    dialogue = input("B.Go back home. ")
                                    dialogue = input("You get back home. ")
                                    dialogue = input("There's something fishy about the Mortician.")
                                    dialogue = input("You fall asleep, then your brother wakes you up. ")
                                    dialogue = input("Brother: Rhabdophis tigrinus. ")
                                    dialogue = input("You: What are you saying?")
                                    dialogue = input("Brother: RT stands for Rhabdophis tigrinus.")
                                    dialogue = input("Scientific name for the tiger keelback.")
                                    dialogue = input("You start to put things together. ")
                                    dialogue = input("Tiger keelback is a snake.")
                                    dialogue = input("The address on the vial is the hospital.")
                                    dialogue = input("Hospitals need snake venom to make antidotes.")
                                    dialogue = input("The Mortician was clearly lying about something.")
                                    dialogue = input("Then it hits you.")
                                    dialogue = input("The Mortician was trying to cover up how the victim died.")
                                    dialogue = input("He didn't bleed to death, he was poisoned. ")
                                    dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                    dialogue = input("A day after, the Mortician is convicted of murder. ")
                                    dialogue = input("You did it again. ")
                                    dialogue = input("Till the next murder mystery, which might not be that far.")
                                    print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                    state = "ALIVE_CAUGHT"
                    # B ARC
                    if ans == "B":
                        strategy_level = strategy_level - 2
                        suspicion_level = suspicion_level + 4
                        dialogue = input("B. Report it to the police ")
                        dialogue = input("You show the police what you found. ")
                        dialogue = input("They warned you that you were too close to the crime scene. ")
                        dialogue = input("They took the evidence and made you go home.")
                        ans = input("""What do you want to do next? 
    A. Back to the crime scene 
    B. The morgue
    Your answer: """).upper().strip()
                        while ans != "A" and ans != "B":
                            ans = input("""Invalid input.
What do you want to do next? 
    A. Back to the crime scene 
    B. The morgue
    Your answer: """).upper().strip()
                        if ans == "A":
                            suspicion_level = suspicion_level + 3
                            strategy_level = strategy_level - 2
                            dialogue = input("A. Back to the crime scene ")
                            dialogue = input("You get to the crime scene.")
                            dialogue = input("It's a small apartment on the sixth floor.")
                            dialogue = input("You see the landlord. ")
                            ans = input("""Do you want to talk to him? 
    A. Yes.
    Your answer: """).upper().strip()
                            while ans != "A":
                                ans = input("""Invalid input.
Do you want to talk to him? 
    A. Yes.
    Your answer: """).upper().strip()
                            if ans == "A":
                                suspicion_level = suspicion_level + 3
                                dialogue = input("A.Yes. ")
                                dialogue = input("The landlord is old, so you have to talk a bit louder than usual. ")
                                dialogue = input("Landlord: can i help you?")
                                dialogue = input("You: yes, i want to know a bit about the man who was murdered here ")
                                dialogue = input("Landlord: which one? ")
                                dialogue = input("That shocks you a bit. ")
                                dialogue = input("You: the most recent one?")
                                dialogue = input("Landlord: i cant hear you. Speak louder. ")
                                ans = input("""Do you want to speak even louder? 
    A. Yes, speak louder 
    Your answer: """).upper().strip()
                                while ans != "A":
                                    ans = input("""Invalid input.
Do you want to speak even louder? 
    A. Yes, speak louder 
    Your answer: """).upper().strip()
                                if ans == "A":
                                    suspicion_level = suspicion_level + 2
                                    dialogue = input("Yes.")
                                    dialogue = input("You've been caught. You spoke so loud the police could hear you from six blocks away.")
                                    print("G A M E   O V E R")
                                    state = "ALIVE_CAUGHT"
                        elif ans == "B":
                            strategy_level = strategy_level + 2
                            dialogue = input("B. Visit the morgue ")
                            dialogue = input("You get to the morgue. You see the Mortician. ")
                            ans = input("""Do you want to talk to him? 
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B" and ans != "C":
                                ans = input("""Invalid input.
Do you want to talk to him? 
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there.
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level - 3
                                dialogue = input("A. Talk to him about the vial ")
                                dialogue = input("You ask him about the vial.")
                                dialogue = input("He says he does not know.")
                                dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake, is from the lab, and the Mortician stole that vial to poison the victim. ")
                                dialogue = input("You died, he got away with it. Oh well.")
                                print("G A M E   O V E R")
                                state = "DEAD_GOTAWAY"
                            elif ans == "B":
                                strategy_level = strategy_level + 1
                                dialogue = input("B. Ask him about the victim")
                                dialogue = input("You: so, how did he die? ")
                                dialogue = input("Mortician: who are you? ")
                                ans = input("""What do you want to do?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you want to do?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level + 2
                                    dialogue = input("A. Pretend you're with the police ")
                                    dialogue = input("You: I'm with the police. ")
                                    dialogue = input("Mortician: like I said last time, stabbed multiple times and bled to death.")
                                    dialogue = input( "You were at the crime scene, and you saw blood, but not enough for someone to die of it.")
                                    dialogue = input("Mortician: Anything else? ")
                                    ans = input("""What do you say?
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                    while ans != "A" and ans != "B":
                                        ans = input("""Invalid input.
What do you say?
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                    if ans == "A":
                                        strategy_level = strategy_level + 2
                                        dialogue = input("A.Go back home.")
                                        dialogue = input("You get back home. There's something fishy about the Mortician. ")
                                        dialogue = input("You tell your brother about the vial, since he has a knack for decoding things.")
                                        dialogue = input("You fall asleep, then your brother wakes you up. ")
                                        dialogue = input("Brother: Rhabdophis tigrinus")
                                        dialogue = input("You: what are you saying? ")
                                        dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                        dialogue = input("You start to put things together. ")
                                        dialogue = input( "Tiger keelback is a snake. The address on the vial is the hospital.")
                                        dialogue = input("Hospitals need snake venom to make antidotes.")
                                        dialogue = input("The Mortician was clearly lying about something. ")
                                        dialogue = input("Then it hits you. ")
                                        dialogue = input("The Mortician was trying to cover up how the victim died. ")
                                        dialogue = input("He didn't bleed to death, he was poisoned. ")
                                        dialogue = input("You write it all down in a letter and send it to the police")
                                        dialogue = input("A day after, the Mortician is convicted of murder. ")
                                        dialogue = input("You did it again. ")
                                        dialogue = input("Till the next murder mystery, which might not be that far.")
                                        print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                        state = "ALIVE_CAUGHT"
                                    elif ans == "B":
                                        strategy_level = strategy_level - 3
                                        suspicion_level = suspicion_level + 3
                                        dialogue = input("B.Talk to him about the vial ")
                                        dialogue = input("You ask him about the vial.")
                                        dialogue = input("He says he does not know. ")
                                        dialogue = input("When you turn your back, he stabs you repeatedly until you die.")
                                        dialogue = input("The Mortician stabbed you in the back, literally.")
                                        dialogue = input( "The vial with the initials R.T. means Rhabdophis tigrinus, the snake. It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                        dialogue = input("You died, and the Mortician got away. Oh well.")
                                        print("G A M E  O V E R")
                                        state = "DEAD_GOTAWAY"
                                elif ans == "B":
                                    strategy_level = strategy_level - 4
                                    dialogue = input("B.Be honest. ")
                                    dialogue = input("You say who you are.")
                                    dialogue = input("You: The police clearly aren't getting anywhere with the investigation so i'm taking it into my own hands.")
                                    dialogue = input("The Mortician looks at you.")
                                    dialogue = input("Once you turn your back against him, you feel a sharp stabbing.")
                                    dialogue = input("The Mortician stabbed you in the back, literally.")
                                    dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                    dialogue = input("You died, and the Mortician got away. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_GOTAWAY"
                            elif ans == "C":
                                strategy_level = strategy_level + 3
                                dialogue = input("C. Pretend you work there ")
                                dialogue = input( "So you go around the morgue, acting as if you know what you're doing.")
                                dialogue = input("You pull up the file of the murder victim, and the Mortician approaches you. ")
                                dialogue = input("Mortician: That file has been approved. It should be in archives and inaccessible to anyone. Give them to me. ")
                                dialogue = input("You: But how did he die?")
                                dialogue = input("Mortician: Multiple stabs, bled to death.")
                                dialogue = input("He walks away with the file. ")
                                dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                dialogue = input("You know that there is no such rule as archiving autopsy reports. ")
                                ans = input("""What do you do next? 
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you do next? 
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level - 2
                                    dialogue = input("A. Talk to him about the vial ")
                                    dialogue = input("You ask him about the vial.")
                                    dialogue = input("He says he does not know.")
                                    dialogue = input("When you turn your back, he stabs repeatedly until you die. ")
                                    dialogue = input("Luckily, your brother cracked the code and called the police.")
                                    dialogue = input("The vial with the initials R.T., which means Rhabdophis tigrinus, the snake.")
                                    dialogue = input("It was from the lab, and the Mortician stole that vial to poison the victim.")
                                    dialogue = input("You died, and the Mortician got away. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_GOTAWAY"
                                elif ans == "B":
                                    strategy_level = strategy_level + 4
                                    dialogue = input("B.Go back home. ")
                                    dialogue = input("You get back home. ")
                                    dialogue = input("There's something fishy about the Mortician. ")
                                    dialogue = input("You tell your brother about the vial, since he has a knack for decoding things. ")
                                    dialogue = input("You fall asleep, then your brother wakes you up. ")
                                    dialogue = input("Brother: Rhabdophis tigrinus")
                                    dialogue = input("You: what are you saying?")
                                    dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                    dialogue = input("You start to put things together. ")
                                    dialogue = input("Tiger keelback is a snake.")
                                    dialogue = input("The address on the vial is the hospital.")
                                    dialogue = input("Hospitals need snake venom to make antidotes.")
                                    dialogue = input("The Mortician was clearly lying about something")
                                    dialogue = input("Then it hits you. ")
                                    dialogue = input("The Mortician was trying to cover up how the victim died.")
                                    dialogue = input("He didn't bleed to death, he was poisoned.")
                                    dialogue = input( "You write it all down in an anonymous letter and send it to the police.")
                                    dialogue = input("A day after, the Mortician is convicted of murder. ")
                                    dialogue = input("You did it again.")
                                    dialogue = input("Till the next murder mystery, which might not be that far.")
                                    print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                    state = "ALIVE_CAUGHT"
                    # C ARC
                    elif ans == "C":
                        strategy_level = strategy_level + 2
                        efficiency_level = efficiency_level + 3
                        dialogue = input("C. Visit the morgue ")
                        dialogue = input("You get to the morgue. You see the Mortician. ")
                        ans = input("""Do you want to talk to him?
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                        while ans != "A" and ans != "B" and ans != "C":
                            ans = input("""Invalid input.
Do you want to talk to him?
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                        if ans == "A":
                            strategy_level = strategy_level - 3
                            dialogue = input("A. Talk to him about the vial ")
                            dialogue = input("You ask him about the vial.")
                            dialogue = input("He says he does not know.")
                            dialogue = input("When you turn your back, he stabs repeatedly until you die. ")
                            dialogue = input( "The vial with the initials R.T. stands for Rhabdophis tigrinus, the snake.")
                            dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                            dialogue = input("You died, he got away with it. Oh well.")
                            print("G A M E  O V E R")
                            state = "DEAD_GOTAWAY"
                        elif ans == "B":
                            strategy_level = strategy_level + 2
                            dialogue = input("B. Ask him about the victim")
                            dialogue = input("You: So, how did he die? ")
                            dialogue = input("Mortician: Who are you? ")
                            ans = input("""What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B":
                                ans = input("""Invalid input.
What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level + 4
                                dialogue = input("A. Pretend you're with the police")
                                dialogue = input("You: I'm with the police. ")
                                dialogue = input("Mortician: like I said last time, stabbed multiple times and bled to death.")
                                dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                dialogue = input("Mortician: Anything else?")
                                ans = input("""What do you say?
    A. That would be all.
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you say?
    A. That would be all.
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level + 3
                                    efficiency_level = efficiency_level + 2
                                    dialogue = input("A. Go back home. ")
                                    dialogue = input("You get back home. There's something fishy about the Mortician.")
                                    dialogue = input( "You tell your brother about the vial, and he says he'll see what he can do, since he has a knack for decoding things. ")
                                    dialogue = input("You fall asleep, then your brother wakes you up. ")
                                    dialogue = input("Brother: Rhabdophis tigrinus ")
                                    dialogue = input("You: What are you saying? ")
                                    dialogue = input( "Brother: R.T. stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                    dialogue = input("You start to put things together. ")
                                    dialogue = input("Tiger keelback is a snake.")
                                    dialogue = input( "The address on the vial is the hospital. Hospitals need snake venom to make antidotes. ")
                                    dialogue = input("The Mortician was clearly lying about something. ")
                                    dialogue = input("Then it hits you.")
                                    dialogue = input("The Mortician was trying to cover up how the victim died. ")
                                    dialogue = input("He didn't bleed to death, he was poisoned. ")
                                    dialogue = input( "You write it all down in an anonymous letter and send it to the police.")
                                    dialogue = input("A day after, the Mortician is convicted of murder. ")
                                    dialogue = input("You did it again.")
                                    dialogue = input("Till the next murder mystery, which might not be that far.")
                                    print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                    state = "ALIVE_CAUGHT"
                                elif ans == "B":
                                    strategy_level = strategy_level - 5
                                    dialogue = input("B.Talk to him about the vial ")
                                    dialogue = input("You ask him about the vial.")
                                    dialogue = input("He says he does not know. ")
                                    dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                    dialogue = input("The vial with the initials R.T. mean Rhabdophis tigrinus, the snake.")
                                    dialogue = input( "It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                    dialogue = input("You died, and the Mortician got away. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_GOTAWAY"
                            elif ans == "B":
                                strategy_level = strategy_level - 4
                                dialogue = input("B.Be honest. ")
                                dialogue = input("You: The police clearly aren't getting anywhere with the investigation so i'm taking it into my own hands. ")
                                dialogue = input("The Mortician looks at you.")
                                dialogue = input("Once you turn your back against him, you feel a sharp stabbing.")
                                dialogue = input("The Mortician stabbed you in the back, literally.")
                                dialogue = input( "The vial with the initials R.T. stands for Rhabdophis tigrinus, the snake.")
                                dialogue = input( "It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                dialogue = input("You died, he got away with it. Oh well.")
                                print("G A M E  O V E R")
                                state = "DEAD_GOTAWAY"
                        elif ans == "C":
                            strategy_level = strategy_level + 4
                            dialogue = input("C. Pretend you work there ")
                            dialogue = input("So you go around the morgue, acting as if you know what you're doing.")
                            dialogue = input( "You pull up the file of the murder victim, and the Mortician approaches you. ")
                            dialogue = input("Mortician: That file has been approved. It should be in archives and inaccessible to anyone. Give them to me.")
                            dialogue = input("You: But how did he die?")
                            dialogue = input("Mortician: Multiple stabs, bled to death.")
                            dialogue = input("He walks away with the file.")
                            dialogue = input( "You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                            dialogue = input("You know that there is no such rule as archiving autopsy reports. ")
                            ans = input("""What do you do next?
    A. Ask about the vial
    B. Go back home
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B":
                                ans = input("""Invalid input.
What do you do next?
    A. Ask about the vial
    B. Go back home
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level - 3
                                dialogue = input("A. Talk to him about the vial ")
                                dialogue = input("You ask him about the vial.")
                                dialogue = input("He says he does not know.")
                                dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                dialogue = input("The vial with the initials R.T. mean Rhabdophis tigrinus, the snake.")
                                dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                dialogue = input("You died, and the Mortician got away with it. Oh well.")
                                print("G A M E  O V E R")
                                state = "DEAD_GOTAWAY"
                            elif ans == "B":
                                strategy_level = strategy_level + 3
                                dialogue = input("B.Go back home. ")
                                dialogue = input("You get back home. ")
                                dialogue = input("There's something fishy about the Mortician. ")
                                dialogue = input("You fall asleep, then your brother wakes you up. ")
                                dialogue = input("Brother: Rhabdophis tigrinus ")
                                dialogue = input("You: What are you saying? ")
                                dialogue = input( "Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                dialogue = input("You start to put things together. ")
                                dialogue = input("Tiger keelback is a snake. ")
                                dialogue = input( "The address on the vial is the hospital. Hospitals need snake venom to make antidotes.")
                                dialogue = input("The Mortician was clearly lying about something.")
                                dialogue = input("Then it hits you.")
                                dialogue = input("The Mortician was trying to cover up how the victim died")
                                dialogue = input("He didn't bleed to death, he was poisoned. ")
                                dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                dialogue = input("A day after, the Mortician is convicted of murder. ")
                                dialogue = input("You did it again.")
                                dialogue = input("Till the next murder mystery, which might not be that far.")
                                print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                state = "ALIVE_CAUGHT"
# DID NOT TALK TO LANDLORD
            elif ans == "B":
                efficiency_level = efficiency_level + 3
                strategy_level = strategy_level + 2
                dialogue = input("B. No.")
                dialogue = input("You look around the crime scene.")
                dialogue = input("The police searched hard, but not enough.")
                dialogue = input("In the corner you see a vial. It has the letters R.T. on it.")
                dialogue = input("On the vial, there's an address.")
                dialogue = input("You put the vial in your pocket.")
                dialogue = input("You searched more, but there's nothing else except that.")
                ans = input("""Where do you want to go next? 
    A. Go home, do some research about the vial. 
    B. Report it to the police. 
    C. Visit the morgue.
    Your answer: """).upper().strip()
                while ans != "A" and ans != "B" and ans != "C":
                    ans = input("""Invalid input.
Where do you want to go next? 
    A. Go home, do some research about the vial. 
    B. Report it to the police. 
    C. Visit the morgue.
    Your answer: """).upper().strip()
                # A ARC
                if ans == "A":
                    strategy_level = strategy_level + 2
                    dialogue = input("A. Go home, do some research. ")
                    dialogue = input("The vial has the address of the local hospital on the vial.")
                    dialogue = input("You try to find out what the initials mean, but you're not in luck.")
                    dialogue = input("You ask your brother for help.")
                    dialogue = input("He went up to his room to see what he can find. ")
                    ans = input("""In the meantime, what do you want to do? 
    A. Report it to the police 
    B. Go to the morgue
    Your answer: """).upper().strip()
                    while ans != "A" and ans != "B":
                        ans = input("""Invalid input.
In the meantime, what do you want to do? 
    A. Report it to the police 
    B. Go to the morgue
    Your answer: """).upper().strip()
                    if ans == "A":
                        suspicion_level = suspicion_level + 4
                        dialogue = input("A.  Report it to the police ")
                        dialogue = input("You show the police what you found.")
                        dialogue = input("They warned you that you were too close to the crime scene.")
                        dialogue = input("They took the evidence and made you go home.")
                        ans = input("""What do you want to do next? 
    A. Back to the crime scene 
    B. The morgue
    Your answer: """).upper().strip()
                        while ans != "A" and ans != "B":
                            ans = input("""Invalid input.
What do you want to do next? 
    A. Back to the crime scene 
    B. The morgue
    Your answer: """).upper().strip()
                        if ans == "A":
                            suspicion_level = suspicion_level + 3
                            dialogue = input("A. Back to the crime scene ")
                            dialogue = input("You get to the crime scene.")
                            dialogue = input("You see the landlord.")
                            dialogue = input("Landlord: Hey you! Come here or I'll call the police!")
                            ans = input("""I guess you have to talk to him.
Talk to the landlord?
    A. Yes
    Your answer: """).upper().strip()
                            while ans != "A":
                                suspicion_level = suspicion_level + 3
                                ans = input("""You have no other choice.
Talk to the landlord?
    A. Yes
    Your answer: """).upper().strip()
                            if ans == "A":
                                suspicion_level = suspicion_level + 3
                                strategy_level = strategy_level - 2
                                dialogue = input("A.Yes. ")
                                dialogue = input("The landlord is old, so you have to talk a bit louder than usual. ")
                                dialogue = input("Landlord: Why are you here again?")
                                dialogue = input("You: I want to know a bit about the man who was murdered here.")
                                dialogue = input("Landlord: I can't hear you. Speak louder. ")
                                dialogue = input("If you leave, he'll call the police for sure.")
                                ans = input("""Do you want to speak even louder?
You have no other choice. 
    A. Yes, speak louder
    Your answer:""").upper().strip()
                                while ans != "A":
                                    strategy_level = strategy_level - 3
                                    ans = input("""Do you want to speak even louder?
You have no other choice. 
    A. Yes, speak louder
    Your answer:""").upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level - 2
                                    dialogue = input("A.Yes. ")
                                    dialogue = input("You've been caught.")
                                    dialogue = input( "You spoke so loud the police could hear you from six blocks away.")
                                    print("G A M E  O V E R")
                        elif ans == "B":
                            strategy_level = strategy_level + 2
                            dialogue = input("B. Visit the morgue ")
                            dialogue = input("You get to the morgue. You see the Mortician. ")
                            ans = input("""Do you want to talk to him?
    A. Talk to him about the vial
    B. Ask him about the victim 
    C. Pretend you work there
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B" and ans != "C":
                                ans = input("""Invalid input.
Do you want to talk to him?
    A. Talk to him about the vial
    B. Ask him about the victim 
    C. Pretend you work there
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level - 3
                                dialogue = input("A. Talk to him about the vial ")
                                dialogue = input("You ask him about the vial.")
                                dialogue = input("He says he does not know.")
                                dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. ")
                                dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                dialogue = input("You died, he got away with it. Oh well.")
                                print("G A M E  O V E R")
                                state = "DEAD_GOTAWAY"
                            elif ans == "B":
                                strategy_level = strategy_level + 2
                                dialogue = input("B. Ask him about the victim ")
                                dialogue = input("You: So, how did he die? ")
                                dialogue = input("Mortician: Who are you? ")
                                ans = input("""What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level + 3
                                    dialogue = input("A. Pretend you're with the police ")
                                    dialogue = input("You: I'm with the police.")
                                    dialogue = input( "Mortician: like I said last time, stabbed multiple times and bled to death.")
                                    dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                    dialogue = input("Mortician: Anything else?")
                                    ans = input("""What do you say?
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                    while ans != "A" and ans != "B":
                                        ans = input("""Invalid input.
What do you say?
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                    if ans == "A":
                                        strategy_level = strategy_level + 3
                                        dialogue = input("A.Go back home. ")
                                        dialogue = input("You get back home. There's something fishy about the Mortician. ")
                                        dialogue = input("You fall asleep, then your brother wakes you up. ")
                                        dialogue = input("Brother: Rhabdophis tigrinus ")
                                        dialogue = input("You: What are you saying? ")
                                        dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback.  ")
                                        dialogue = input("You start to put things together.")
                                        dialogue = input("Tiger keelback is a snake. ")
                                        dialogue = input("The address on the vial is the hospital. Hospitals need snake venom to make antidotes.")
                                        dialogue = input("The Mortician was clearly lying about something. ")
                                        dialogue = input("Then it hits you. ")
                                        dialogue = input("The Mortician was trying to cover up how the victim died. ")
                                        dialogue = input("He didn't bleed to death, he was poisoned. ")
                                        dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                        dialogue = input("A day after, the Mortician is convicted of murder.")
                                        dialogue = input("You did it again.")
                                        dialogue = input("Till the next murder mystery, which might not be that far.")
                                        print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                        state = "ALIVE_CAUGHT"
                                    elif ans == "B":
                                        strategy_level = strategy_level - 3
                                        dialogue = input("B.Talk to him about the vial ")
                                        dialogue = input("You ask him about the vial.")
                                        dialogue = input("He says he does not know.")
                                        dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                        dialogue = input("Luckily, your brother cracked the code and called the police. ")
                                        dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. ")
                                        dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim.")
                                        dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                        print("G A M E  O V E R")
                                        state = "DEAD_CAUGHT"
                                elif ans == "B":
                                    strategy_level = strategy_level - 3
                                    dialogue = input("B.Be honest. ")
                                    dialogue = input("You: The police clearly aren't getting anywhere with the investigation so I'm taking it into my own hands. ")
                                    dialogue = input("The Mortician looks at you.")
                                    dialogue = input("Once you turn your back against him, you feel a sharp stabbing.")
                                    dialogue = input("The Mortician stabbed you in the back, literally.")
                                    dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. ")
                                    dialogue = input( "It's from the lab, and the Mortician stole that vial to poison the victim.")
                                    dialogue = input("You died, the Mortician got away. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_GOTAWAY"
                            elif ans == "C":
                                strategy_level = strategy_level + 2
                                dialogue = input("C. Pretend you work there.")
                                dialogue = input("So you go around the morgue, acting as if you know what you're doing.")
                                dialogue = input("You pull up the file of the murder victim, and the Mortician approaches you. ")
                                dialogue = input("Mortician: That file has been approved. It should be in archives and inaccessible to anyone. Give them to me.")
                                dialogue = input("You: But how did he die?")
                                dialogue = input("Mortician: Multiple stabs, bled to death.")
                                dialogue = input("He walks away with the file. ")
                                dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                dialogue = input("You know that there is no such rule as archiving autopsy reports. ")
                                ans = input("""What do you do next?
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you do next?
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level - 3
                                    dialogue = input("A. Talk to him about the vial ")
                                    dialogue = input("You ask him about the vial.")
                                    dialogue = input("He says he does not know.")
                                    dialogue = input("When you turn your back, he stabs repeatedly until you die. ")
                                    dialogue = input("Luckily, your brother cracked the code and called the police.")
                                    dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. ")
                                    dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                    dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_CAUGHT"
                                elif ans == "B":
                                    strategy_level = strategy_level + 3
                                    dialogue = input("B. Go back home. ")
                                    dialogue = input("You get back home. ")
                                    dialogue = input("There's something fishy about the Mortician. ")
                                    dialogue = input("You fall asleep, then your brother wakes you up. ")
                                    dialogue = input("Brother: Rhabdophis tigrinus ")
                                    dialogue = input("You: what are you saying?")
                                    dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback.  ")
                                    dialogue = input("You start to put things together.")
                                    dialogue = input("Tiger keelback is a snake.")
                                    dialogue = input("The address on the vial is the hospital.")
                                    dialogue = input("Hospitals need snake venom to make antidotes.")
                                    dialogue = input("The Mortician was clearly lying about something.")
                                    dialogue = input("Then it hits you.")
                                    dialogue = input("The Mortician was trying to cover up how the victim died.")
                                    dialogue = input("He didn't bleed to death, he was poisoned. ")
                                    dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                    dialogue = input("A day after, the Mortician is convicted of murder. ")
                                    dialogue = input("You did it again.")
                                    dialogue = input("Till the next murder mystery, which might not be that far.")
                                    print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                    state = "ALIVE_CAUGHT"
                    elif ans == "B":
                        strategy_level = strategy_level + 3
                        efficiency_level = efficiency_level + 3
                        dialogue = input("B. Visit the morgue ")
                        dialogue = input("You get to the morgue. You see the Mortician. ")
                        ans = input("""Do you want to talk to him? 
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                        while ans != "A" and ans != "B" and ans != "C":
                            ans = input("""Invalid input.
Do you want to talk to him? 
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                        if ans == "A":
                            strategy_level = strategy_level - 2
                            dialogue = input("A. Talk to him about the vial")
                            dialogue = input("You ask him about the vial.")
                            dialogue = input("He says he does not know.")
                            dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                            dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus.")
                            dialogue = input("It's the tiger keelback, a venomous snake.")
                            dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                            dialogue = input("You died, he got away with it. Oh well.")
                            print("G A M E  O V E R")
                            state = "DEAD_GOTAWAY"
                        elif ans == "B":
                            strategy_level = strategy_level - 3
                            dialogue = input("B. Ask him about the victim ")
                            dialogue = input("You: so, how did he die?")
                            dialogue = input("Mortician: who are you? ")
                            ans = input("""What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B":
                                ans = input("""Invalid input.
What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level + 3
                                dialogue = input("A. Pretend you're with the police")
                                dialogue = input("You: I'm with the police.")
                                dialogue = input("Mortician: like I said last time, stabbed multiple times and bled to death.")
                                dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                                dialogue = input("Mortician: Anything else? ")
                                ans = input("""What do you say? 
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you say? 
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level + 3
                                    dialogue = input("A.Go back home. ")
                                    dialogue = input("You get back home. There's something fishy about the Mortician. ")
                                    dialogue = input("You fall asleep, then your brother wakes you up. ")
                                    dialogue = input("Brother: Rhabdophis tigrinus.")
                                    dialogue = input("You: what are you saying? ")
                                    dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                    dialogue = input("You start to put things together")
                                    dialogue = input("Tiger keelback is a snake.")
                                    dialogue = input("The address on the vial is the hospital. Hospitals need snake venom to make antidotes.")
                                    dialogue = input("The Mortician was clearly lying about something. ")
                                    dialogue = input("Then it hits you. ")
                                    dialogue = input("The Mortician was trying to cover up how the victim died. ")
                                    dialogue = input("He didn't bleed to death, he was poisoned. ")
                                    dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                    dialogue = input("A day after, the Mortician is convicted of murder. ")
                                    dialogue = input("You did it again. ")
                                    dialogue = input("Till the next murder mystery, which might not be that far.")
                                    print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                    state = "ALIVE_CAUGHT"
                                elif ans == "B":
                                    strategy_level = strategy_level - 2
                                    dialogue = input("B.Talk to him about the vial ")
                                    dialogue = input("You ask him about the vial.")
                                    dialogue = input("He says he does not know.")
                                    dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                    dialogue = input("Luckily, your brother cracked the code and called the police.")
                                    dialogue = input( "The vial with the initials R.T. means Rhabdophis tigrinus, the snake.")
                                    dialogue = input( "It's from the lab, and the Mortician stole that vial to poison the victim.")
                                    dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_CAUGHT"
                            elif ans == "B":
                                strategy_level = strategy_level - 3
                                dialogue = input("B. Be honest. ")
                                dialogue = input("You say who you are.")
                                dialogue = input("You: The police clearly aren't getting anywhere with the investigation so I'm taking it into my own hands. ")
                                dialogue = input("The Mortician looks at you.")
                                dialogue = input("Once you turn your back against him, you feel a sharp stabbing.")
                                dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake.")
                                dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim.")
                                dialogue = input("The Mortician stabbed you in the back, literally.")
                                dialogue = input("You died, and the Mortician got away. Oh well.")
                                print("G A M E  O V E R")
                                state = "DEAD_GOTAWAY"
                        elif ans == "C":
                            strategy_level = strategy_level + 3
                            dialogue = input("C. Pretend you work there ")
                            dialogue = input("So you go around the morgue, acting as if you know what you're doing.")
                            dialogue = input("You pull up the file of the murder victim, and the Mortician approaches you. ")
                            dialogue = input("Mortician: That file has been approved. It should be in archives and inaccessible to anyone. Give them to me. ")
                            dialogue = input("You: But how did he die?")
                            dialogue = input("Mortician: multiple stabs, bled to death.")
                            dialogue = input("He walks away with the file. ")
                            dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                            dialogue = input("You know that there is no such rule as archiving autopsy reports. ")
                            ans = input("""What do you do next?
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B":
                                ans = input("""Invalid input.
What do you do next?
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level - 2
                                dialogue = input("A. Talk to him about the vial ")
                                dialogue = input("You ask him about the vial.")
                                dialogue = input("He says he does not know.")
                                dialogue = input("When you turn your back, he stabs repeatedly until you die. ")
                                dialogue = input("Luckily, your brother cracked the code and called the police. ")
                                dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus.")
                                dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim.")
                                dialogue = input("The police caught the Mortician, but you died. Oh well.")
                                print("G A M E  O V E R")
                                state = "DEAD_CAUGHT"
                            elif ans == "B":
                                strategy_level = strategy_level + 3
                                dialogue = input("B.Go back home. ")
                                dialogue = input("You get back home. ")
                                dialogue = input("There's something fishy about the Mortician.")
                                dialogue = input("You fall asleep, then your brother wakes you up. ")
                                dialogue = input("Brother: Rhabdophis tigrinus. ")
                                dialogue = input("You: What are you saying?")
                                dialogue = input("Brother: RT stands for Rhabdophis tigrinus.")
                                dialogue = input("Scientific name for the tiger keelback.")
                                dialogue = input("You start to put things together. ")
                                dialogue = input("Tiger keelback is a snake.")
                                dialogue = input("The address on the vial is the hospital.")
                                dialogue = input("Hospitals need snake venom to make antidotes.")
                                dialogue = input("The Mortician was clearly lying about something.")
                                dialogue = input("Then it hits you.")
                                dialogue = input("The Mortician was trying to cover up how the victim died.")
                                dialogue = input("He didn't bleed to death, he was poisoned. ")
                                dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                dialogue = input("A day after, the Mortician is convicted of murder. ")
                                dialogue = input("You did it again. ")
                                dialogue = input("Till the next murder mystery, which might not be that far.")
                                print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                state = "ALIVE_CAUGHT"

                # B ARC
                elif ans == "B":
                    strategy_level = strategy_level - 2
                    suspicion_level = suspicion_level + 3
                    dialogue = input("B. Report it to the police ")
                    dialogue = input("You show the police what you found. ")
                    dialogue = input("They warned you that you were too close to the crime scene. ")
                    dialogue = input("They took the evidence and made you go home.")
                    ans = input("""What do you want to do next? 
    A. Back to the crime scene 
    B. The morgue
    Your answer: """).upper().strip()
                    while ans != "A" and ans != "B":
                        ans = input("""Invalid input.
What do you want to do next? 
    A. Back to the crime scene 
    B. The morgue
    Your answer: """).upper().strip()
                    if ans == "A":
                        strategy_level = strategy_level - 2
                        suspicion_level = suspicion_level + 3
                        dialogue = input("A. Back to the crime scene ")
                        dialogue = input("You get to the crime scene.")
                        dialogue = input("It's a small apartment on the sixth floor.")
                        dialogue = input("You see the landlord. ")
                        ans = input("""Do you want to talk to him? 
    A. Yes.
    Your answer: """).upper().strip()
                        while ans != "A":
                            ans = input("""Invalid input.
Do you want to talk to him? 
    A. Yes.
    Your answer: """).upper().strip()
                        if ans == "A":
                            suspicion_level = suspicion_level + 2
                            strategy_level = strategy_level - 3
                            dialogue = input("A.Yes. ")
                            dialogue = input("The landlord is old, so you have to talk a bit louder than usual. ")
                            dialogue = input("Landlord: can i help you?")
                            dialogue = input("You: yes, i want to know a bit about the man who was murdered here ")
                            dialogue = input("Landlord: which one? ")
                            dialogue = input("That shocks you a bit. ")
                            dialogue = input("You: the most recent one?")
                            dialogue = input("Landlord: i cant hear you. Speak louder. ")
                            ans = input("""Do you want to speak even louder? 
    A. Yes, speak louder 
    Your answer: """).upper().strip()
                            while ans != "A":
                                ans = input("""Invalid input.
Do you want to speak even louder? 
    A. Yes, speak louder 
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level - 2
                                dialogue = input("Yes.")
                                dialogue = input(
                                    "You've been caught. You spoke so loud the police could hear you from six blocks away.")
                                print("G A M E   O V E R")
                                state = "ALIVE_GOTAWAY"
                    elif ans == "B":
                        strategy_level = strategy_level + 3
                        dialogue = input("B. Visit the morgue ")
                        dialogue = input("You get to the morgue. You see the Mortician. ")
                        ans = input("""Do you want to talk to him? 
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                        while ans != "A" and ans != "B" and ans != "C":
                            ans = input("""Invalid input.
Do you want to talk to him? 
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there.
    Your answer: """).upper().strip()
                        if ans == "A":
                            strategy_level = strategy_level - 3
                            dialogue = input("A. Talk to him about the vial ")
                            dialogue = input("You ask him about the vial.")
                            dialogue = input("He says he does not know.")
                            dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                            dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake, is from the lab, and the Mortician stole that vial to poison the victim. ")
                            dialogue = input("You died, he got away with it. Oh well.")
                            print("G A M E   O V E R")
                            state = "DEAD_GOTAWAY"
                        elif ans == "B":
                            strategy_level = strategy_level + 1
                            dialogue = input("B. Ask him about the victim")
                            dialogue = input("You: so, how did he die? ")
                            dialogue = input("Mortician: who are you? ")
                            ans = input("""What do you want to do?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B":
                                ans = input("""Invalid input.
What do you want to do?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level + 3
                                dialogue = input("A. Pretend you're with the police ")
                                dialogue = input("You: I'm with the police. ")
                                dialogue = input( "Mortician: like I said last time, stabbed multiple times and bled to death.")
                                dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it.")
                                dialogue = input("Mortician: Anything else? ")
                                ans = input("""What do you say?
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                while ans != "A" and ans != "B":
                                    ans = input("""Invalid input.
What do you say?
    A. That would be all. 
    B. Ask about the vial.
    Your answer: """).upper().strip()
                                if ans == "A":
                                    strategy_level = strategy_level + 3
                                    dialogue = input("A.Go back home.")
                                    dialogue = input( "You get back home. There's something fishy about the Mortician. ")
                                    dialogue = input("You tell your brother about the vial, since he has a knack for decoding things. ")
                                    dialogue = input("You fall asleep, then your brother wakes you up. ")
                                    dialogue = input("Brother: Rhabdophis tigrinus")
                                    dialogue = input("You: what are you saying? ")
                                    dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                    dialogue = input("You start to put things together. ")
                                    dialogue = input("Tiger keelback is a snake. The address on the vial is the hospital.")
                                    dialogue = input("Hospitals need snake venom to make antidotes.")
                                    dialogue = input("The Mortician was clearly lying about something. ")
                                    dialogue = input("Then it hits you. ")
                                    dialogue = input("The Mortician was trying to cover up how the victim died. ")
                                    dialogue = input("He didn't bleed to death, he was poisoned. ")
                                    dialogue = input("You write it all down in a letter and send it to the police")
                                    dialogue = input("A day after, the Mortician is convicted of murder. ")
                                    dialogue = input("You did it again. ")
                                    dialogue = input("Till the next murder mystery, which might not be that far.")
                                    print ("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                    state = "ALIVE_CAUGHT"
                                elif ans == "B":
                                    strategy_level = strategy_level - 3
                                    dialogue = input("B.Talk to him about the vial ")
                                    dialogue = input("You ask him about the vial.")
                                    dialogue = input("He says he does not know. ")
                                    dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                    dialogue = input("Luckily, your brother cracked the code and called the police.")
                                    dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                    dialogue = input("You died, and the Mortician got away. Oh well.")
                                    print("G A M E  O V E R")
                                    state = "DEAD_GOTAWAY"
                            elif ans == "B":
                                strategy_level = strategy_level - 3
                                dialogue = input("B.Be honest. ")
                                dialogue = input("You say who you are.")
                                dialogue = input("You: The police clearly aren't getting anywhere with the investigation so i'm taking it into my own hands.")
                                dialogue = input("The Mortician looks at you.")
                                dialogue = input("Once you turn your back against him, you feel a sharp stabbing.")
                                dialogue = input("The Mortician stabbed you in the back, literally.")
                                dialogue = input("The vial with the initials R.T. means Rhabdophis tigrinus, the snake. It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                dialogue = input("You died, and the Mortician got away. Oh well.")
                                print("G A M E  O V E R")
                                state = "DEAD_GOTAWAY"
                        elif ans == "C":
                            strategy_level = strategy_level + 3
                            dialogue = input("C. Pretend you work there ")
                            dialogue = input("So you go around the morgue, acting as if you know what you're doing.")
                            dialogue = input("You pull up the file of the murder victim, and the Mortician approaches you. ")
                            dialogue = input("Mortician: That file has been approved. It should be in archives and inaccessible to anyone. Give them to me. ")
                            dialogue = input("You: But how did he die?")
                            dialogue = input("Mortician: Multiple stabs, bled to death.")
                            dialogue = input("He walks away with the file. ")
                            dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                            dialogue = input("You know that there is no such rule as archiving autopsy reports. ")
                            ans = input("""What do you do next? 
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B":
                                ans = input("""Invalid input.
What do you do next? 
    A. Ask about the vial 
    B. Go back home
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level - 3
                                dialogue = input("A. Talk to him about the vial ")
                                dialogue = input("You ask him about the vial.")
                                dialogue = input("He says he does not know.")
                                dialogue = input("When you turn your back, he stabs repeatedly until you die. ")
                                dialogue = input("Luckily, your brother cracked the code and called the police.")
                                dialogue = input("The vial with the initials R.T., which means Rhabdophis tigrinus, the snake.")
                                dialogue = input("It was from the lab, and the Mortician stole that vial to poison the victim.")
                                dialogue = input("You died, and the Mortician got away with it. Oh well.")
                                print("G A M E  O V E R")
                                state = "DEAD_GOTAWAY"
                            elif ans == "B":
                                strategy_level = strategy_level + 3
                                dialogue = input("B.Go back home. ")
                                dialogue = input("You get back home. ")
                                dialogue = input("There's something fishy about the Mortician. ")
                                dialogue = input("You tell your brother about the vial, since he has a knack for decoding things. ")
                                dialogue = input("You fall asleep, then your brother wakes you up. ")
                                dialogue = input("Brother: Rhabdophis tigrinus")
                                dialogue = input("You: what are you saying?")
                                dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                dialogue = input("You start to put things together. ")
                                dialogue = input("Tiger keelback is a snake.")
                                dialogue = input("The address on the vial is the hospital.")
                                dialogue = input("Hospitals need snake venom to make antidotes.")
                                dialogue = input("The Mortician was clearly lying about something")
                                dialogue = input("Then it hits you. ")
                                dialogue = input("The Mortician was trying to cover up how the victim died.")
                                dialogue = input("He didn't bleed to death, he was poisoned.")
                                dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                dialogue = input("A day after, the Mortician is convicted of murder. ")
                                dialogue = input("You did it again.")
                                dialogue = input("Till the next murder mystery, which might not be that far.")
                                print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                state = "ALIVE_CAUGHT"
                # C ARC
                elif ans == "C":
                    efficiency_level = efficiency_level + 3
                    strategy_level = strategy_level + 2
                    dialogue = input("C. Visit the morgue ")
                    dialogue = input("You get to the morgue. You see the Mortician. ")
                    ans = input("""Do you want to talk to him?
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                    while ans != "A" and ans != "B" and ans != "C":
                        ans = input("""Do you want to talk to him?
    A. Talk to him about the vial 
    B. Ask him about the victim. 
    C. Pretend you work there
    Your answer: """).upper().strip()
                    if ans == "A":
                        strategy_level = strategy_level - 3
                        dialogue = input("A. Talk to him about the vial ")
                        dialogue = input("You ask him about the vial.")
                        dialogue = input("He says he does not know.")
                        dialogue = input("When you turn your back, he stabs repeatedly until you die. ")
                        dialogue = input("The vial with the initials R.T. stands for Rhabdophis tigrinus, the snake.")
                        dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                        dialogue = input("You died, he got away with it. Oh well.")
                        print("G A M E  O V E R")
                        state = "DEAD_GOTAWAY"
                    elif ans == "B":
                        strategy_level = strategy_level + 2
                        dialogue = input("B. Ask him about the victim")
                        dialogue = input("You: So, how did he die? ")
                        dialogue = input("Mortician: Who are you? ")
                        ans = input("""What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                        while ans != "A" and ans != "B":
                            ans = input("""Invalid input.
What do you say?
    A. Pretend you're with the police 
    B. Be honest.
    Your answer: """).upper().strip()
                        if ans == "A":
                            strategy_level = strategy_level + 3
                            dialogue = input("A. Pretend you're with the police")
                            dialogue = input("You: I'm with the police. ")
                            dialogue = input("Mortician: like I said last time, stabbed multiple times and bled to death.")
                            dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                            dialogue = input("D: Anything else?")
                            ans = input("""What do you say?
    A. That would be all.
    B. Ask about the vial.
    Your answer: """).upper().strip()
                            while ans != "A" and ans != "B":
                                ans = input("""Invalid input.
What do you say?
    A. That would be all.
    B. Ask about the vial.
    Your answer: """).upper().strip()
                            if ans == "A":
                                strategy_level = strategy_level + 2
                                dialogue = input("A.Go back home. ")
                                dialogue = input("You get back home. There's something fishy about the Mortician.")
                                dialogue = input("You tell your brother about the vial, and he says he'll see what he can do, since he has a knack for decoding things. ")
                                dialogue = input("You fall asleep, then your brother wakes you up. ")
                                dialogue = input("Brother: Rhabdophis tigrinus ")
                                dialogue = input("You: What are you saying? ")
                                dialogue = input("Brother: R.T. stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                                dialogue = input("You start to put things together. ")
                                dialogue = input("Tiger keelback is a snake.")
                                dialogue = input("The address on the vial is the hospital. Hospitals need snake venom to make antidotes. ")
                                dialogue = input("The Mortician was clearly lying about something. ")
                                dialogue = input("Then it hits you.")
                                dialogue = input("The Mortician was trying to cover up how the victim died. ")
                                dialogue = input("He didn't bleed to death, he was poisoned. ")
                                dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                                dialogue = input("A day after, the Mortician is convicted of murder. ")
                                dialogue = input("You did it again.")
                                dialogue = input("Till the next murder mystery, which might not be that far.")
                                print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                                state = "ALIVE_CAUGHT"
                            elif ans == "B":
                                strategy_level = strategy_level - 3
                                dialogue = input("B.Talk to him about the vial ")
                                dialogue = input("You ask him about the vial.")
                                dialogue = input("He says he does not know. ")
                                dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                                dialogue = input("The vial with the initials R.T. mean Rhabdophis tigrinus")
                                dialogue = input( "It's from the lab, and the Mortician stole that vial to poison the victim. ")
                                dialogue = input("You died, oh well.")
                                print("G A M E  O V E R")
                                state = "DEAD_GOTAWAY"
                        elif ans == "B":
                            strategy_level = strategy_level - 2
                            dialogue = input("B. Be honest. ")
                            dialogue = input("You: The police clearly aren't getting anywhere with the investigation so i'm taking it into my own hands. ")
                            dialogue = input("The Mortician looks at you.")
                            dialogue = input("Once you turn your back against him, you feel a sharp stabbing.")
                            dialogue = input("The Mortician stabbed you in the back, literally.")
                            dialogue = input("The vial with the initials R.T. stands for Rhabdophis tigrinus, the snake.")
                            dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                            dialogue = input("You died, he got away with it. Oh well.")
                            print("G A M E  O V E R")
                            state = "DEAD_GOTAWAY"
                    elif ans == "C":
                        strategy_level = strategy_level + 3
                        dialogue = input("C. Pretend you work there ")
                        dialogue = input("So you go around the morgue, acting as if you know what you're doing.")
                        dialogue = input("You pull up the file of the murder victim, and the Mortician approaches you. ")
                        dialogue = input("Mortician: That file has been approved. It should be in archives and inaccessible to anyone. Give them to me.")
                        dialogue = input("You: But how did he die?")
                        dialogue = input("Mortician: Multiple stabs, bled to death.")
                        dialogue = input("He walks away with the file.")
                        dialogue = input("You were at the crime scene, and you saw blood, but not enough for someone to die of it. ")
                        dialogue = input("You know that there is no such rule as archiving autopsy reports. ")
                        ans = input("""What do you do next?
    A. Ask about the vial
    B. Go back home
    Your answer: """).upper().strip()
                        while ans != "A" and ans != "B":
                            ans = input("""Invalid input.
What do you do next?
    A. Ask about the vial
    B. Go back home
    Your answer: """).upper().strip()
                        if ans == "A":
                            strategy_level = strategy_level - 2
                            dialogue = input("A. Talk to him about the vial ")
                            dialogue = input("You ask him about the vial.")
                            dialogue = input("He says he does not know.")
                            dialogue = input("When you turn your back, he stabs repeatedly until you die.")
                            dialogue = input("The vial with the initials R.T. mean Rhabdophis tigrinus, the snake.")
                            dialogue = input("It's from the lab, and the Mortician stole that vial to poison the victim. ")
                            dialogue = input("You died, and the Mortician got away with it. Oh well.")
                            print("G A M E  O V E R")
                            state = "DEAD_GOTAWAY"
                        elif ans == "B":
                            strategy_level = strategy_level + 3
                            dialogue = input("B.Go back home. ")
                            dialogue = input("You get back home. ")
                            dialogue = input("There's something fishy about the Mortician. ")
                            dialogue = input("You fall asleep, then your brother wakes you up. ")
                            dialogue = input("Brother: Rhabdophis tigrinus ")
                            dialogue = input("You: What are you saying? ")
                            dialogue = input("Brother: RT stands for Rhabdophis tigrinus. Scientific name for the tiger keelback. ")
                            dialogue = input("You start to put things together. ")
                            dialogue = input("Tiger keelback is a snake. ")
                            dialogue = input("The address on the vial is the hospital. Hospitals need snake venom to make antidotes.")
                            dialogue = input("The Mortician was clearly lying about something.")
                            dialogue = input("Then it hits you.")
                            dialogue = input("The Mortician was trying to cover up how the victim died")
                            dialogue = input("He didn't bleed to death, he was poisoned. ")
                            dialogue = input("You write it all down in an anonymous letter and send it to the police.")
                            dialogue = input("A day after, the Mortician is convicted of murder. ")
                            dialogue = input("You did it again.")
                            dialogue = input("Till the next murder mystery, which might not be that far.")
                            print("Y O U  C R A C K E D  T H E  C A S E ! ! !")
                            state = "ALIVE_CAUGHT"

            stats = input("--------------")
            if state == "ALIVE_GOTAWAY":
                if strategy_level < 10:
                   print("You were a good sleuth, but for this mystery, not good enough.")
                if suspicion_level >= 8:
                    print("The police were on to you from the beginning. ")
            elif state == "ALIVE_CAUGHT":
                if efficiency_level == 6:
                    print("You solved this case with the quickest route possible. ")
                if efficiency_level < 6:
                    print(" You solved the crime, but you could've done that faster. Any slower, the Mortician might have gotten away. ")
                if strategy_level >= 10:
                    print(" Great strategist, you are. ")
                if suspicion_level < 8:
                    print("Another case solved, and you’re still in the shadows. The police are still looking for you, the mystery sleuth who solves cases the police can’t. ")
                if suspicion_level >= 8:
                    print("You solved the case, but the police were on to you. You almost got caught. ")
            elif state == "DEAD_GOTAWAY":
                if strategy_level < 10:
                    print("You were a good sleuth, but for this mystery, not good enough. ")
                if strategy_level >= 10:
                    print(" You may have amazing strategy, but strategy isn't enough to solve a crime. ")
                if suspicion_level < 8:
                    print("You were stealthy, but a bit too stealthy. The police found your body, and couldn't identify who you were. Your murder ended up being forgotten by the police. ")
                if suspicion_level >= 8:
                    print("Not only did the Mortician get away, the police didn’t bother to investigate your murder. They say you were in the wrong place at the wrong time, anyway. ")
            elif state == "DEAD_CAUGHT":
                if strategy_level >= 10:
                    print("Your brother studies your strategy how you went about solving mysteries as he carries on what you started.")
                if suspicion_level < 8:
                    print("Your brother mourns your death. He decides to resume your role, as the mystery sleuth who solves cases the police can't.")
                if suspicion_level >= 8:
                    print("Your brother may have solved the case, but the police arrested him for intervening with a classified case. He got sent to jail. ")

            stats = input("--------------")
            stats = input("STATS")

            print("Suspicion Level:   " , suspicion_level)

            print("Strategy Level:    " , strategy_level)

            print("Efficiency Level:  " , efficiency_level)

            repeat = input("Do you want to play again? [Y/N]: ").upper().strip()
            while repeat != "Y" and repeat != "N":
                repeat = input("Invalid input. \n Do you want to play again? [Y/N]: ").upper().strip()
            if repeat == "Y":
                repeat = 1
            elif repeat == "N":
                print("fine then :(((")
                repeat = 0
        elif answer == "N":
            print("ok then :(((")
            repeat = 0



















