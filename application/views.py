# views.py - Test of MapItGIS and PostgreSQL integration
# April 2, 2019
# by Nicole White
# This script contains the views and URLs for test web map.

#Import the app object, the flask functions, and the application forms and models
from application import app
from flask import render_template,jsonify, redirect, url_for, request
from .forms import *
from .models import *
from shapely import wkb

@app.route('/', methods=["GET"])
def home():
	return redirect(url_for('avtc'))

@app.route('/avtc', methods=["GET","POST"])
def avtc():

	# Query everything from the culverts table
	culverts = session.query(Culvert).all()

	# Loop through all culvert records
	for culvert in culverts:

		# Use shapely's wkb.loads() to turn WKB into lat long
		# Format output as GeoJSON
		culvert_pts =[[wkb.loads(bytes(culverts[j].wkb_geometry.data)).x,
		               wkb.loads(bytes(culverts[j].wkb_geometry.data)).y] for j, item in enumerate(culverts)]


	return render_template('index.html',culvert_pts=culvert_pts)
