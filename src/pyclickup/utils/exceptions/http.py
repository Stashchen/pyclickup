
class BadRequest(Exception):
    """Raised when HTTP response is not 2xx status code"""

class AuthTokenMissing(Exception):
    """Raised when there is no auth token found during authorization."""
