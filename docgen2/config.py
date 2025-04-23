import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into the environment

OPENAI_API_KEY     = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL       = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.4"))
OPENAI_MAX_TOKENS  = int(os.getenv("OPENAI_MAX_TOKENS", "400"))
MAX_CODE_CHUNKS    = int(os.getenv("MAX_CODE_CHUNKS", "10"))