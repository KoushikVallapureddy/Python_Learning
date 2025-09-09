class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.host = "localhost"
        self.connected = False
    
    def connect(self):
        self.connected = True
        print("Connected to database at localhost")
    
    def disconnect(self):
        self.connected = False
        print("Disconnected from database")