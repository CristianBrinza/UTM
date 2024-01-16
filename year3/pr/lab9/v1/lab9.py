# Importing necessary libraries and modules for GUI, email, and FTP functionalities
import tkinter as tk  # Tkinter for creating graphical user interface (GUI) applications.
from tkinter import filedialog  # File dialog module from Tkinter for opening file selection dialogs.
from tkinter import messagebox  # Message box module from Tkinter for displaying alerts and prompts.
import smtplib  # SMTPLib for sending emails using the Simple Mail Transfer Protocol (SMTP).
from email.mime.multipart import MIMEMultipart  # For creating multipart (having multiple parts like text, attachments) email messages.
from email.mime.text import MIMEText  # For creating text parts in emails.
from ftplib import FTP  # FTP library for handling File Transfer Protocol operations.


# ▒█▀▄▒█▀▄ lab. PR | FAF | FCIM | UTM | Fall 2023
# ░█▀▒░█▀▄ FAF-212 Cristian Brinza lab9


print('')
print('▒█▀▄▒█▀▄  lab. PR | FAF | FCIM | UTM | Fall 2023')
print('░█▀▒░█▀▄  FAF-212 Cristian Brinza lab9  ')
print('')


# Function to send an email
def send_email(destination_email, subject, email_text, file_link):
    """
    This function is used to send an email.

    Parameters:
    destination_email (str): The email address of the recipient.
    subject (str): The subject line of the email.
    email_text (str): The body text of the email.
    file_link (str): A link to include in the email, typically to a file.

    Note:
    The sender's email and password should not be hardcoded. Ideally, they should be
    securely stored and retrieved from environment variables or a secure store.
    """
    sender_email = "cristian.brinza.service.acc@gmail.com"  # The sender's email address (should be replaced with a real address).
    sender_password = "dzet yvpf pesr dcsz"  # The sender's email password (should be replaced with a real password).

    message = MIMEMultipart()  # Creating a MIMEMultipart object for the email message.
    message['From'] = sender_email  # Setting the sender's email in the message header.
    message['To'] = destination_email  # Setting the recipient's email in the message header.
    message['Subject'] = subject  # Setting the subject of the email in the message header.
    message.attach(MIMEText(email_text + "\n\nFile link: " + file_link, 'plain'))  # Attaching the email text and file link to the message.

    session = smtplib.SMTP('smtp.gmail.com', 587)  # Creating an SMTP session using Gmail's SMTP server.
    session.starttls()  # Starting TLS (Transport Layer Security) for secure email sending.
    session.login(sender_email, sender_password)  # Logging into the SMTP server using the sender's credentials.
    session.sendmail(sender_email, destination_email, message.as_string())  # Sending the email.
    session.quit()  # Terminating the SMTP session.



# Function to upload a file to an FTP server
def upload_file_ftp(file_path):
    """
    Uploads a file to an FTP server and returns the web accessible path.

    Parameters:
    file_path (str): The local path of the file to be uploaded.

    Returns:
    str: The web accessible path of the uploaded file.
    """
    ftp_server = "yourftpserver.com"  # FTP server address.
    username = "yourusername"  # FTP username.
    password = "yourpassword"  # FTP password.
    remote_path = "/home/somedirectory/faf-212/cristian_brinza/"  # Remote directory path on the FTP server.

    # Deriving the remote file path.
    remote_file_path = remote_path + file_path.split('/')[-1]

    # Establishing an FTP connection and uploading the file.
    ftp = FTP(ftp_server)
    ftp.login(username, password)
    with open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {remote_file_path}', file)  # Uploading the file in binary mode.
    ftp.quit()

    # Constructing and returning the web accessible path of the file.
    web_accessible_path = "/faf-212/cristian_brinza/" + file_path.split('/')[-1]
    return "http://138.68.98.108" + web_accessible_path


# Defining functions for the GUI elements
def browse_file():
    """
    Function invoked by the 'Browse' button in the GUI.
    It opens a file dialog for the user to select a file and updates the file path entry with the selected file.
    """
    filename = filedialog.askopenfilename()  # Opens a file dialog and stores the selected file's path.
    file_path_entry.delete(0, tk.END)  # Clears the current file path entry.
    file_path_entry.insert(0, filename)  # Inserts the selected file path into the entry widget.

