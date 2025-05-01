import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(recipient, subject, body):
    # Email account credentials
    sender_email = "abcd@gmail.com"
    password = "#######"  # Use app password for Gmail

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject

    # Attach body text
    message.attach(MIMEText(body, "plain"))

    # Send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        server.quit()
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error sending email: {e}")


# Example usage
send_email("abcd@hotmail.com", "Automated Email", "This email was sent using Python automation!")