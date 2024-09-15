# Layover time computation script

This repository contains a Python script that computes layover times at airports based on flight data. The script collects flight information from the [AviationStack API](https://aviationstack.com/), processes it, and calculates layover times for a selected airport within a specified time window.

## Overview

The script calculates the difference between arrival and departure times for each aircraft at a given airport. The key steps include:
1. **Data Collection:** Fetching arrival and departure data from the AviationStack API for a specified airport and date range.
2. **Layover Calculation:** Computing layover times based on the difference between the arrival time of a flight and the departure time of the next flight for the same aircraft.
3. **Data Filtering:** Only layover times that fall within a defined window (e.g., 30 minutes to 8 hours) are considered.
4. **Plotting Results:** Generating visualizations of layover time distributions.

## Requirements

- **Python 3.6+**
- **Libraries:**
  - `requests`
  - `pandas`
  - `matplotlib`
  
  Install the necessary libraries using the following command:
  ```bash
  pip install -r requirements.txt
  ```

## Configuration

You need to configure the following parameters in the `inputs.py` file:
- `airport_code`: The IATA code of the airport (e.g., `DXB`, `LHR`).
- `start_date`: Start date for data collection (in `YYYY-MM-DD` format).
- `end_date`: End date for data collection (in `YYYY-MM-DD` format).
- `min_layover_time`: Minimum layover time in minutes (e.g., 30).
- `max_layover_time`: Maximum layover time in minutes (e.g., 480).

Additionally, update the `API_KEY` in the `config.py` file with your AviationStack API key.

## Running the Script

To run the script, simply execute the following command:

```bash
python compute_layover.py
```

This will collect flight data from the specified airport within the date range, calculate layover times, and generate a visual representation of the layover distribution.

## Example

An example of usage for Dubai International Airport (DXB) with a 3-month data range from June to August 2024:

```python
airport_code = 'DXB'
start_date = '2024-06-01'
end_date = '2024-08-31'
min_layover_time = 30
max_layover_time = 480
```

## Limitations

- **Computation Time:** Processing large datasets may take several hours. For instance, analyzing 30 million possibilities for an airport like DXB or LHR can take over 8 hours.
- **API Limitations:** The script is subject to API rate limits, which may restrict the amount of data that can be collected in one run.

## Results

The script outputs:
- A PNG image showing the distribution of layover times.
- Insights into typical layover durations at the selected airport.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
