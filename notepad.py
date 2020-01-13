# module for getting file name
import os

# module for making GUI
from tkinter import *

# module to change font
from tkinter.font import *

# module to show messagebox
from tkinter.messagebox import *

# module to open and save file
from tkinter.filedialog import *

# class for making frame
class NotepadFrame(Frame):
    def __init__(self, master = None):
        # the beginning of Notepad, so there is no file path stored
        self.currentfilepath = None
        
        # initialize Notepad frame
        Frame.__init__(self, master)
        self.notepadframe = self.master
        
        # call function to initialize Notepad frame settings
        self.setNotepadFrameSettings()
        # call function to initialize Notepad controls
        self.makeNotepadControls()

    def setNotepadFrameSettings(self):
        # set Notepad frame title
        self.notepadframe.title("Untitled - Notepad")
        # set Notepad frame size
        self.notepadframe.geometry("1200x675")
    
    def makeNotepadControls(self):
        # make menubar
        self.menubar = Menu(self.notepadframe)
        
        # add File menu
        self.filemenu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        # add New menu item in File menu
        self.filemenu.add_command(label = "New", command = self.fileNew)
        # add New Window menu item in File menu
        self.filemenu.add_command(label = "New Window", command = self.fileNewWindow)
        # add Open menu item in File menu
        self.filemenu.add_command(label = "Open", command = self.fileOpen)
        # add Save menu item in File menu
        self.filemenu.add_command(label = "Save", command = self.fileSave)
        # add Save As menu item in File menu
        self.filemenu.add_command(label = "Save As", command = self.fileSaveAs)
        # add Separator
        self.filemenu.add_separator()
        # add Exit menu item in File menu
        self.filemenu.add_command(label = "Exit", command = self.quit)

        # add Edit menu
        self.editmenu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Edit", menu = self.editmenu)

        # add Undo menu item in Edit menu
        self.editmenu.add_command(label = "Undo", accelerator = "Ctrl+Z", command = self.editUndo)
        # add Redo menu item in Edit menu
        self.editmenu.add_command(label = "Redo", accelerator = "Ctrl+Y", command = self.editRedo)
        # add Separator
        self.editmenu.add_separator()
        # add Cut menu item in Edit menu
        self.editmenu.add_command(label = "Cut", accelerator = "Ctrl+X", command = self.editCut)
        # add Copy menu item in Edit menu
        self.editmenu.add_command(label = "Copy", accelerator = "Ctrl+C", command = self.editCopy)
        # add Paste menu item in Edit menu
        self.editmenu.add_command(label = "Paste", accelerator = "Ctrl+V", command = self.editPaste)
        # add Delete menu item in Edit menu
        self.editmenu.add_command(label = "Delete", accelerator = "Del", command = self.editDelete)
        # add Separator
        self.editmenu.add_separator()
        # add Select All menu item in Edit menu
        self.editmenu.add_command(label = "Select All", accelerator = "Ctrl+A", command = self.editSelectAll)

        # add About menu
        self.aboutmenu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "About", menu = self.aboutmenu)

        # add About Notepad menu item in About menu
        self.aboutmenu.add_command(label = "About Author", command = self.aboutAboutAuthor)

        # displaying menubar in frame
        self.notepadframe.config(menu = self.menubar)
        
        # add main panel for frame
        self.panel1 = PanedWindow(self.notepadframe)
        self.panel1.pack(fill = BOTH, expand = 1)

        # add second panel inside main panel with vertical orientation for combining font configuration and text
        self.panel2 = PanedWindow(self.panel1, orient = VERTICAL)
        self.panel1.add(self.panel2)

        # add third panel inside second panel with horizontal orientation for placing font configuration option menus
        self.panel3 = PanedWindow(self.panel2, orient = HORIZONTAL)
        self.panel2.add(self.panel3)

        # make Font option menu
        self.fontvariable = StringVar(self.panel3)
        self.fontvariable.set("Please select the Font of your choice")
        self.fontoptionmenu = OptionMenu(self.panel3, self.fontvariable, 'System', '8514oem', 'Fixedsys', 'Terminal', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Text', 'Sitka Subheading', 'Sitka Heading', 'Sitka Display', 'Sitka Banner', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight', 'HoloLens MDL2 Assets', 'Century', 'Wingdings 2', 'Wingdings 3', 'Tempus Sans ITC', 'Pristina', 'Papyrus', 'Mistral', 'Lucida Handwriting', 'Kristen ITC', 'Juice ITC', 'French Script MT', 'Freestyle Script', 'Bradley Hand ITC', 'MS Outlook', 'Arial Narrow', 'Book Antiqua', 'Garamond', 'Monotype Corsiva', 'Century Gothic', 'Algerian', 'Baskerville Old Face', 'Bauhaus 93', 'Bell MT', 'Berlin Sans FB', 'Bernard MT Condensed', 'Bodoni MT Poster Compressed', 'Britannic Bold', 'Broadway', 'Brush Script MT', 'Californian FB', 'Centaur', 'Chiller', 'Colonna MT', 'Cooper Black', 'Footlight MT Light', 'Harlow Solid Italic', 'Harrington', 'High Tower Text', 'Jokerman', 'Kunstler Script', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Magneto', 'Matura MT Script Capitals', 'Modern No. 20', 'Niagara Engraved', 'Niagara Solid', 'Old English Text MT', 'Onyx', 'Parchment', 'Playbill', 'Poor Richard', 'Ravie', 'Informal Roman', 'Showcard Gothic', 'Snap ITC', 'Stencil', 'Viner Hand ITC', 'Vivaldi', 'Vladimir Script', 'Wide Latin', 'Tw Cen MT', 'Tw Cen MT Condensed', 'Script MT Bold', 'Rockwell Extra Bold', 'Rockwell Condensed', 'Rockwell', 'Rage Italic', 'Perpetua Titling MT', 'Perpetua', 'Palace Script MT', 'OCR A Extended', 'Maiandra GD', 'Lucida Sans Typewriter', 'Lucida Sans', 'Imprint MT Shadow', 'Haettenschweiler', 'Goudy Stout', 'Goudy Old Style', 'Gloucester MT Extra Condensed', 'Gill Sans Ultra Bold Condensed', 'Gill Sans Ultra Bold', 'Gill Sans MT Condensed', 'Gill Sans MT', 'Gill Sans MT Ext Condensed Bold', 'Gigi', 'Franklin Gothic Medium Cond', 'Franklin Gothic Heavy', 'Franklin Gothic Demi Cond', 'Franklin Gothic Demi', 'Franklin Gothic Book', 'Forte', 'Felix Titling', 'Eras Medium ITC', 'Eras Light ITC', 'Eras Demi ITC', 'Eras Bold ITC', 'Engravers MT', 'Elephant', 'Edwardian Script ITC', 'Curlz MT', 'Copperplate Gothic Light', 'Copperplate Gothic Bold', 'Century Schoolbook', 'Castellar', 'Calisto MT', 'Bookman Old Style', 'Bodoni MT Condensed', 'Bodoni MT Black', 'Bodoni MT', 'Blackadder ITC', 'Arial Rounded MT Bold', 'Agency FB', 'Bookshelf Symbol 7', 'MS Reference Sans Serif', 'MS Reference Specialty', 'Berlin Sans FB Demi', 'Tw Cen MT Condensed Extra Bold')
        self.panel3.add(self.fontoptionmenu)

        # set current font to None because there is no font selected
        self.currentfont = None

        # make Font Style option menu
        self.fontstylevariable = StringVar(self.panel3)
        self.fontstylevariable.set("Please select the Font Style of your choice")
        self.fontstyleoptionmenu = OptionMenu(self.panel3, self.fontstylevariable, "Regular", "Bold", "Italic", "Underline", "Overstrike")
        self.panel3.add(self.fontstyleoptionmenu)

        # set current font style to None because there is no font selected
        self.currentfontstyle = None

        # make Font Style option menu
        self.fontsizevariable = StringVar(self.panel3)
        self.fontsizevariable.set("Please select the Font Size of your choice")
        self.fontsizeoptionmenu = OptionMenu(self.panel3, self.fontsizevariable, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 26, 28, 36, 48, 72)
        self.panel3.add(self.fontsizeoptionmenu)

        # set current font size to None because there is no font selected
        self.currentfontsize = None

        # make Apply button to apply font changes if font has been configurated
        self.applybutton = Button(self.panel3, text = "Apply", command = self.applyChanges)
        self.panel3.add(self.applybutton)
        
        # make invisible label so Apply button will not expand
        self.invisiblelabel = Label(self.panel3, text = "")
        self.panel3.add(self.invisiblelabel)
        
        # make text
        self.text = Text(self.panel2, undo = True)
        self.panel2.add(self.text)

        # make vertical scroll bar for text
        self.textscrollbar = Scrollbar(self.text, command = self.text.yview)
        self.textscrollbar.pack(side = RIGHT, fill = Y)

        # scroll bar will adjust according to text content
        self.text.config(yscrollcommand = self.textscrollbar.set)

    def fileNew(self):
        # make new file
        self.notepadframe.title("Untitled - Notepad")
        self.file = None
        self.text.delete(1.0, END)
    
    def fileNewWindow(self):
        # make new Notepad frame
        self.notepadwindow = Toplevel(self.notepadframe)
        self.notepadframe = NotepadFrame(self.notepadwindow)
        
    def fileOpen(self):
        # file types
        self.filetypes = [("Text Document", "*.txt"), ("All Files", "*.*")]

        # ask whether user wants to open file
        self.currentfilepath = askopenfilename(filetypes = self.filetypes, defaultextension = ".txt")
        
        if self.currentfilepath == "":
            # no file name, so user cannot open file
            self.currentfilepath = None

        # open file
        else:
            # delete previous contents in text
            self.text.delete(1.0, END)

            # open saved file to read new contents
            file = open(self.currentfilepath, "r")
            
            # insert new contents to text
            self.text.insert(1.0, file.read())

            # close read file
            file.close()

            # read current font settings from files
            file = open("C:/Users/user/.vscode/Final Project/notepadfont.txt", "r")
            self.currentfont = file.read()
            file.close()
            file = open("C:/Users/user/.vscode/Final Project/notepadfontstyle.txt", "r")
            self.currentfontstyle = file.read()
            file.close()
            file = open("C:/Users/user/.vscode/Final Project/notepadfontsize.txt", "r")
            try:
                self.currentfontsize = int(file.read())
            except:
                pass
            file.close()

            # load current font settings if available
            if self.currentfont in families() and self.currentfontstyle in ["Regular", "Bold", "Italic", "Underline", "Overstrike"] and self.currentfontsize in [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 26, 28, 36, 48, 72]:
                if self.currentfontstyle == "Regular":
                    self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "normal")
                elif self.currentfontstyle == "Bold":
                    self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "bold")
                elif self.currentfontstyle == "Italic":
                    self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "normal", slant = "italic")
                elif self.currentfontstyle == "Underline":
                    self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "normal", underline = 1)
                elif self.currentfontstyle == "Overstrike":
                    self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "normal", overstrike = 1)
                self.text.config(font = self.fontsettings)
                
                # display font settings
                self.fontvariable.set(self.currentfont)
                self.fontstylevariable.set(self.currentfontstyle)
                self.fontsizevariable.set(self.currentfontsize)

            # change Notepad window title
            self.notepadframe.title(os.path.basename(self.currentfilepath) + " - Notepad")
    
    def fileSave(self):
        # file types
        self.filetypes = [("Text Document", "*.txt"), ("All Files", "*.*")]
        
        # ask whether user wants to save file
        if self.currentfilepath == None:
            # the beginning of Notepad, so Save acts the same as Save As
            self.currentfilepath = asksaveasfilename(initialfile = 'Untitled.txt', filetypes = self.filetypes, defaultextension = ".txt")

            if self.currentfilepath == "":
                # no file name, so user cannot save file
                self.currentfilepath = None

            else:
                # save file
                file = open(self.currentfilepath, "w")
                file.write(self.text.get(1.0, END))
                file.close()

                # write font settings into new files if available
                if self.currentfont in families() and self.currentfontstyle in ["Regular", "Bold", "Italic", "Underline", "Overstrike"] and self.currentfontsize in [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 26, 28, 36, 48, 72]:
                    file = open("C:/Users/user/.vscode/Final Project/notepadfont.txt", "w")
                    file.write(self.currentfont)
                    file.close()
                    file = open("C:/Users/user/.vscode/Final Project/notepadfontstyle.txt", "w")
                    file.write(self.currentfontstyle)
                    file.close()
                    file = open("C:/Users/user/.vscode/Final Project/notepadfontsize.txt", "w")
                    file.write(str(self.currentfontsize))
                    file.close()
                
                # change Notepad window title
                self.notepadframe.title(os.path.basename(self.currentfilepath) + " - Notepad")
        
        else:
            # save file changes
            file = open(self.currentfilepath, "w")
            file.write(self.text.get(1.0, END))
            file.close()

            # write font settings into new files if available
            if self.currentfont in families() and self.currentfontstyle in ["Regular", "Bold", "Italic", "Underline", "Overstrike"] and self.currentfontsize in [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 26, 28, 36, 48, 72]:
                file = open("C:/Users/user/.vscode/Final Project/notepadfont.txt", "w")
                file.write(self.currentfont)
                file.close()
                file = open("C:/Users/user/.vscode/Final Project/notepadfontstyle.txt", "w")
                file.write(self.currentfontstyle)
                file.close()
                file = open("C:/Users/user/.vscode/Final Project/notepadfontsize.txt", "w")
                file.write(str(self.currentfontsize))
                file.close()

    def fileSaveAs(self):
        # file types
        self.filetypes = [("Text Document", "*.txt"), ("All Files", "*.*")]
        
        # ask whether user wants to save file
        if self.currentfilepath == None:
            # the beginning of Notepad, so file name is Untitled
            self.currentfilepath = asksaveasfilename(initialfile = 'Untitled.txt', filetypes = self.filetypes, defaultextension = ".txt")

        else:
            # the saved file has already been named, so user must change the file name
            self.currentfilepath = asksaveasfilename(initialfile = os.path.basename(self.currentfilepath), filetypes = self.filetypes, defaultextension = ".txt")

        if self.currentfilepath == "":
            # no file name, so user cannot save file
            self.currentfilepath = None

        else:
            # save file
            file = open(self.currentfilepath, "w")
            file.write(self.text.get(1.0, END))
            file.close()

            # write font settings into new files if available
            if self.currentfont in families() and self.currentfontstyle in ["Regular", "Bold", "Italic", "Underline", "Overstrike"] and self.currentfontsize in [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 26, 28, 36, 48, 72]:
                file = open("C:/Users/user/.vscode/Final Project/notepadfont.txt", "w")
                file.write(self.currentfont)
                file.close()
                file = open("C:/Users/user/.vscode/Final Project/notepadfontstyle.txt", "w")
                file.write(self.currentfontstyle)
                file.close()
                file = open("C:/Users/user/.vscode/Final Project/notepadfontsize.txt", "w")
                file.write(str(self.currentfontsize))
                file.close()
            
            # change Notepad window title
            self.notepadframe.title(os.path.basename(self.currentfilepath) + " - Notepad")

    def editUndo(self):
        # generate Undo command
        self.text.edit_undo()
    
    def editRedo(self):
        # generate Redo command
        self.text.edit_redo()
    
    def editCut(self):
        # generate Cut command
        self.text.event_generate("<<Cut>>")

    def editCopy(self):
        # generate Copy command
        self.text.event_generate("<<Copy>>")
    
    def editPaste(self):
        # generate Paste command
        self.text.event_generate("<<Paste>>")
    
    def editDelete(self):
        # generate Delete command
        self.text.event_generate("<<Clear>>")

    def editSelectAll(self):
        # generate Select All command
        self.text.event_generate("<<SelectAll>>")
    
    def aboutAboutAuthor(self):
        # author info
        messagebox.showinfo("About Author", "Jeremy Ponto\n2301891525")
    
    def applyChanges(self):
        # get value from Font, Font Style, and Font Size option menu
        self.currentfont = self.fontvariable.get()
        self.currentfontstyle = self.fontstylevariable.get()
        self.currentfontsize = self.fontsizevariable.get()
        
        # set font changes
        if self.currentfontstyle == "Regular":
            self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "normal")
        elif self.currentfontstyle == "Bold":
            self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "bold")
        elif self.currentfontstyle == "Italic":
            self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "normal", slant = "italic")
        elif self.currentfontstyle == "Underline":
            self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "normal", underline = 1)
        elif self.currentfontstyle == "Overstrike":
            self.fontsettings = Font(family = self.currentfont, size = self.currentfontsize, weight = "normal", overstrike = 1)
        self.text.config(font = self.fontsettings)
        
# make new object for running notepad
notepad = NotepadFrame()

# run notepad
notepad.mainloop()