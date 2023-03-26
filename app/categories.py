from flask import Blueprint, render_template, redirect, flash
from . import db
from .models.Category import Category
from .forms import CategoryForm


categories = Blueprint("categories", __name__)


@categories.route("/all", methods=["GET"])
def get_all_categories():
    categories = Category.query.all()
    return render_template("categories.html", categories=categories)



@categories.route("/<id>", methods=["GET"])
def get_exos_category(id):
    category = Category.query.filter_by(id=id).first()
    return render_template("exosCategory.html", category=category, exos=category.exercises)




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
            flash("Category name already exists !", category="error")

    return render_template("formCategory.html", form=form)



@categories.route("/edit/<id>", methods=["GET", "POST"])
def edit_category(id):

    category = Category.query.filter_by(id=id).first()


    if category == None:
        flash("This category does not exist! ", category="error")
        return redirect("/categories/all")
    
    form = CategoryForm()

    if form.validate_on_submit():
        check_category_exits = Category.query.filter(Category.name==form.name.data, Category.id != category.id).first()

        if check_category_exits == None:
            category.name = form.name.data 
            db.session.commit()
            flash("Category edited !")
            return redirect("/categories/all")

        else:
            flash("Category name already exists !", category="error")
    
    return render_template("formCategory.html", category=category, form=form)



@categories.route("/delete/<id>")
def delete_categories(id):
    category = Category.query.filter_by(id=id).first()
    if not category:
        flash("This category does not exits", category="error")
        return redirect("/categories/all")
    
    db.session.delete(category)
    db.session.commit()
    flash("Category deleted !")
    return redirect("/categories/all")


