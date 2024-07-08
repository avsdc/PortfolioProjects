#Import statements

from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt 

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Create class CafeForm that takes as parameter FlaskForm. add: Location URL, open time, closing time, coffee rating, tea rating, smoothie,
# breakfast, lunch and bakery rating, wifi rating, power outlet rating fields
# make coffee/tea/smoothie/breakfast/lunch/bakery/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/🍵/🥤/🥯/🥪/🧁/💪/🔌

class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8:00 A.M', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30 P.M', validators=[DataRequired()])
    coffee = SelectField("Coffee Rating", choices=[(1, "☕"), (2, "☕☕"), (3, "☕☕☕"), (4, "☕☕☕☕"), (5, "☕☕☕☕☕")], validators=[DataRequired()])
    tea = SelectField("Tea Rating", choices=[(1, "🍵"), (2, "🍵🍵"), (3, "🍵🍵🍵"), (4, "🍵🍵🍵🍵"), (5,"🍵🍵🍵🍵🍵")], validators=[DataRequired()])
    smoothie = SelectField("Smoothie Rating", choices=[(1, "🥤"), (2, "🥤🥤"), (3, "🥤🥤🥤"), (4, "🥤🥤🥤🥤"), (5, "🥤🥤🥤🥤🥤")], validators=[DataRequired()])
    breakfast = SelectField("Breakfast Rating", choices=[(1, "🥯"), (2, "🥯🥯"), (3, "🥯🥯🥯"), (4, "🥯🥯🥯🥯"), (5, "🥯🥯🥯🥯🥯")], validators=[DataRequired()])
    lunch = SelectField("Lunch Rating", choices=[(1, "🥪"), (2, "🥪🥪"), (3, "🥪🥪🥪"), (4, "🥪🥪🥪🥪"), (5, "🥪🥪🥪🥪🥪")], validators=[DataRequired()])
    bakery = SelectField("Bakery Rating", choices=[(1, "🧁"), (2, "🧁🧁"), (3, "🧁🧁🧁"), (4,"🧁🧁🧁🧁"), (5,"🧁🧁🧁🧁🧁")], validators=[DataRequired()])
    wifi = SelectField("Wifi Strength Rating", choices=[(1, "💪"), (2, "💪💪"), (3, "💪💪💪"),(4, "💪💪💪💪"), (5, "💪💪💪💪💪")], validators=[DataRequired()])
    power = SelectField("Power Socket Availability", choices=[(1, "🔌"),(2, "🔌🔌"),(3, "🔌🔌🔌"),(4, "🔌🔌🔌🔌"),(5, "🔌🔌🔌🔌🔌")],validators=[DataRequired()])
    submit = SubmitField('Submit')


# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    open_time: Mapped[str] = mapped_column(String(250), nullable=False)
    close_time: Mapped[str] = mapped_column(String(250), nullable=False)
    coffee: Mapped[float] = mapped_column(Float, nullable=False)
    tea: Mapped[float] = mapped_column(Float, nullable=False)
    smoothie: Mapped[float] = mapped_column(Float, nullable=False)
    breakfast: Mapped[float] = mapped_column(Float, nullable=False)
    lunch: Mapped[float] = mapped_column(Float, nullable=False)
    bakery: Mapped[float] = mapped_column(Float, nullable=False)
    wifi: Mapped[float] = mapped_column(Float, nullable=False)
    power: Mapped[float] = mapped_column(Float, nullable=False)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


# all Flask routes below

#Display the home page
@app.route("/")
def home():
    return render_template("index.html")

#Add another cafe
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.name.data
        cafe_location = form.location.data
        cafe_open_time = form.open_time.data
        cafe_close_time = form.close_time.data
        cafe_coffee = form.coffee.data
        cafe_tea = form.tea.data
        cafe_smoothie = form.smoothie.data
        cafe_breakfast = form.breakfast.data
        cafe_lunch = form.lunch.data
        cafe_bakery = form.bakery.data
        cafe_wifi = form.wifi.data
        cafe_power = form.power.data

        new_cafe = Cafe(
            name = cafe_name,
            location = cafe_location,
            open_time = cafe_open_time,
            close_time = cafe_close_time,
            coffee = cafe_coffee,
            tea = cafe_tea,
            smoothie = cafe_smoothie,
            breakfast = cafe_breakfast,
            lunch = cafe_lunch,
            bakery = cafe_bakery,
            wifi = cafe_wifi,
            power = cafe_power
        )
        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


#Display all cafes
@app.route('/cafes')
def cafes():
    #READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_cafes = result.scalars().all()
    return render_template("cafes.html", cafes=all_cafes)


#Edit a cafe using edit link
@app.route('/edit', methods=["GET", "POST"])
def edit_cafe():
        cafe_id = request.args.get("id")
        cafe = db.get_or_404(Cafe, cafe_id)

        edit_form = CafeForm(
            name=cafe.name,
            location=cafe.location,
            open_time=cafe.open_time,
            close_time=cafe.close_time,
            coffee=cafe.coffee,
            tea=cafe.tea,
            smoothie=cafe.smoothie,
            breakfast=cafe.breakfast,
            lunch=cafe.lunch,
            bakery=cafe.bakery,
            wifi=cafe.wifi,
            power=cafe.power
        )
        if edit_form.validate_on_submit():
            cafe.name = edit_form.name.data
            cafe.location = edit_form.location.data
            cafe.open_time = edit_form.open_time.data
            cafe.close_time = edit_form.close_time.data
            cafe.coffee = edit_form.coffee.data
            cafe.tea = edit_form.tea.data
            cafe.smoothie = edit_form.smoothie.data
            cafe.breakfast = edit_form.breakfast.data
            cafe.lunch = edit_form.lunch.data
            cafe.bakery = edit_form.bakery.data
            cafe.wifi = edit_form.wifi.data
            cafe.power = edit_form.power.data
            db.session.commit()
            return redirect(url_for("cafes", cafe_id=cafe.id))
        return render_template("add.html", form=edit_form, is_edit=True)

#Delete a cafe using the delete link
@app.route('/delete')
def delete():
           cafe_id = request.args.get("id")
           cafe = db.get_or_404(Cafe, cafe_id)
           db.session.delete(cafe)
           db.session.commit()
           return redirect(url_for("cafes"))


if __name__ == '__main__':
    app.run(debug=True)
