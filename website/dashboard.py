from flask import Blueprint, render_template
from .models import ProgLang,Library,Tools,Education, Location
dashboard = Blueprint('dashboard',__name__)

@dashboard.route('/dashboard')  
def showDashboard():
    
    proLang_array = []
    ds_count = []
    proglang = getDataBaseValue(ProgLang)
    lib = getDataBaseValue(Library)
    # print(lib)
    tools = getDataBaseValue(Tools)
    edu = getDataBaseValue(Education)
    loc = getDataBaseValue(Location)
    return render_template("dashboard.html",proglang=proglang, lib=lib,tools=tools,edu=edu,loc=loc)

def getDataBaseValue(database_class):
    
    # print("Hey")
    labels=[]
    counts=[]
    ds_data = database_class.query.with_entities(database_class.Words, database_class.DS_count).filter(database_class.DS_count>1).order_by(database_class.DS_count.desc()).all()
    da_data = database_class.query.with_entities(database_class.Words, database_class.DA_count).filter(database_class.DA_count>1).order_by(database_class.DA_count.desc()).all()
    de_data = database_class.query.with_entities(database_class.Words, database_class.DE_count).filter(database_class.DE_count>1).order_by(database_class.DE_count.desc()).all()
    ml_data = database_class.query.with_entities(database_class.Words, database_class.ML_count).filter(database_class.ML_count>1).order_by(database_class.ML_count.desc()).all()
    datas = [ds_data,da_data,de_data,ml_data]
    
    for data in datas:
        label = list(map(lambda x:x[0], data))
        count = list(map(lambda x:x[1], data)) 
        total_sum = sum(count)
        percentage_count = list(map(lambda x:round(x/total_sum*100,1), count))
        # print(percentage_count)
        labels.append(label)
        counts.append(percentage_count)
    
    return [labels,counts]