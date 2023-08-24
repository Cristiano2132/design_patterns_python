class SMS:
    def send_sms(self, recipient, message):
        return f"Sending SMS to {recipient}: {message}"

class Email:
    def send_email(self, recipient, subject, message):
        return f"Sending Email to {recipient} - Subject: {subject}, Message: {message}"

class PushNotification:
    def push(self, recipient, message):
        return f"Pushing Notification to {recipient}: {message}"

class MessagingAdapter:
    def __init__(self, messaging_service):
        self.messaging_service = messaging_service

    def send_message(self, recipient, message):
        if isinstance(self.messaging_service, SMS):
            return self.messaging_service.send_sms(recipient, message)
        elif isinstance(self.messaging_service, Email):
            return self.messaging_service.send_email(recipient, "Chat Notification", message)
        elif isinstance(self.messaging_service, PushNotification):
            return self.messaging_service.push(recipient, message)

if __name__ == "__main__":
    # Usage
    sms_service = SMS()
    email_service = Email()
    push_service = PushNotification()

    sms_adapter = MessagingAdapter(sms_service)
    email_adapter = MessagingAdapter(email_service)
    push_adapter = MessagingAdapter(push_service)

    print(sms_adapter.send_message("Alice", "Hello from chat app!"))  # Output: Sending SMS to Alice: Hello from chat app!
    print(email_adapter.send_message("Bob", "Chat invitation"))       # Output: Sending Email to Bob - Subject: Chat Notification, Message: Chat invitation
    print(push_adapter.send_message("Charlie", "New message"))        # Output: Pushing Notification to Charlie: New message
