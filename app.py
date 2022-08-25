import pandas as pd
import datetime
import numpy as np
import mysql.connector
import time
import select
import json
import datetime
from flask import Flask, make_response, Response
from flask import Flask, render_template, jsonify, redirect, request
from datetime import datetime, time, timedelta
import csv

meter_id = [1]


# calculate the previous all day timestamp
midnight = datetime.combine(datetime.today(), time.min)
yesterday_midnight = midnight - timedelta(days=1)
#print(f"from {yesterday_midnight.timestamp()}......to {midnight.timestamp()}")


app = Flask(__name__)


@app.route('/data', methods =["GET", "POST"])
def data():
    global meter_id
    try:
        db = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT voltage from sql6514334.bokaro_1 WHERE meter_id = %s"
        data1 = meter_id
        db_cursor.execute(stmt1,data1)
        data1 = db_cursor.fetchall()
        db.commit()
        db.close()
        y_values = pd.DataFrame(data1)
        #print((y_values.T).iloc[:,0:].values)
        y_val = ((y_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(y_val[0])
        y_value = y_val[0][0]
        #print(y_value)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db2 = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT time_stamp from sql6514334.bokaro_1 WHERE meter_id = %s"
        data2_m = meter_id
        db2_cursor.execute(stmt2,data2_m)
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data2)
        #print((y_values.T).iloc[:,0:].values)
        x_val = ((x_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(x_val[0])
        x_value = x_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT current from sql6514334.bokaro_1 WHERE meter_id = %s"
        data3_m = meter_id
        db_cursor.execute(stmt1,data3_m)
        data3 = db_cursor.fetchall()
        db.commit()
        db.close()
        z_values = pd.DataFrame(data3)
        #print((y_values.T).iloc[:,0:].values)
        z_val = ((z_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(y_val[0])
        z_value_c = z_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT frequency from sql6514334.bokaro_1 WHERE meter_id = %s"
        data4_m = meter_id
        db_cursor.execute(stmt1,data4_m)
        data4 = db_cursor.fetchall()
        db.commit()
        db.close()
        a_values = pd.DataFrame(data4)
        #print((y_values.T).iloc[:,0:].values)
        a_val = ((a_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(y_val[0])
        a_value_c = a_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db2 = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT total_harmonic_distortion from sql6514334.bokaro_1 WHERE meter_id = %s"
        data2_m = meter_id
        db2_cursor.execute(stmt2,data2_m)
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data2)
        #print((y_values.T).iloc[:,0:].values)
        x_val = ((x_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(x_val[0])
        x_value_t = x_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT apparent_energy from sql6514334.bokaro_1 WHERE meter_id = %s"
        data2_m = meter_id
        db2_cursor.execute(stmt2,data2_m)
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data2)
        #print((y_values.T).iloc[:,0:].values)
        x_val = ((x_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(x_val[0])
        x_value_appen = x_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT power_factor from sql6514334.bokaro_1 WHERE meter_id = %s"
        data2_m = meter_id
        db2_cursor.execute(stmt2,data2_m)
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data2)
        #print((y_values.T).iloc[:,0:].values)
        x_val = ((x_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(x_val[0])
        x_value_pf = x_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT energy from sql6514334.bokaro_1 WHERE meter_id = %s"
        data2_m = meter_id
        db2_cursor.execute(stmt2,data2_m)
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data2)
        #print((y_values.T).iloc[:,0:].values)
        x_val = ((x_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(x_val[0])
        x_value_en = x_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT power from sql6514334.bokaro_1 WHERE meter_id = %s"
        data2_m = meter_id
        db2_cursor.execute(stmt2,data2_m)
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data2)
        #print((y_values.T).iloc[:,0:].values)
        x_val = ((x_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(x_val[0])
        x_value_pwr = x_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT apparent_power from sql6514334.bokaro_1 WHERE meter_id = %s"
        data2_m = meter_id
        db2_cursor.execute(stmt2,data2_m)
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data2)
        #print((y_values.T).iloc[:,0:].values)
        x_val = ((x_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(x_val[0])
        x_value_apppwr = x_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT location from sql6514334.bokaro_1_loc WHERE meter_id = %s"
        data2_m = meter_id
        db2_cursor.execute(stmt2,data2_m)
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data2)
        #print((y_values.T).iloc[:,0:].values)
        x_val = ((x_values.T).values.tolist())
        #print((y_values.T).to_numpy())
        #print(x_val[0])
        x_value_loc= x_val[0][0]
        #print(f"location{x_value_loc}, type{type(x_value_loc)}")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    meter_info = int(meter_id[0])
    #print(type(meter_info))
    data = [x_value, y_value, z_value_c, a_value_c, meter_info, x_value_t, x_value_appen, x_value_pf, x_value_en, x_value_pwr, x_value_apppwr, x_value_loc ]
    response1 = make_response(json.dumps(data))
    response1.content_type = 'applicatopn/json'
    return response1


@app.route("/", methods=["POST"])
def meter():
    global meter_id
    meter_id = [int(request.form.get("meter_id"))]
    print(meter_id)
    print(type(meter_id))
    return render_template('ems_test_v20.html')


@app.route("/getPlotCSV")
def getPlotCSV():
    try:
        db = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT * from sql6514334.bokaro_1 WHERE meter_id =%s "
        data5_m = meter_id
        db_cursor.execute(stmt1, data5_m)
        data5 = db_cursor.fetchall()
        db.commit()
        db.close()
        b_values = pd.DataFrame(data5, columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency',
                                                'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                                'energy', 'power', 'apparent_power'])
        # print((y_values.T).iloc[:,0:].values)
        b_val = ((b_values.T).values.tolist())
        # print((y_values.T).to_numpy())
        # print(y_val[0])
        b_value_c = b_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    #data_to_dwnld = pd.DataFrame(b_val)
    #response_csv = data_to_dwnld.to_csv("data_snap.csv")
   # return response_csv
    #a = random()
#    b = random()
#    print(b_val)
    sensor_data_frame = pd.DataFrame(b_val)
#    df_w = pd.DataFrame(sensor_dataframe, columns=["a", "b"])
#    sensor_data_frame.to_csv("data_snap.csv", index=False)
#    print(type(sensor_data_frame))
#    data will be called from sql database
#    print(b_val)
    csv = b_values.to_string(columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency',
                                                'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                                'energy', 'power', 'apparent_power'], header = 'false',index = 'false' )
#    print(csv)
#    csv = ' '.join(map(str, b_values))
    #print(sensor_data_frame)
    return Response(
        b_values.to_csv(index=False),
        mimetype="text/csv",
        headers={"Content-disposition":
                "attachment; filename = BSL_EMS_meterdata.csv"})


@app.route("/getexcel")#, methods=["GET","POST"])
def getexcel():
    try:
        db = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT * from sql6514334.bokaro_1 "
        data5_m = meter_id
        db_cursor.execute(stmt1)
        data7 = db_cursor.fetchall()
        db.commit()
        db.close()
        b_values = pd.DataFrame(data7, columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency',
                                                'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                                'energy', 'power', 'apparent_power'])
        # print((y_values.T).iloc[:,0:].values)
        b_val = ((b_values).values.tolist())
        # print((y_values.T).to_numpy())
        # print(y_val[0])
        b_value_c = b_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(b_val))
    response4.content_type = 'applicatopn/json'
    #return response4
    return render_template("datasheet.html", data=(b_val))


@app.route("/historical", methods=["POST"])
def historical():
    try:
        db = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT * from sql6514334.bokaro_1 "
        data5_m = meter_id
        db_cursor.execute(stmt1)
        data8 = db_cursor.fetchall()
        db.commit()
        db.close()
        b_values = pd.DataFrame(data8, columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency',
                                                'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                                'energy', 'power', 'apparent_power'])
        # print((y_values.T).iloc[:,0:].values)
        b_val = ((b_values).values.tolist())
        # print((y_values.T).to_numpy())
        # print(y_val[0])
        b_value_c = b_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response5 = make_response(json.dumps(b_val))
    response5.content_type = 'applicatopn/json'
    #return response4
    return render_template("historic.html", data=(b_val))

@app.route("/specific_energy", methods=["GET","POST"])
def sp_energy():
    try:
        db = mysql.connector.connect(user="sql6514334", password="U2m8kZqyVm", host="sql6.freesqldatabase.com", database="sql6514334",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT SUM(energy) from sql6514334.bokaro_1 WHERE time_stamp BETWEEN %s AND %s"
        data_allday_yesterday = (yesterday_midnight.timestamp(), midnight.timestamp())
        data5_m = meter_id
        db_cursor.execute(stmt1,data_allday_yesterday)
        data8 = db_cursor.fetchall()
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(data8))
    response4.content_type = 'applicatopn/json'
    return render_template('ems_test_v20.html', data=data8)


@app.route("/")
def index():
    return render_template('ems_test_v20.html')
    


@app.route("/historic")
def historic():
    return render_template('historic.html')


if __name__ == "__main__":
    app.run()
