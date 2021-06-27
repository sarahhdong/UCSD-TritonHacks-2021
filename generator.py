import sys
import math
from convert import calculate_moons

# HTML Template. We fill the "{}" areas with actual content
HTML_FORMAT = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Price Comparison App</title>
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="./css_template.css">
   
  </head>  
  <body>
     <!--Title-->
     <h1 id="title">Statistics Comparison of {}</h1>
    
    <!--Board-->
    <div id="board">
      {}
    </div>
  </body>
</html>
"""

# Single Picture
ITEM_FORMAT = """
  <div class="slide">
    <!--location-->
    <h2>{location}</h2>
    <!--average rating-->
    <div><strong>Average rating:</strong>{rating}</div>
    <!--average price-->
    <div><strong>Average price:</strong>{price}</div>
    <!--Image-->
    <div class="imageCollage">
      {images}
    </div>
  </div>
"""

HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Price Comparison App</title>
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="./css_template.css">
   
  </head>  
  <body>
     <!--Title-->
     <h1 id="title">Welcome to the Location Comparator App!</h1>
     <br>

     <h2 form id = "form" onsubmit = "return false;>
      <label for="food-type">Food Type:</label><br>
      <input type="text" id="food-type" name="food-type">
      <br>
      <br>

      <label for="first-city">First City:</label><br>
      <input type="text" id="firstcity" name="first-city">
      <br>
      <br>

      <label for="second-city">Second City:</label><br>
      <input type="text" id="second-city" name="second-city">
      <br>
      <br>

      <input type="submit"/>

    </form></h2>

    
    
  </body>
</html>
"""

# Write findings to out.html
def generate(item, dataList):
  middle = ""
  for data in dataList:

    # Calculate average rating & price, display with moon emoji
    rating, rating_int = calculate_moons(data['rating'], 4)
    price, price_int = calculate_moons(data['price'], 5)

    # Insert image links and append to image string
    images_string = ""
    for url in data['images']:
      images_string += """<img src="{}">""".format(url) + "\n"

    
    # Using the ITEM_FORMAT template, we fill in the rest of the information
    # including the location, rating, price, and images
    middle += ITEM_FORMAT.format(location=data['location'], 
              rating = rating + "(" + str(rating_int) + ")",
              price  = price + "(" + str(price_int) + ")",
              images = images_string)

  with open("index.html", "w+") as new_file:
    new_file.write(HTML_FORMAT.format(item, middle))

def homePage():
  with open("index.html", "w+") as new_file:
    new_file.write(HOME_HTML)
  print('written homepage')