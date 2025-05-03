from datetime import datetime
from datetime import timezone, timedelta

# Get the current date and time
current_time = datetime.now()

# Print a welcoming message
print("Hell, User! Welcome!")

# Print the current date and time
# Convert the current time to GMT+7
gmt_plus_7_time = current_time.astimezone(timezone(timedelta(hours=7)))

print("The current date and time is:", gmt_plus_7_time.strftime("%Y-%m-%d %H:%M:%S"))