def submit():
    """
    Function invoked by the 'Send Email' button in the GUI.
    It gathers all the email information from the GUI, uploads the selected file via FTP, and sends the email.
    """
# This block of code is responsible for retrieving user input from the GUI fields.

    destination_email = destination_email_entry.get()  
    # Retrieves the text entered in the 'destination_email_entry' field.
    # This is where the user inputs the recipient's email address.

    subject = subject_entry.get()  
    # Retrieves the text entered in the 'subject_entry' field.
    # This is where the user inputs the subject of the email.

    email_text = email_text_entry.get("1.0", tk.END)  
    # Retrieves the text from the 'email_text_entry' Text widget.
    # "1.0" refers to the starting index (line 1, character 0) in the Text widget.
    # 'tk.END' specifies to get all the text up to the end of the text box.
    # This is where the user inputs the main body of the email.

    file_path = file_path_entry.get()  
    # Retrieves the text entered in the 'file_path_entry' field.
    # This is where the user inputs or selects the path of the file they want to attach to the email.

    # This block handles the process of uploading a file and sending an email.

    try:
        # The 'try' block is used to catch any exceptions that might occur during the execution of the enclosed code.

        file_link = upload_file_ftp(file_path)  
        # Calls the 'upload_file_ftp' function with the provided 'file_path'.
        # This function uploads the file located at 'file_path' to an FTP server.
        # It returns a link to the uploaded file, which is stored in 'file_link'.

        send_email(destination_email, subject, email_text, file_link)  
        # Calls the 'send_email' function with the recipient's email address, email subject, email text, and the link to the uploaded file.
        # This function sends an email with these details using the SMTP protocol.

        messagebox.showinfo("Success", "Email has been sent successfully!")  
        # If the email is sent successfully, this line displays a message box with a success message.
        # 'showinfo' is a function from tkinter.messagebox that shows an informational message box.

    except Exception as e:
        # If any exception occurs in the 'try' block, it is caught here.

        messagebox.showerror("Error", str(e))  
        # This line displays a message box with the error message.
        # 'showerror' is a function from tkinter.messagebox that shows an error message box.
        # 'str(e)' converts the exception object 'e' into a string that describes the error.


# Setting up the Tkinter GUI
root = tk.Tk()  
# 'root' is the main window (top-level widget) of the application. 'tk.Tk()' initializes Tkinter and creates this main window.

root.title("Email Sender UI")  
# Setting the title of the main window to "Email Sender UI".

# Creating and placing GUI widgets for email input fields and buttons.
tk.Label(root, text="Enter destination email:").pack()  
# Creates a label widget with the text "Enter destination email:" and adds it to the main window.
# The 'pack()' method is used to automatically place the label in the window.

destination_email_entry = tk.Entry(root, width=50)  
# Creates an entry widget for inputting the destination email and adds it to the main window.
# The 'width=50' sets the width of the input field to accommodate 50 characters.

destination_email_entry.pack()  
# Places the destination email entry widget in the main window using the 'pack()' method.

tk.Label(root, text="Enter email subject:").pack()  
# Creates and places a label for the email subject entry field.

subject_entry = tk.Entry(root, width=50)  
# Creates an entry widget for inputting the email subject.

subject_entry.pack()  
# Places the subject entry widget in the main window.

tk.Label(root, text="Enter email text:").pack()  
# Creates and places a label for the email text input area.

email_text_entry = tk.Text(root, height=10, width=50)  
# Creates a text widget for composing the email body. 'height=10' and 'width=50' set the size of the text box.

email_text_entry.pack()  
# Places the email text entry widget in the main window.

tk.Label(root, text="Enter path to the file to upload:").pack()  
# Creates and places a label for the file path entry field.

file_path_entry = tk.Entry(root, width=50)  
# Creates an entry widget for inputting the file path to upload.

file_path_entry.pack()  
# Places the file path entry widget in the main window.

browse_button = tk.Button(root, text="Browse", command=browse_file)  
# Creates a button labeled "Browse". When clicked, it will call the 'browse_file' function.

browse_button.pack()  
# Places the browse button in the main window.

submit_button = tk.Button(root, text="Send Email", command=submit)  
# Creates a button labeled "Send Email". When clicked, it will call the 'submit' function.

submit_button.pack()  
# Places the submit button in the main window.

root.mainloop()  
# Enters the main loop of the application. This call is blocking and waits for user interaction, such as button clicks.
