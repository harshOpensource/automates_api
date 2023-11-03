from flask import Blueprint,request
import smtplib

def check_smtp_details(smtp_server, smtp_port, smtp_username, smtp_password):
    try:
        # Create an SMTP object to connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)

        # Start a TLS connection (for secure email sending)
        server.starttls()

        # Log in to the email account
        server.login(smtp_username, smtp_password)

        # Close the connection
        server.quit()

        return True  # SMTP details are valid
    except smtplib.SMTPAuthenticationError:
        return False  # Invalid username or password
    except smtplib.SMTPConnectError:
        return False  # Connection to the server failed
    except Exception as e:
        return False  # Other exceptions


async def create_account(prisma):
        data = request.get_json()
        smtp_port = data['port']
        smtp_server = data['smtp_server']
        smtp_username = data['smtp_username']
        smtp_password = data['smtp_password']
        email = data['email']
        session = data['session']

        if(session == "undefined"):
             return "Not Authenticated!"
        

        

           


        
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)


        if check_smtp_details(smtp_server, smtp_port, smtp_username, smtp_password):
            ('SMTP details are valid.')
        else:
            print('SMTP details are invalid.')

        
        return 'Account Tested successfully'
    



