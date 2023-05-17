from flask import Blueprint, render_template, redirect, request, flash
from . import db
from .models.Category import Category
from .models.Exercise import Exercise
from .forms import ExerciseForm


exercises = Blueprint("exercises", __name__)


@exercises.route("/all", methods=["GET"])
def get_all_exos():
    exos = Exercise.query.all()
    return render_template("exos.html", exos=exos)


@exercises.route("/create", methods=["GET", "POST"])
def create_exercise():
    form = ExerciseForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]

    if form.validate_on_submit():
        check_exo_exits = Exercise.query.filter_by(name=form.name.data).first()

        if check_exo_exits == None:
            category = Category.query.filter_by(id=form.category.data).first()
            exo = Exercise(
                name=form.name.data, description=form.description.data, category=category)

            db.session.add(exo)
            db.session.commit()
            flash("Exo created !")
            return redirect("/exos/all")

        else:
            flash("Exo name alreadry exist !", category="error")

    return render_template("formExo.html", form=form)


@exercises.route("/edit/<id>", methods=["GET", "POST"])
def edit_exos(id):
    exo = Exercise.query.filter_by(id=id).first()
    form = ExerciseForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]

    if exo == None:
        flash("This exo does not exist! ", category="error")
        return redirect("/exos/all")

    if request.method == "GET":
        form.description.data = exo.description

    if form.validate_on_submit():
        check_exo_exits = Exercise.query.filter(
            Exercise.name == form.name.data, Exercise.id != exo.id).first()

        if check_exo_exits == None:
            exo.name = form.name.data
            exo.description = form.description.data
            exo.category = Category.query.filter_by(
                id=form.category.data).first()
            db.session.commit()
            flash("Exo edited !")
            return redirect("/exos/all")

        else:
            flash("Exo name alreadry exist !", category="error")

    return render_template("formExo.html", exo=exo, form=form)


@exercises.route("/delete/<id>")
def delete_exo(id):
    exo = Exercise.query.filter_by(id=id).first()
    if not exo:
        flash("This exo does not exits", category="error")
        return redirect("/exos/all")

    db.session.delete(exo)
    db.session.commit()
    flash("Exo deleted !")
    return redirect("/exos/all")
