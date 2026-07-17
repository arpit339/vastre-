class ResourceNotFound(Exception):
    def __init__(self, message="Resource not found"):
        self.message = message
