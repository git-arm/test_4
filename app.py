from flask import Flask, render_template
app = Flask(__name__)

@app.route("/specific_energy", methods=["GET","POST"])
def sp_energy():
    try:
        db = mysql.connector.connect(user="python", password="Armatrics123$", host="192.168.0.108", database="jspl_wrm",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT SUM(energy) from jspl_wrm.bokaro_1 WHERE time_stamp BETWEEN %s AND %s"
        data_allday_yesterday = (yesterday_midnight.timestamp(), midnight.timestamp())
        data5_m = meter_id
        db_cursor.execute(stmt1,data_allday_yesterday)
        data8 = db_cursor.fetchall()
        db.commit()
        db.close()
        #b_values = pd.DataFrame(data8, columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency'])
        # print((y_values.T).iloc[:,0:].values)
        #b_val = ((b_values).values.tolist())
        # print((y_values.T).to_numpy())
        print(data8)
        #b_value_c = b_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(data8))
    response4.content_type = 'applicatopn/json'
    return response4


@app.route("/historic")
def historic():
    return render_template('historic.html')

@app.route("/")
def hello():
    return render_template('ems_test_v20.html')

if __name__ == "__main__":
    app.run()
