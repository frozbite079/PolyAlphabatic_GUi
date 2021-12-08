from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import pyttsx3


def  build():
    app =QApplication(sys.argv)
    win = QTabWidget()

    engine = pyttsx3.init()
    
    ico = "polyboy.png"

    gif = "dog.gif"

    img = "back.png"

    tab1 = QWidget()
    tab2 = QWidget()

    win.addTab(tab1,"en_poly")
    win.addTab(tab2,"de_poly")

    def clear():
        line.clear()

    def clear1():
        line1.clear()    

    def decrypt():

        
        if edit2.text == "" and edit3.text =="":
                dio = QMessageBox(win)
                dio.setText("please enter text filed")
                dio.show()
        


    
        sentence = edit2.text()
        line1.appendPlainText("Enter Phrase:\n")
        engine.say("Your Encoded phrase")
        engine.runAndWait()
        line1.appendPlainText(str(">> "+sentence+"\n"))
        engine.say(str(sentence))
        engine.runAndWait()       
        
        shiftword = edit3.text()
        line1.appendPlainText("Provide Shift Word:\n")
        engine.say("Your Shift Word")
        engine.runAndWait()
        line1.appendPlainText(str(">> "+shiftword+"\n"))
        engine.say(str(shiftword)) 
        engine.runAndWait()

        

        

        shiftletters = list(shiftword)
        letters = list(sentence)
        
        if(len(shiftletters) == 0 or len(sentence) == 0):
                
    
        
            print("Both a passphrase and an encoded phrase is required")

                    
        PolyDict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25, 'A':26, 'B':27,'C':28,'D':29,'E':30,'F':31,'G':32,'H':33,'I':34,'J':35,'K':36,'L':37,'M':38,'N':39,'O':40,'P':41,'Q':42,'R':43,'S':44,'T':45,'U':46,'V':47,'W':48,'X':49,'Y':50,'Z':51,'1':52,'2':53,'3':54,'4':55,'5':56,'6':57,'7':58,'8':59,'9':60,'0':61,'!':62,'@':63,'#':64,'$':65,'%':66,'^':67,'&':68,'*':69,'(':70,')':71,'-':72,'+':73,'=':74,':':75,';':76,'"':77,"'":78,',':79,'<':80,'>':81,'.':82,'?':83,' ':84}
        notInDictErrorMsg = "Invalid Chracters: One or more characters in your phrase or passcode is not accepted by this program"
        for letter in sentence:
            if(letter in PolyDict):
                pass
            else:
                exit(notInDictErrorMsg)
        for letter in shiftword:
            if(letter in PolyDict):
                pass
            else:
                exit(notInDictErrorMsg)

        def find_value(letter):
            letter = str(letter)
            key = PolyDict[letter]
            return int(key)
        def find_key(val):
            for key in PolyDict.keys():
                if PolyDict[key] == val:
                    return str(key)
        ordinated = []
        for letter in letters:
            ordinatedLetter = find_value(letter)
            ordinated.append(ordinatedLetter)
        usedChars = []
        allshifted = []
        for number in ordinated:
            if(len(shiftletters) > 0):
                shiftLetter = shiftletters[0]
                convertedLetter = find_value(shiftLetter)
                shiftByNum = (number - convertedLetter) % 85
                allshifted.append(shiftByNum)
                usedChars.append(shiftLetter)
                shiftletters.remove(shiftLetter)
                if(len(shiftletters) == 0):
                    for element in usedChars:
                        shiftletters.append(element)
                    del usedChars[:]
            elif(len(shiftletters) == 0):
                for element in usedChars:
                    shiftletters.append(element)
                del usedChars[:]
        encString = []

        for number in allshifted:
            char = find_key(number)
            encString.append(char)
        line1.appendPlainText("Your Decryption: \n")
        engine.say("Your Decryption")
        engine.runAndWait()    
        line1.appendPlainText(str(">>"+''.join(encString)+"\n"))      
        engine.say(str(''.join(encString)))
        engine.runAndWait()



    def encrypt():

        if edit.text == "" and edit1.text =="":
                dio = QMessageBox(win)
                dio.setText("please enter text filed")
                dio.show()


        sentence = edit.text()
        line.appendPlainText("Enter Phrase:\n")
        engine.say("Your Enter Phrase")
        engine.runAndWait()
        line.appendPlainText(">> "+sentence +"\n")
        engine.say(str(sentence))
        engine.runAndWait()
        shiftword = edit1.text()
        line.appendPlainText("Privided Shift Word :\n")
        engine.say("Provided Shift Word")
        engine.runAndWait()
        line.appendPlainText(">> "+shiftword +"\n")
        engine.say(str(shiftword))
        engine.runAndWait()

        shiftletters = list(shiftword)
        letters = list(sentence)
        PolyDict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25, 'A':26, 'B':27,'C':28,'D':29,'E':30,'F':31,'G':32,'H':33,'I':34,'J':35,'K':36,'L':37,'M':38,'N':39,'O':40,'P':41,'Q':42,'R':43,'S':44,'T':45,'U':46,'V':47,'W':48,'X':49,'Y':50,'Z':51,'1':52,'2':53,'3':54,'4':55,'5':56,'6':57,'7':58,'8':59,'9':60,'0':61,'!':62,'@':63,'#':64,'$':65,'%':66,'^':67,'&':68,'*':69,'(':70,')':71,'-':72,'+':73,'=':74,':':75,';':76,'"':77,"'":78,',':79,'<':80,'>':81,'.':82,'?':83,' ':84}
        if(len(shiftletters) == 0 or len(sentence) == 0):
            print("Both a passphrase and a phrase to be encoded is required")

        notInDictErrorMsg = "Invalid Chracters: One or more characters in your phrase or passcode is not accepted by this program"
        for letter in sentence:
            if(letter in PolyDict):
                pass
            else:
                exit(notInDictErrorMsg)
        for letter in shiftword:
            if(letter in PolyDict):
                pass
            else:
                exit(notInDictErrorMsg)

        def find_value(letter):
            letter = str(letter)
            key = PolyDict[letter]
            return key
        def find_key(val):
            for key in PolyDict.keys():
                if PolyDict[key] == val:
                    return str(key)
        ordinated = []
        for letter in letters:
            ordinatedLetter = find_value(letter)
            ordinated.append(ordinatedLetter)

        encString = []
        usedChars = []
        allshifted = []
        for number in ordinated:
            if(len(shiftletters) > 0):
                shiftLetter = shiftletters[0]
                convertedLetter = find_value(shiftLetter)
                shiftByNum = (number + convertedLetter) % 85

                allshifted.append(shiftByNum)
                usedChars.append(shiftLetter)
                del shiftletters[0]
                if(len(shiftletters) == 0):
                    for element in usedChars:
                        shiftletters.append(element)
                    del usedChars[:]
            elif(len(shiftletters) == 0):
                for element in usedChars:
                    shiftletters.append(element)
                del usedChars[:]
        for number in allshifted:
            char = find_key(number)
            encString.append(char)
            
        line.appendPlainText("Your Encryption: \n")
        engine.say("Your Encryption")
        engine.runAndWait()
        line.appendPlainText(str(">>"+''.join(encString)+"\n"))
        engine.say(str(''.join(encString)))
        engine.runAndWait()


    label = QLabel(tab1)    
    label.setPixmap(QPixmap(img))
    label.show()

    gif1 = QLabel(tab1)
    mov = QMovie(gif)
    gif1.setMovie(mov)
    mov.start()
    gif1.move(430,53)
    mov.setScaledSize(QSize(120,100))


    

    title= QLabel(tab1)
    title.setText("PolyAlpha")
    title.setFont(QFont("bradley hand ITC",50))
    title.setStyleSheet("font-weight:bold;border:2px solid white;border-radius:20px;color:white")
    title.move(330,10)



    b1= QPushButton(tab1)
    b1.setFont(QFont("Century Gothic",20))
    b1.setStyleSheet("QPushButton::hover""{"
                "background-color:#8bb4c3"
    "}")
    b1.setText("Encrypt")
    b1.setFixedHeight(50)
    b1.setFixedWidth(200)
    b1.move(50,400)
    b1.show()
    b1.clicked.connect(encrypt)

    b2= QPushButton(tab1)
    b2.setFont(QFont("Century Gothic",20))
    b2.setStyleSheet("QPushButton::hover""{"
                "background-color:#8bb4c3"
    "}")
    b2.setText("Clear")
    b2.setFixedHeight(50)
    b2.setFixedWidth(150)
    b2.move(270,400)
    b2.show()
    b2.clicked.connect(clear)

    

    lab = QLabel(tab1)
    lab.setStyleSheet("color:white;font-weight:bold")
    lab.setText("Enter Phrase")
    lab.setFont(QFont("arial",20))
    lab.move(50,130)
    lab.show()

    edit = QLineEdit(tab1)
    edit.setStyleSheet("border-radius:20px;")
    edit.setPlaceholderText("Gimme your Phrase")
    edit.setFont(QFont("arial",20))
    edit.setFixedHeight(50)
    edit.setFixedWidth(300)
    edit.move(230,120)


    lab1 = QLabel(tab1)
    lab1.setStyleSheet("color:white;font-weight:bold")
    lab1.setText("Shift Word")
    lab1.setFont(QFont("arial",20))
    lab1.move(50,230)
    lab1.show()

    edit1 = QLineEdit(tab1)
    edit1.setStyleSheet("border-radius:20px;")

    edit1.setPlaceholderText("Provide shift word")
    edit1.setFont(QFont("arial",20))
    edit1.setFixedHeight(50)
    edit1.setFixedWidth(300)
    edit1.move(230,220)

    line = QPlainTextEdit(tab1)
    line.setReadOnly(True)
    line.setStyleSheet("border:2px solid black;border-radius:20px")

    line.setFont(QFont("Arial",15))
    line.setFixedHeight(300)
    line.setFixedWidth(420)
    line.show()
    line.move(550,120)

    #for decryption

    label = QLabel(tab2)    
    label.setPixmap(QPixmap(img))
    label.show()

    gif2 = QLabel(tab2)
    mov1 = QMovie(gif)
    gif2.setMovie(mov)
    mov1.start()
    gif2.move(430,319)
    mov1.setScaledSize(QSize(120,100))

    title= QLabel(tab2)
    title.setText("PolyAlpha")
    title.setFont(QFont("bradley hand ITC",50))
    title.setStyleSheet("font-weight:bold;border:2px solid white;border-radius:20px;color:white")
    title.move(330,10)



    b1= QPushButton(tab2)
    b1.setFont(QFont("Century Gothic",20))
    b1.setStyleSheet("QPushButton::hover""{"
                "background-color:#8bb4c3"
    "}")
    b1.setText("Decrypt")
    b1.setFixedHeight(50)
    b1.setFixedWidth(200)
    b1.move(50,400)
    b1.show()
    b1.clicked.connect(decrypt)

    lab = QLabel(tab2)
    lab.setStyleSheet("color:white;font-weight:bold")
    lab.setText("Enter Phrase")
    lab.setFont(QFont("arial",20))
    lab.move(50,130)
    lab.show()

    b3= QPushButton(tab2)
    b3.setFont(QFont("Century Gothic",20))
    b3.setStyleSheet("QPushButton::hover""{"
                "background-color:#8bb4c3"
    "}")
    b3.setText("Clear")
    b3.setFixedHeight(50)
    b3.setFixedWidth(150)
    b3.move(270,400)
    b3.show()
    b3.clicked.connect(clear1)

    edit2 = QLineEdit(tab2)
    edit2.setStyleSheet("border-radius:20px;")
    edit2.setPlaceholderText("Gimme your Phrase")
    edit2.setFont(QFont("arial",20))
    edit2.setFixedHeight(50)
    edit2.setFixedWidth(300)
    edit2.move(230,120)


    lab1 = QLabel(tab2)
    lab1.setStyleSheet("color:white;font-weight:bold")
    lab1.setText("Shift Word")
    lab1.setFont(QFont("arial",20))
    lab1.move(50,230)
    lab1.show()

    edit3 = QLineEdit(tab2)
    edit3.setStyleSheet("border-radius:20px;")

    edit3.setPlaceholderText("Provide shift word")
    edit3.setFont(QFont("arial",20))
    edit3.setFixedHeight(50)
    edit3.setFixedWidth(300)
    edit3.move(230,220)

    line1 = QPlainTextEdit(tab2)
    line1.setReadOnly(True)
    line1.setStyleSheet("border:2px solid black;border-radius:20px")

    line1.setFont(QFont("Arial",15))
    line1.setFixedHeight(300)
    line1.setFixedWidth(420)
    line1.show()
    line1.move(550,120)


    




    

    

    

    win.setWindowIcon(QIcon(ico))
    win.setFixedHeight(500)
    win.setFixedWidth(1000)
    win.setWindowTitle("PolyAlphabaticApp")
    win.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    build()


