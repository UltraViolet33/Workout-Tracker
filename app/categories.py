from flask import Blueprint, request, render_template, redirect, url_for, request, flash
from . import db
from .models.Category import Category
from sqlalchemy.sql.expression import func
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


categories = Blueprint("categories", __name__)

class CategoryForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])


@categories.route("/create", methods=["GET", "POST"])
def create_category():

    form = CategoryForm()

    if form.validate_on_submit():
        check_category_exits = Category.query.filter_by(name=form.name.data).first()

        if check_category_exits == None:

            category = Category(name=form.name.data)
            db.session.add(category)
            db.session.commit()
            flash("Category created !")
            return redirect("/categories/all")

        else:
            flash("Category name alreadry exist !", category="error")

    return render_template("formCategory.html", form=form)


@categories.route("/all", methods=["GET"])
def get_all_categories():

    categories = Category.query.all()
    return render_template("categories.html", categories=categories)


@categories.route("/edit/<id>", methods=["GET", "POST"])
def edit_category(id):

    category = Category.query.filter_by(id=id).first()
    form = CategoryForm()

    if category == None:
        flash("This category does not exist! ", category="error")
        return redirect("/categories/all")
    

    if form.validate_on_submit():
        check_category_exits = Category.query.filter(Category.name==form.name.data, Category.id != category.id).first()

        if check_category_exits == None:
            category.name = form.name.data 
            db.session.commit()
            flash("Category edited !")
            return redirect("/categories/all")

        else:
            flash("Category name alreadry exist !", category="error")
    
    return render_template("formCategory.html", category=category, form=form)
