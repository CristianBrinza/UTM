# ▒█▀▄▒█▀▄ lab. PR | FAF | FCIM | UTM | Fall 2023
# ░█▀▒░█▀▄ FAF-212 Cristian Brinza lab9



"""
This script sets up a simple SMTP (Simple Mail Transfer Protocol) server. SMTP is the protocol used for sending email messages between servers. 
It uses the aiosmtpd library, which is an asynchronous SMTP server framework, allowing it to handle multiple email transactions simultaneously.
"""

# Importing necessary classes from the aiosmtpd library.
# Controller: The main class to set up and control the SMTP server.
from aiosmtpd.controller import Controller

# Defining a custom handler for handling incoming SMTP connections and emails.
class SimpleMailHandler:
    """
    SimpleMailHandler is a custom handler for the SMTP server. 
    It defines what actions to take when the server receives an email.
    """

    # handle_DATA is a coroutine method that gets called when an email is received.
    # It receives parameters about the server, the session, and the email (envelope).
    async def handle_DATA(self, server, session, envelope):
        """
        Handles the incoming email data.

        Parameters:
        server: The server instance.
        session: The session object, containing details about the SMTP session.
        envelope: The envelope object, containing the email details.

        Envelope Attributes:
        mail_from: The sender's email address.
        rcpt_tos: A list of recipient email addresses.
        content: The actual content of the email (in bytes).
        """

        # Printing out details of the email.
        print('Mail from:', envelope.mail_from)  # Sender's email address.
        print('Mail to:', envelope.rcpt_tos)  # Recipient email addresses.
        
        # Decoding the email content from bytes to string using UTF-8 encoding.
        # 'errors=replace' means any decoding errors will replace problematic characters.
        print('Mail data:', envelope.content.decode('utf8', errors='replace'))
        
        # Returning an SMTP response code indicating successful receipt of the email.
        return '250 Message accepted for delivery'

# This conditional statement checks if the script is being run as the main program.
if __name__ == '__main__':
    """
    This block sets up and starts the SMTP server.
    It only executes if the script is run directly (not imported as a module).
    """

    # Creating an instance of Controller with our custom handler, specifying the server's address and port.
    controller = Controller(SimpleMailHandler(), hostname='localhost', port=1025)
    
    # Starting the SMTP server.
    controller.start()

    # Informing the user that the SMTP server is running and how to stop it.
    print('SMTP server running on localhost:1025. Press Ctrl+C to stop.')

    # This loop keeps the script running indefinitely until interrupted by the user.
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Handling a keyboard interrupt (Ctrl+C) to stop the server gracefully.
        pass

    # Stopping the SMTP server when the script is interrupted.
    controller.stop()
