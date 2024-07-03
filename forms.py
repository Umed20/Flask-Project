from flask_wtf import FlaskForm
from wtforms import(
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired
import pandas as pd

## geting the data
train  = pd.read_csv("data/train.csv")
val  = pd.read_csv("data/val.csv")
X_data = pd.concat([train,val],axis=0).drop(columns="price")

class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=X_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )
    doj = DateField(
        label="Date of Journey",
        validators=[DataRequired()]
    )
    source = SelectField(
        label="Source",
        choices=X_data.source.unique().tolist(),
        validators=[DataRequired()]
    )
    destination = SelectField(
        label="Destination",
        choices=X_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )
    dept_time = TimeField(
        label="Departure Time",
        validators=[DataRequired()]
    )
    arrival_time = TimeField(
        label="Arrival Time",
        validators=[DataRequired()]
    )
    duration = IntegerField(
        label="Duration",
        
    )
    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices=X_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
