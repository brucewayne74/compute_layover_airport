# inputs.py

from datetime import datetime, timedelta

# Input parameters
airport_code = 'DXB'  # Example airport code
start_date = datetime(2023, 1, 1)  # Example start date
end_date = datetime(2023, 4, 1)   # Example end date
use_cached = False  # Set to False if you want to fetch new data from the API

# Time window for layover calculation
min_layover_time = timedelta(minutes=15) # in minutes
max_layover_time = timedelta(hours=8.25) # in hours
