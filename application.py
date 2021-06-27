from flask import Flask, render_template, request, url_for, flash, redirect

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

@app.route('/compare', methods=('GET', 'POST'))
def compare():
    if request.method == 'POST':
        type = request.form['type']
        loc1 = request.form['loc1']
        loc2 = request.form['loc2']
        
        # Make the scrapping requests (this may take a few seconds)
        # scrape_for is a function imported from scraper.py
        if not (type and loc1 and loc2):
            flash('Required field needed')
        else:
            (prices1, stars1, images1) = scrape_for(type, loc1)
            (prices2, stars2, images2) = scrape_for(type, loc2)
        
            # calculate the averaged prices and stars of the separate locations
            place1_avg_price = avg_price(prices1)
            place1_avg_rating = avg_rating(stars1)

            place2_avg_price = avg_price(prices2)
            place2_avg_rating = avg_rating(stars2)
        
            # Determine the cheaper and higher rated places
            cheaper = loc2 if place1_avg_price > place2_avg_price else loc1
            higher_rating = loc2 if place2_avg_rating > place1_avg_rating else loc1
            #return redirect(url_for('result', type=type))
            return 'Cheaper place is: %s' % cheaper + '   Higher rating is: %s' % higher_rating
        
    return render_template('compare.html')

@app.route('/result/<type>')
def result(type):
   return 'welcome %s' % type
