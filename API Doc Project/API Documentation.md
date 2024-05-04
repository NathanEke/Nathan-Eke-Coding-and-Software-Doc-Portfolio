# GetMyWeather API
The **GetMyWeather** API is a useful tool that allows developers to embed simple weather forecasts into their websites and applications.
## Introduction
**GetMyWeather** allows developers to embed "micro-forecasts" into their websites. These forecasts accept user input based on various parameters and data types that will further specify the location and timing of the forecast. This API could be useful for a variety of applications such as:
* An outdoor event planning website that wants attendees to be able to view the forecast at the time and location of an activity.
* Realtor websites that want to give buyers an idea of the weather patterns in a particular neighborhood.
## Prerequisites 
**GetMyWeather** is supported by all modern browsers that support Javascript. Javascript must be enabled to use **GetMyWeather**.

To access the **GetMyWeather** API, you will need an API key. You can register for one at https://getmyweather.com. Pricing information will be available on the website. A no-cost key is available for testing and development purposes.
## The getWeather Method
The **getWeather** method works off of these parameters:
* *Location*
* *Specificity*
* *Time*

These parameters help specify what weather data the user needs.

## Parameters
**getWeather** has three parameters for fetching specific weather data, each accepting different legal values for user input.
### Location
*Location* is one of two parameters that specify the area that **getWeather's** "micro-forecast" covers. *Location* accepts legal values in the form of coordinates, expressed as *latitude/longitude*, in ISO 6709 format. You might use *location* to find the weather forecast for a particular neighborhood.
### Specificity
*Specificity* is one of two parameters that specify the area that **getWeather's** "micro-forecast" covers. It defines a circular area around the *location*, accepting a radius of 5 meters (minimum) to 150,000 meters (maximum) for legal values. You might use *specificity* to single out a house in a larger neighborhood. 

**NOTE:** The larger the *specificity* value, the less accurate the forecast will be (learn more in the *trust* section).
### Time
*Time* is the parameter that specifies how many hours into the future that the "micro-forecast" will cover. *Time* accepts legal values in the form of hours, with a minimum of 0 (which would show you the current weather forecast). Decimals are acceptable. You might use time to find out the forecast 48 hours (two days) into the future.

**NOTE:** The larger the *time* value, the less accurate the forecast will be (learn more in the *trust* section). Forecasts of greater than 240 hours (10 days) in the future are unreliable and are based on historical averages for a location.
## Return Value
**getWeather** has a unique return value, in the form of the *trust* value. 
### Trust
*Trust* is a return value that indicates how reliable **getWeather's** forecast is. It goes from 1 (least reliable) to 100 (most reliable). Reliability is determined by *specificity* and *time*. A large *specificity* area will lower *trust*, as will a large *time* value. A 10 or lower *trust* value indicates that the forecast is based on historical averages for the location, not on anticipated weather patterns. A low *trust* value may be an indication to lower your *specificity* and *time* values, or to check other weather forecast services for a second opinion.
## Code Samples
Here are some examples of what the **getWeather** API might look like in javascript.
### Initialize getWeather
    <script type="text/javascript">
    var weatherForecast;
    function init() {
    weatherForecast =
    new getWeather(document.getElementById('forecast')}
    </script>
### Call getWeather
Here is a code sample for the forecast at a spot near the lake in Schenley Park, 4 days from now, with a radius of 100 meters:

    <script async defer
    src="https://www.getmyweather.com/getWeather?
    key=<YOUR_KEY>&
    callback=init&
    location=<40.43>:<-79.94>&
    specificity=<100>&
    time=<96>">
    </script>
### Return Package
Time between invoking the getWeather method and the return package is negligible. Most web applications will not require a GUI indication that the application is waiting for a result.

The resulting forecast will return temperature in Fahrenheit, wind speed in miles per hour, chance of rain in percentage, and the *trust* value. These return packages are static, you must call **getWeather** again with new parameter values to generate a new forecast. 

    <div class="forecast">
        <div class="temperature">78</div>
        <div class="windspeed">15</div>
        <div class="chanceRain">30</div>
        <div class="trust">80</div>
    </div>
#### Errors
The following are error strings **getWeather** may produce and explanations for each:
* "Invalid key"
    * Your API key was not recognized or permissions were revoked.
* "Invalid parameter format"
    * *Location*, *specificity*, or *time* parameters were not given proper legal values.
* "Parameter out of range"
    * *Location*, *specificity*, or *time* parameters were given values outside of their minimum or maximum range.
* "Server unavailable/Forecast failed
    * API server is currently overloaded.
