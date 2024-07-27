from flask import Flask
from models import db, Vala, Troop, Campaign
app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:123450@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#@app.route()
#def hello_world():
#    return 'Hello world! CARAJO!!!!!!!'

@app.route('/', methods=['GET'])
def get_Valar():
    try:
        #Trigo la info de los Valar
        valar = Vala.query.all()
        valarData = []
        for vala in valar:
            valaData = {
                'id': vala.id,
                'name': vala.description,
            }
            valarData.append(valaData)
        
        #Traigo la info de las Tropas
        Troops = Troop.query.all()
        TroopsData = []
        for troop in Troops:
            TroopData = {
                'id': troop.id,
                'name': troop.name,
                'description': troop.description,
                'combatPower': troop.combatPower,
                'consumption': troop.consumption,
            }
            TroopsData.append(TroopData)
        
        #Muestro la info por consola
        print(valarData)     
        print(TroopsData)   
        return 'COOL'
    except Exception as error:
        print('Error', error)
        return 'Error', 500

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()  
    app.run(host='0.0.0.0', debug=True, port=port)