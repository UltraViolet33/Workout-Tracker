from flask import Blueprint, request, render_template, redirect, url_for, request, flash
from . import db
from .models.Category import Category
from sqlalchemy.sql.expression import func
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


exercises = Blueprint("exercises", __name__)