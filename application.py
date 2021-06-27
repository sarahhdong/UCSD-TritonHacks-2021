from flask import Flask, render_template, request, url_for, flash, redirect

# Entrypoint to your webscraping starter kit
import os         # Used to open html page after scraping
import webbrowser
import sys        # Used to end program if error occurs

from convert import avg_price, avg_rating
from scraper import scrape_for, getHotel
from scraper import getweather
from generator import generate, homePage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/foodcompare', methods=('GET', 'POST'))
def foodcompare():
    if request.method == 'POST':
        type = request.form['type']
        loc1 = request.form['loc1']
        loc2 = request.form['loc2']

        # Make the scrapping requests (this may take a few seconds)
        # scrape_for is a function imported from scraper.py
        if not (type and loc1 and loc2):
            flash('Required field needed')
        else:
            try:
                (prices1, stars1, images1) = scrape_for(type, loc1)
                (prices2, stars2, images2) = scrape_for(type, loc2)

                # calculate the averaged prices and stars of the separate locations
                place1_avg_price = avg_price(prices1)
                place1_avg_rating = avg_rating(stars1)

                place2_avg_price = avg_price(prices2)
                place2_avg_rating = avg_rating(stars2)

            except Exception as e:
                flash('Bad input, please re-enter.')
                return render_template('foodcompare.html')
                #return("Input value is not corret. Please re-enter")

            # Determine the cheaper and higher rated places
            #cheaper = loc2 if place1_avg_price > place2_avg_price else loc1
            #higher_rating = loc2 if place2_avg_rating > place1_avg_rating else loc1

            return redirect(url_for('result', type=type, loc1=loc1, loc2=loc2, place1_avg_price=place1_avg_price, place2_avg_price=place2_avg_price, place1_avg_rating=place1_avg_rating, place2_avg_rating=place2_avg_rating, cheaper=cheaper, higher=higher_rating))
            #return 'Cheaper place is: %s' % cheaper + '   Higher rating is: %s' % higher_rating
            #return 'star1 is: %s' % cheaper + '   Higher rating is: %s' % higher_rating

            if place1_avg_price > place2_avg_price:
                pricecmp = 'The cheaper place is: ' + loc2
            elif place1_avg_price == place2_avg_price:
                pricecmp = 'The average price for the two locations are the same'
            else:
                pricecmp = 'The cheaper place is: ' + loc1

            if place2_avg_rating > place1_avg_rating:
                ratecmp = 'The higher rate place is: ' + loc2
            elif place1_avg_rating == place2_avg_rating:
                ratecmp = 'The avarage rating for the two locations are the same'
            else:
                ratecmp = 'The higher rate place is: ' + loc1

            return redirect(url_for('result', type=type, loc1=loc1, loc2=loc2, place1_avg_price=place1_avg_price, place2_avg_price=place2_avg_price, place1_avg_rating=place1_avg_rating, place2_avg_rating=place2_avg_rating, pricecmp=pricecmp, ratecmp=ratecmp))


    return render_template('foodcompare.html')

 @app.route('/result/<type>/<loc1>/<loc2>/<place1_avg_price>/<place2_avg_price>/<place1_avg_rating>/<place2_avg_rating>/ <pricecmp>/<ratecmp>')
def result(type, loc1, loc2, place1_avg_price, place2_avg_price, place1_avg_rating, place2_avg_rating, pricecmp, ratecmp):
    return render_template('result.html', type=type, loc1=loc1, loc2=loc2, place1_avg_price=place1_avg_price, place2_avg_price=place2_avg_price, place1_avg_rating=place1_avg_rating, place2_avg_rating=place2_avg_rating, pricecmp=pricecmp, ratecmp=ratecmp)

@app.route('/hotel', methods=('GET', 'POST'))
def hotel():
    if request.method == 'POST':
        city1 = request.form['city1']
        city2 = request.form['city2']

        if not (city1 and city2):
            flash('Required field needed')
        else:
            try:
                (hotels1, prices1) = getHotel(city1)
                (hotels2, prices2) = getHotel(city2)

                city1_avg = avg_price(prices1)
                city2_avg = avg_prices(prices2)

                cheaper = city2 if city1_avg > city2_avg else city1
                return (cheaper + " is cheaper on average")
            except Exception as e:
                flash('Bad input, please re-enter')
                return render_template('hotel.html')

            return render_template('hotel.html')
    return render_template('hotel.html')
