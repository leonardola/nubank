#!/usr/bin/env python3
from flask import Flask, request, jsonify, redirect
from flask import render_template
from Entity.Movement import Movement
from Entity.Category import Category
from Entity.Movement_has_Category import Movement_has_Category
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
from pynubank.nubank import Nubank
from Importer import Importer
import yaml

app = Flask(__name__)


@app.route("/addMovement/<year>/<month>", methods=['POST'])
def addMovement(year, month):
    movement = Movement.create(
        date=request.form['date'],
        original_name=request.form['name'],
        value=request.form['value'],
        type=request.form['type'],
        status='SHOW'
    )
    movement.save()

    return redirect("/" + year + "/" + month)


@app.route("/removeMovement/<movement_id>", methods=['POST'])
def removeMovement(movement_id):
    movement = Movement.get(id=movement_id)
    movement.status = Movement.STATUS_HIDE
    movement.save()
    return "ok"


@app.route("/changeMovementName/<movement_id>", methods=['POST'])
def changeMovementName(movement_id):
    movement = Movement.get(id=movement_id)
    movement.edited_name = request.form['newName']
    movement.save()
    return "ok"


@app.route("/", defaults={'month': None, 'year': None})
@app.route("/<year>/<month>")
def list(year, month):
    if not month:
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)

    try:
        movements = Movement.select().where(
            Movement.date.between(year + '-' + month + '-01', year + '-' + month + '-31')).order_by(Movement.date.asc())

        months = getMonthsList()

        total = 0
        totalIncome = 0
        totalOutcome = 0
        for movement in movements:
            if movement.status == 'SHOW':
                if movement.type == 'OUTCOME':
                    total = total - movement.value
                    totalOutcome = totalOutcome + movement.value
                else:
                    total = total + movement.value
                    totalIncome = totalIncome + movement.value

        return render_template(
            'movements.jinja2',
            movements=movements,
            total=total,
            months=months,
            totalIncome=totalIncome,
            totalOutcome=totalOutcome,
            year=year,
            month=month
        )

    except:
        return render_template(
            'movements.jinja2',
            movements=[],
            total=0,
            months=[],
            totalIncome=0,
            totalOutcome=0
        )


def getMonthsList():
    firstMovement = Movement.select().order_by(Movement.date.asc()).get()
    firstMovement.date = firstMovement.date + relativedelta(months=-1)
    lastMovement = Movement.select().order_by(Movement.date.desc()).get()

    startDate = datetime.datetime.strftime(firstMovement.date, '%Y-%m-%d')
    endDate = datetime.datetime.strftime(lastMovement.date, '%Y-%m-%d')

    months = pd.date_range(startDate, endDate,
                           freq='MS').strftime("%b-%Y$%Y/%m").tolist()
    return months


@app.route("/addTag/<movement_id>", methods=['POST'])
def addCategory(movement_id):
    name = request.form['name']
    try:
        category = Category.get(name=name)
    except:
        category = Category.create(name=name)
        category.save()

    movement = Movement.get(id=movement_id)
    Movement_has_Category.create(movement=movement, category=category).save()

    return jsonify({'id': category.id})


@app.route("/getTags/<movement_id>")
def getMovmentTags(movement_id):
    tags = Category.select().join(Movement_has_Category).join(Movement).where(Movement.id == movement_id)

    tags_list = []
    for tag in tags:
        tags_list.append({"id": tag.id, "name": tag.name})

    return jsonify(tags_list)


@app.route("/getTags")
def getTags():
    tags = Category.select().execute()
    tags_list = []
    for tag in tags:
        tags_list.append(tag.name)

    return jsonify(tags_list)


@app.route("/removeMovementTag/<movement_id>/<tag_id>", methods=['POST'])
def removeMovementTag(movement_id, tag_id):
    Movement_has_Category.delete().where(
        (Movement_has_Category.movement == movement_id) & (Movement_has_Category.category == tag_id)).execute()

    return "ok"


@app.route("/generateQRCode", methods=['POST'])
def generateQRCode():
    nu = Nubank()
    uuid, qr_code = nu.get_qr_code()
    image = qr_code.make_image(fill_color="black", back_color="white")
    image.save("static/image/qrcode.jpg")

    return jsonify({"uuid": uuid})


@app.route("/generateQRCode/<uuid>", methods=['POST'])
def sync(uuid):
    Importer(uuid)
    return "ok"


@app.route("/getMovementsByTags/<year>/<month>")
def getMovementsByTags(year, month):
    tags = Category.select().execute()
    data = {}
    for tag in tags:
        movements = Movement.select().join(Movement_has_Category).join(Category).where(
            (Category.id == tag.id) & (Movement.date.between(year + '-' + month + '-01', year + '-' + month + '-31'))
        )

        sum = 0
        for movement in movements:
            if movement.type == "OUTCOME":
                sum = sum + movement.value

        if sum:
            data[tag.name] = str(sum)

    return jsonify(data)


with open('config.yml', 'r') as f:
    doc = yaml.load(f)

app.run(debug=True, port=doc['port'])
