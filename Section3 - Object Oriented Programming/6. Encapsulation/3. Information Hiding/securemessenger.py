class SecureMessenger:
    def __init__(self, username, password="secure123"):
        self.username = username
        self.__password = password
        self.__messages = []
        self.__login_attempts = 0
        self.__is_logged_in = False
    
    def add_message(self, message):
        if self.__is_logged_in:
            self.__messages.append(message)
            return f"Message added: {message}"
        return "Error: You must be logged in to add messages"
    
    def login(self, password):
        self.__login_attempts += 1
        if password == self.__password:
            self.__is_logged_in = True
            return "Login successful"
        return "Login failed: Incorrect password"
    
    def get_messages(self):
        if self.__is_logged_in:
            if not self.__messages:
                return "No messages"
            return "\n".join(self.__messages)
        return "Error: You must be logged in to view messages"
    
    def get_login_attempts(self):
        return f"Login attempts: {self.__login_attempts}"