from flask import render_template, redirect, flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app