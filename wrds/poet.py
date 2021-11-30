import colors as c
import os

def run():
    print(c.clear)
    print(c.yellow)
    print("""    
                            .-'''-.                                 
                           '   _    \                               
_________   _...._       /   /` '.   \      __.....__               
\        |.'      '-.   .   |     \  '  .-''         '.             
 \        .'```'.    '. |   '      |  '/     .-''"'-.  `.     .|   
  \      |       \     \\    \     / //     /________\   \   .' |_  
   |     |        |    | `.   ` ..' / |                  | .'     | 
   |      \      /    .     '-...-'`  \    .-------------''--.  .-' 
   |     |\`'-.-'   .'                 \    '-.____...---.   |  |   
   |     | '-....-'`                    `.             .'    |  |   
  .'     '.                               `''-...... -'      |  '.' 
'-----------'                                                |   /  
                                                             `'-' 
                            """+c.cyan+"""    Recording tool for Think-Aloud Protocol
    """)
    option=input(c.yellow+"Would you like to view old data? or create new data? (1), (2)"+c.reset+" >>>"+c.cyan)
    if option == '1':
        os.system('cat .data.txt')
        clean=input(c.yellow+'Would you like to delete this data? (Y/N)'+c.reset+' >>>'+c.cyan).strip().lower()
        if clean == 'y':
            os.system('rm .data.txt')
            print(c.yellow+'Data deleted!')
        elif clean == 'n':
            print(c.yellow+'Data saved!')
        else:
            print(c.yellow+'No answer provided. Data Kept.')
        input('[Press enter to continue]')
        print(c.clear)
        run()
    elif option == '2':
        perl()
    else:
        input('Invalid Response [Press enter to continue]')
        print(c.clear)
        run()

def perl():
    print(c.clear)
    print("""
          TALKING                            READING                                        WRITING

    General Planning [PL] 1      Reading the directions [RD] 14                      Writing silently [W] 22
    Local Planning [PLL] 2       Reading the question [RQ] 15                        Writing aloud [TW] 23
    Global Planning [PLG] 3      Reading the statement [R8] 16                       Editing [E] 24
    Commenting [C] 4             Reading one sentence or a few words [Ra] 17         Adding syntactic markers[Eadd] 25
    Interpreting [I] 5           Reading a number of sentences together [Ra-b] 18    Deleting [Edel] 26
    Assessing [A+] 6             Reading the entire draft through [RWI] 19           Grammar concern [Egr] 27
    Assessing [A-] 7             Control F [CF] 20                                   Punctuation [Epunc] 28
    Questioning [Q] 8            Lookup [LU] 21                                      Spelling [Esp] 29
    Talking While Writing [TW] 9                                                     Sentence structure [Ess] 30
    Talking leading to writing [T -- W] 10                                           Word choice concern [Ewc] 31
    Repeating [re] 11                                                                Verb form change [Evc] 32
    Silence [s] 12                                                                   Writing spellcheck [Ews] 33
    Reacting to distractions [RTD] 13
    """)
    print("enter [exit] to return to the menu.")
    prompt = input(c.yellow+"Input here"+c.reset+" >>> "+c.cyan).strip().upper()
    if prompt == "EXIT":
        print(c.clear)
        run()
    elif prompt == "1":
        os.system('date >> .data.txt')
        os.system('echo -   General Planning [PL] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "PL":
        os.system('date >> .data.txt')
        os.system('echo -   General Planning [PL] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "2":
        os.system('date >> .data.txt')
        os.system('echo -   Local Planning [PLL] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "PLL":
        os.system('date >> .data.txt')
        os.system('echo -   Local Planning [PLL] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "3":
        os.system('date >> .data.txt')
        os.system('echo -   Global Planning [PLG] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "PLG":
        os.system('date >> .data.txt')
        os.system('echo -   Global Planning [PLG] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "4":
        os.system('date >> .data.txt')
        os.system('echo -   Commenting [C] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "C":
        os.system('date >> .data.txt')
        os.system('echo -   Commenting [C] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "5":
        os.system('date >> .data.txt')
        os.system('echo -   Interpreting [I] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "I":
        os.system('date >> .data.txt')
        os.system('echo -   Interpreting [I] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "6":
        os.system('date >> .data.txt')
        os.system('echo -   Assessing A+ >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "A+":
        os.system('date >> .data.txt')
        os.system('echo -   Assessing A+ >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "7":
        os.system('date >> .data.txt')
        os.system('echo -   Assessing A-  >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "A-":
        os.system('date >> .data.txt')
        os.system('echo -   Assessing A- >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "8":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Questioning [Q] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "Q":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Questioning [Q] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "9":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Talking While Writing [TW] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "TW":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Talking While Writing [TW] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "10":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Talking leading to writing [T -- W] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "T -- W":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Talking leading to writing [T -- W] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "11":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Repeating [re] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "RE":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Repeating [re] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "12":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Silence [s] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "S":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Silence [s] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "13":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reacting to distractions [RTD] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "RTD":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reacting to distractions [RTD] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "14":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading the directions [RD] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "RD":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading the directions [RD] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "15":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading the question [RQ] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "RQ":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading the question [RQ] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "16":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading the statement [R8] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "R8":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading the statement [R8] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "17":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading one sentence or a few words [Ra] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "RA":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading one sentence or a few words [Ra] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "18":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading a number of sentences together [Ra-b] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "RA-B":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading a number of sentences together [Ra-b] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "19":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading the entire draft through [RWI] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "RWI":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Reading the entire draft through [RWI] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "20":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Control F [CF] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "CF":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Control F [CF] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "21":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Lookup [LU] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "LU":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Lookup [LU] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "22":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Writing silently [W] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "W":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Writing silently [W] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "23":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Writing aloud [TW] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "TW":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Writing aloud [TW] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "24":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Editing [E] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "E":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Editing [E] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "25":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Adding syntactic markers [Eadd] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "EADD":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Adding syntactic markers[Eadd] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "26":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Deleting [Edel] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "EDEL":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Deleting [Edel] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "27":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Grammar concern [Egr] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "EGR":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Grammar concern [Egr] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "28":
        os.system('date >> .data.txt')                                          
        os.system('echo -  Punctuation [Epunc]  >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "EPUNC":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Punctuation [Epunc] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "29":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Spelling [Esp] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "ESP":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Spelling [Esp] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "30":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Sentence structure [Ess] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "ESS":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Sentence structure [Ess] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "31":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Word choice concern [Ewc] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "EWC":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Word choice concern [Ewc] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "32":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Verb form change [Evc] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "EVC":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Verb form change [Evc] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "33":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Writing spellcheck [Ews] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    elif prompt == "EWS":
        os.system('date >> .data.txt')                                          
        os.system('echo -   Writing spellcheck [Ews] >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
    else:
        os.system('date >> .data.txt')
        os.system('echo -   '+prompt+' >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
        #os.system('bash notify')
        input('Message sent! [Press enter]')
    print(c.clear)
    perl()
    #else:
     #   print('Invalid Response')
      #  t.sleep(1)
       # print(c.clear)
        #run()

if __name__ == '__main__':

    while True:
        try:
            run()
        except(KeyboardInterrupt):
            print("Goodbye!")
            exit()
        except(EOFError):
            print("Goodbye!")
            exit()
