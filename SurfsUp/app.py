# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables

Base.prepare(engine, reflect=True)

# Save references to each table

measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB

session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)



#################################################
# Flask Routes
#################################################
app = Flask(__name__)

# Create Flask Routes 

# Create root route

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes for Hawaii Weather Data:<br/><br>"
        f"-- Daily Precipitation Totals for Last Year: <a href=\"/api/v1.0/precipitation\">/api/v1.0/precipitation<a><br/>"
        f"-- Active Weather Stations: <a href=\"/api/v1.0/stations\">/api/v1.0/stations<a><br/>"
        f"-- Daily Temperature Observations for Station USC00519281 for Last Year: <a href=\"/api/v1.0/tobs\">/api/v1.0/tobs<a><br/>"
        f"-- Min, Average & Max Temperatures for Date Range: /api/v1.0/trip/yyyy-mm-dd/yyyy-mm-dd<br>"
        f"NOTE: If no end-date is provided, the trip api calculates stats through 08/23/17<br>" 
    )
# Create a route that queries precipiation levels and dates and returns a dictionary using date as key and precipation as value
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all daily precipitation totals for the last year"""
    
    # Create new variable to store results from query to Measurement table for prcp and date columns
   start_date = '2016-08-23'
    sel = [measurement.date, 
        func.sum(measurement.prcp)]
    precipitation = session.query(*sel).\
            filter(measurement.date >= start_date).\
            group_by(measurement.date).\
            order_by(measurement.date).all()

    # Close session
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
        # 1. Create an empty list of precipitation query values 
        # 2. Create for loop to iterate through query results (precipitation_query_results) 
        # 3. Create dictionary with key "precipitation" set to prcp from precipitation_query_results and key "date" to date from precipitation_query_results
        # 4. Append values from precipitation_dict to your original empty list precipitation_query_values 
        # 5. Return JSON format of your new list that now contains the dictionary of prcp and date values to your browser
    
    precipitation_dates = []
    precipitation_totals = []

    for date, dailytotal in precipitation:
        precipitation_dates.append(date)
        precipitation_totals.append(dailytotal)
    
    precipitation_dict = dict(zip(precipitation_dates, precipitation_totals))

    return jsonify(precipitation_dict)

# Create a route that returns a JSON list of stations from the database
@app.route("/api/v1.0/stations")
def stations(): 

    session = Session(engine)

    """Return a list of stations from the database""" 
   
    sel = [measurement.station]
    active_stations = session.query(*sel).\
        group_by(measurement.station).all()
    session.close()

   
   list_of_stations = list(np.ravel(active_stations)) 
    return jsonify(list_of_stations)


# Create a route that queries the dates and temp observed for the most active station for the last year of data and returns a JSON list of the temps observed for the last year
@app.route("/api/v1.0/tobs") 
def tobs():
   
    session = Session(engine)
    
    """Return a list of dates and temps observed for the most active station for the last year of data from the database""" 
    # Create query to find the last date in the database
    
    start_date = '2016-08-23'
    sel = [measurement.date, measurement.tobs]
    station_temps = session.query(*sel).\
            filter(measurement.date >= start_date, measurement.station == 'USC00519281').\
            group_by(measurement.date).\
            order_by(measurement.date).all()

    print(year_query_results)
    # last_year_date returns row ('2017-08-23',), use this to create a date time object to find start query date 
    
    # check to see if last year was correctly returned by creating dictionary to return last year value to browser in JSON format
    year_query_values = []
    for date in last_year_query_results:
        year_dict = {}
        year_dict["date"] = date
        year_query_values.append(year_dict) 
    print(year_query_values)
    # returns: [{'date': '2017-08-23'}]

    # Create query_start_date by finding the difference between date time object of "2017-08-23" - 365 days
  
    # returns: 2016-08-23 

    # Create query to find most active station in the database 


    # Create a query to find dates and tobs for the most active station (USC00519281) within the last year (> 2016-08-23)

    

    # Create a list of dates,tobs,and stations that will be appended with dictionary values for date, tobs, and station number queried above

# Create a route that when given the start date only, returns the minimum, average, and maximum temperature observed for all dates greater than or equal to the start date entered by a user

# Define function, set "start" date entered by user as parameter for start_date decorator 


    # Create query for minimum, average, and max tobs where query date is greater than or equal to the date the user submits in URL


    # Create a list of min,max,and average temps that will be appended with dictionary values for min, max, and avg tobs queried above


# Create a route that when given the start date only, returns the minimum, average, and maximum temperature observed for all dates greater than or equal to the start date entered by a user


# Define function, set start and end dates entered by user as parameters for start_end_date decorator

    
    # Create query for minimum, average, and max tobs where query date is greater than or equal to the start date and less than or equal to end date user submits in URL

   
  
    # Create a list of min,max,and average temps that will be appended with dictionary values for min, max, and avg tobs queried above
    
