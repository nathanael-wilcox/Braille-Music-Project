import customtkinter as ctk
import tkinter as tk
import tkinter.filedialog as filedialog
import xml.etree.ElementTree as ET
import os

window = ctk.CTk()
window.title("XML File Processor")
window.geometry("1000x500")

label = ctk.CTkLabel(window, text=" ")

def on_button_click():
    open_xml_file_dialog()

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
        label.configure(text=f"Selected file: {filename}")
        print ("Processing complete. File named", filename)
    else:
        label.configure(text="No file selected.")

def process_xml_file(filepath):
    # This is where you would put your XML processing logic
    try:
        # Parse the XML file
        tree = ET.parse(filepath)
        root = tree.getroot()

        print(f"Root tag of the XML file: {root.tag}")

        # Example: Add a new element to the XML structure
        new_element = ET.Element("new_data")
        new_element.text = "This data was added via the GUI"
        root.append(new_element)

        # Save the modified XML to a new file (or overwrite the old one)
        new_filepath = filepath.replace(".musicxml", "_modified.xml")
        tree.write(new_filepath)
        print(f"Modified MusicXML saved to {new_filepath}")

    except ET.ParseError as e:
        print(f"Error parsing MusicXML file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# button = tk.Button(window, text="Open MusicXML File", command=on_button_click)
# button.pack(pady=20)

# window.mainloop()

button = ctk.CTkButton(window, text="Open MusicXML File", command=on_button_click)
button.pack(pady=100)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()