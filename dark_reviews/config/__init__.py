import os

from config import dev, prod

INDEX = globals()[os.getenv("location", "prod")].INDEX
