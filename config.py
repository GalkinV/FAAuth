from datetime import timedelta

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 255

ACCESS_TOKEN_TTL = timedelta(hours=1)
REFRESH_TOKEN_TTL = timedelta(days=10)

TOKEN_LENGTH = 80
