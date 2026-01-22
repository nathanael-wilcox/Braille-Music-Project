import customtkinter as ctk  #pip install customtkinter
import tkinter as tk
import tkinter.filedialog as filedialog
import xml.etree.ElementTree as ET
import os
# from PIL import Image, ImageTk

def on_button_click():
    filename = open_xml_file_dialog()
    print("Filename = ", filename)
    window.frame.update_textbox(f"Selected file: {filename}\nProcessing complete.")


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
        #label.configure(text=f"Selected file: {filename}")
        print ("Processing complete. File named", filename)
        return filename
        
    else:
        #label.configure(text="No file selected.")
        print("No file selected.")
        return "No file selected."

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

def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        print("Application Quit")
        window.quit()
        #window.destroy()

class MyFrame1(ctk.CTkFrame):
    def __init__(self, master, label="", **kwargs):
        super().__init__(master, **kwargs)
    
        # Widgets added to the frame
        self.label = ctk.CTkLabel(self)
        self.label.configure(text=label)
        self.label.update()
        self.label.grid(row=0, column=0, padx=20)

        self.textbox = ctk.CTkTextbox(self, width=300, height=100)
        self.textbox.insert("0.0", "No file selected.")
        self.textbox.configure(state=tk.DISABLED)
        self.textbox.grid(row=2, column=0, pady=10, padx=20)
        
        self.button = ctk.CTkButton(self, text="Open MusicXML File", command=on_button_click)
        self.button.grid(row=1, column=0, pady=10, padx=20)
    
    def update_textbox(self, text):
        self.textbox.configure(state=tk.NORMAL)
        self.textbox.delete("0.0", tk.END)
        self.textbox.insert("0.0", text)
        self.textbox.configure(state=tk.DISABLED)

        # image_path = 'musicfileicon.png' 
        # self.image = Image.open(image_path)
        # self.image = self.image.resize((64, 64), Image.LANCZOS)
        # self.photo_image = ImageTk.PhotoImage(self.image)
        # I tried to add an image, but that is put on hold lol
        
class MyFrame2(ctk.CTkFrame):
    def __init__(self, master, label="", **kwargs):
        super().__init__(master, **kwargs)
    
        # Widgets added to the frame
        self.label = ctk.CTkLabel(self)
        self.label.configure(text=label)
        self.label.update()
        self.label.grid(row=0, column=0, padx=20)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        label = "Select a MusicXML file to process."

        self.frame = MyFrame1(self, "Button Frame")
        #self.frame2 = MyFrame(self,"Yet another label")
        self.frame.grid(row=0, column=0, pady=20, padx=20)
        #self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        #self.frame2.pack(pady=20, padx=60, fill="both", expand=True)
        self.frame2 = MyFrame2(self, "No Button Frame")
        self.frame2.grid(row=0, column=1, pady=20, padx=20)
        #self.frame2.pack(pady=20, padx=60, fill="both", expand=True)
        #self.button = ctk.CTkButton(self, text="Open MusicXML File", command=on_button_click)


window = App()
window.title("XML File Processor")
window.geometry("600x200")

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()