import customtkinter as ctk  #pip install customtkinter
import tkinter as tk
import tkinter.filedialog as filedialog
import xml.etree.ElementTree as ET
import os
from PIL import Image, ImageTk

def on_button_click():
    filename = open_xml_file_dialog()
    if filename != "No file selected.":
        print("Filename = ", filename)
    window.frame2.update_textbox(f"Selected file: {filename}")


# Function to open file dialog and select XML file
def open_xml_file_dialog():
    # Create a root window but hide it, as we only need the dialog box
    root = tk.Tk()
    root.withdraw()

    # Open the file selection dialog
    file_path = filedialog.askopenfilename(
        title="Select MusicXML File",
        filetypes=(("MusicXML files", "*.musicxml"), ("All files", "*.*"))
    )

    if file_path:
        filename = os.path.basename(file_path)
        print(f"Selected file: {file_path}")
        # Call the function to process the XML file
        process_xml_file(file_path)
        print ("Processing complete. File named", filename)
        return filename
        
    else:
        print("No file selected.")
        return "No file selected."

#  Function to process the selected XML file
def process_xml_file(filepath):
    # This is where you would put your XML processing logic
    try:
        # Parse the XML file
        tree = ET.parse(filepath)
        root = tree.getroot()

        new_element = ET.Element("new_data")
        new_element.text = "This data was added via the GUI"
        root.append(new_element)

        # Save the modified XML to a new file (or overwrite the old one)
        new_filepath = filepath.replace(".musicxml", "_modified.xml")
        tree.write(new_filepath)

        # Catch Exceptions
    except ET.ParseError as e:
        print(f"Error parsing MusicXML file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Handle window closing event
def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        print("Application Quit")
        window.quit()

class MyFrame1(ctk.CTkFrame):
    def __init__(self, master, label="", **kwargs):
        super().__init__(master, **kwargs)
    
        # Frame Label
        #self.label = ctk.CTkLabel(self)
        #self.label.configure(text=label)
        #self.label.update()
        #self.label.grid(row=1, column=0, padx=20)
        self.entry = ctk.CTkEntry(self, placeholder_text="CTkEntry", textvariable=tk.StringVar(value="Button Frame"), width=300, state=tk.DISABLED)
        self.entry.pack(side='top',pady=10, padx=20)
        
        # Frame Button
        self.button = ctk.CTkButton(self, text="Open MusicXML File", command=on_button_click, width=150, height=50)
        self.button.pack(side="right", padx=20, pady=10)
        
    

        try:
            image_path = 'musicfileicon.png' 
            pil_image = Image.open(image_path)
            #pil_image = pil_image.resize((128, 128), Image.LANCZOS)
            tk_image = ctk.CTkImage(pil_image, size=(128, 128))
        except Exception as e:
            print(f"Exception {e} found loading image.")
            tk_image = None

        if tk_image:
            image_label = ctk.CTkLabel(self, image=tk_image, bg_color="transparent", text='')
            image_label.image = tk_image  # Keep a reference to avoid garbage collection
            image_label.pack(side="left", padx=20, pady=10)

        # I tried to add an image, but that is put on hold lol
        
class MyFrame2(ctk.CTkFrame):
    def __init__(self, master, label="", **kwargs):
        super().__init__(master, **kwargs)
    
        # Frame Label
        # self.label = ctk.CTkLabel(self)
        # self.label.configure(text=label)
        # self.label.update()
        # self.label.grid(row=1, column=0, padx=20)
        self.entry = ctk.CTkEntry(self, placeholder_text="CTkEntry", textvariable=tk.StringVar(value="File Name"), width=300, state=tk.DISABLED)
        self.entry.grid(row=0, column=0, pady=10, padx=20)

        # Frame Textbox
        self.textbox = ctk.CTkTextbox(self, width=300, height=100)
        self.textbox.insert("0.0", "No file selected.")
        self.textbox.configure(state=tk.DISABLED)
        self.textbox.grid(row=2, column=0, pady=10, padx=20)


    # Method to update textbox content with filename label
    def update_textbox(self, text):
        self.textbox.configure(state=tk.NORMAL)
        self.textbox.delete("0.0", tk.END)
        self.textbox.insert("0.0", text)
        self.textbox.configure(state=tk.DISABLED)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Frame 1 of the App
        self.frame = MyFrame1(self)
        self.frame.grid(row=0, column=0, pady=20, padx=20)
        self.frame.configure(border_width=2, border_color="red")

        # Frame 2 of the App
        self.frame2 = MyFrame2(self)
        self.frame2.grid(row=1, column=0, pady=20, padx=20)
        self.frame2.configure(border_width=2, border_color="red")


# Create the main application window
window = App()
window.title("XML File Processor")
window.geometry("400x450")

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()