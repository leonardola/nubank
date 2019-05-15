from flask import Flask, request, jsonify
from flask import render_template
from Entity.Movement import Movement
from Entity.Category import Category
from Entity.Movement_has_Category import Movement_has_Category
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

app = Flask(__name__)


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
        totalOutcome=totalOutcome
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

    # tags = Category.select().where(Movement.id==movement_id).execute()
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


@app.route("/removeMovementTag/<movement_id>/<tag_id>", methods=['POST', 'GET'])
def removeMovementTag(movement_id, tag_id):
    Movement_has_Category.delete().where(
        (Movement_has_Category.movement == movement_id) & (Movement_has_Category.category == tag_id)).execute()

    return "ok"


app.run(debug=True)
