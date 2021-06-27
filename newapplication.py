from flask import Flask, render_template, request, url_for, flash, redirect
import re

# Entrypoint to your webscraping starter kit
import os         # Used to open html page after scraping
import webbrowser
import sys        # Used to end program if error occurs

from convert import avg_price, avg_rating
from scraper import scrape_for
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

                place1_avg_price = avg_price(prices1)
                place2_avg_price = avg_price(prices2)

                firstHot1 = hotels1[0]
                firstHot2 = hotels2[0]

                firstHot1_price = prices1[0]
                firstHot2_price = prices2[0]

                cheaper = city2 if city1_avg > city2_avg else city1
                pricecmp = (cheaper + " has cheaper hotels on average")

                return redirect('hotelresult.html', city1=city1, city2=city2, firstHot1=firstHot1, firstHot2=firstHot2, firstHot1_price=firstHot1_price, firstHot2_price=firstHot2_price, pricecmp=pricecmp)



            except Exception as e:
                flash('Bad input, please re-enter')
                return render_template('hotel.html')

            return render_template('hotel.html')
    return render_template('hotel.html')

<<<<<<< HEAD

@app.route('/weather', methods=('GET', 'POST'))
def weather():
    if request.method == 'POST':
        city1 = request.form['city1']
        city2 = request.form['city2']
        
        ns_place1 = re.sub(' ', '-', city1);
        ns_place2 = re.sub(' ', '-', city2);
        if not (city1 and city2):
            flash('Required field needed')
        else:
            try:
                (temp1, symbol1) = getweather(city1)
                (temp2, symbol2) = getweather(city2)

                warmer = city2 if temp2 > temp1 else city1
                givedeg = "{} is currently {}, while {} is {}"
                print(givedeg.format(city1,temp1,city2,temp2))
                return (warmer + "is warmer")

            except Exception as e:
                flash('Bad input, please re-enter')
=======
@app.route('/hotelresult/<city1>/<city2>/<firstHot1>/<firstHot2>/<firstHot1_price>/<firstHot2_price>/ <pricecmp1>')
def hotelresult(city1, city2, firstHot1, firstHot2, firstHot1_price, firstHot2_price, pricecmp1):
    return render_template('hotelresult.html', city1=city1, city2=city2, firstHot1=firstHot1, firstHot2=firstHot2, firstHot1_price=firstHot1_price, firstHot2_price=firstHot2_price, pricecmp=pricecmp)


>>>>>>> f3d077200421a80ef18b826ad7a5667d5305b52a