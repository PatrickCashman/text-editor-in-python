import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to open a file and load its content into the text editor
def open_file(window, text_edit): 
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    # If no file is selected, return without doing anything
    if not filepath:
        return
    # Clear the existing text in the text editor
    text_edit.delete(1.0, tk.END)
    
    # Open the selected file and read its content
    with open(filepath, "r") as f:
        content = f.read()
        # Insert the content into the text editor
        text_edit.insert(tk.END, content)

    # Set the window title to indicate the opened file
    window.title(f"Open File: {filepath}")

# Function to save the content of the text editor to a file
def save_file(window, text_edit):
    # Open a file dialog to select a location to save the file
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    # If no location is selected, return without doing anything
    if not filepath:
        return
    
    # Open the selected file for writing
    with open(filepath, "w") as f:
        # Get the content of the text editor
        content = text_edit.get(1.0, tk.END)
        # Write the content to the file
        f.write(content)

    # Set the window title to indicate the saved file
    window.title(f"Save File: {filepath}")

# Main function to create the GUI and handle user interactions
def main():
    # Create the main window
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    # Create a text editor widget
    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1, sticky="nsew")

    # Create a frame to hold the buttons
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    # Create 'Save' and 'Open' buttons, with commands to call the save_file and open_file functions
    save_button = tk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit))

    # Position the buttons within the frame
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")

    # Position the frame within the window
    frame.grid(row=0, column=0, sticky="ns")

    # Bind keyboard shortcuts (Ctrl+S for save, Ctrl+O for open)
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    # Start the Tkinter event loop
    window.mainloop()

# Call the main function to run the application
main()
