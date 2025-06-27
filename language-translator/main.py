def translate(): #Translation function
    translator = Translator(from_lang=language_opts[InputLanguageChoice.get()],to_lang=language_opts[TranslateLanguageChoice.get()])
    translation = translator.translate(TextVar.get())
    OutputVar.set(str(translation))                                  


def main(): #Mainloop for tkinter GUI
    #Setting up the screen
    Screen = Tk()
    Screen.title("Language Translator")
    Screen.geometry("600x100")
    
    #Setting up language vars
    global language_opts #Needed for the translate function
    language_opts = {
        "English":"en",
        "German":"de",
        "French":"fr",
        "Spanish":"es"
    }
    
    global InputLanguageChoice #Needed for the translate function
    global TranslateLanguageChoice #Needed for the translate function
    
    InputLanguageChoice = StringVar()
    TranslateLanguageChoice = StringVar()
    InputLanguageChoice.set("English")
    TranslateLanguageChoice.set("French")
    
    #Choice for input language
    InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*language_opts)
    Label(Screen,text="Choose a Language to Translate FROM").grid(row=0,column=1)
    InputLanguageChoiceMenu.grid(row=1,column=1)
 
    #Choice for output language
    NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*language_opts)
    Label(Screen,text="Choose a Language to Translate TO").grid(row=0,column=2)
    NewLanguageChoiceMenu.grid(row=1,column=2)

    #Setting up labels
    Label(Screen,text="Enter Text").grid(row=2,column =0)
    global TextVar #Needed for the translate function
    TextVar = StringVar()
    TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)
    
    Label(Screen,text="Output Text").grid(row=2,column =2)
    global OutputVar #Needed for the translate function
    OutputVar = StringVar()
    TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 3)

    #Button for calling function
    B = Button(Screen,text="Translate",command=translate) #The reason global vars was needed
    B.grid(row=3,column=0,columnspan = 3)
    
    
    Screen.mainloop()


if __name__ == "__main__":
    from tkinter import *
    from translate import Translator
    main()