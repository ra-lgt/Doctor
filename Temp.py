from datetime import datetime, timedelta
from email.utils import formatdate

# Get today's date
today = datetime.utcnow()

# Calculate the date one week later
one_week_later = today + timedelta(days=7)

# Format the date in the desired string format
formatted_date = formatdate(one_week_later.timestamp(), localtime=False)

print("hello")

