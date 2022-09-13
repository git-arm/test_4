import pandas as pd
import datetime
import numpy as np
import mysql.connector
import datetime
from flask import Flask, make_response, Response, json
from flask import Flask, render_template, jsonify, redirect, request
from datetime import datetime, time, timedelta
import json

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
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT voltage from bokaro_1 WHERE meterID = %s"
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
        db2 = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT time_stamp from bokaro_1 WHERE meterID = %s"
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
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT current from bokaro_1 WHERE meterID = %s"
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
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT frequency from bokaro_1 WHERE meterID = %s"
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
        db2 = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT total_harmonic_distortion from bokaro_1 WHERE meterID = %s"
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
        db2 = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT apparent_energy from bokaro_1 WHERE meterID = %s"
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
        db2 = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT power_factor from bokaro_1 WHERE meterID = %s"
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
        db2 = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT energy from bokaro_1 WHERE meterID = %s"
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
        db2 = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT power from bokaro_1 WHERE meterID = %s"
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
        db2 = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT apparent_power from bokaro_1 WHERE meterID = %s"
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
        db2 = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db2_cursor = db2.cursor()
        stmt2 = "SELECT location from bokaro_1_loc WHERE meterID = %s"
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


@app.route("/home", methods=["POST"])
def meter():
    global meter_id
    meter_id = [int(request.form.get("meter_id"))]
    print(meter_id)
    print(type(meter_id))



    try:
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT * from bokaro_1 "
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
    
    try:
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT SUM(energy) from bokaro_1 WHERE time_stamp BETWEEN %s AND %s"
        data_allday_yesterday = (yesterday_midnight.timestamp(), midnight.timestamp())
        data5_m = meter_id
        db_cursor.execute(stmt1, data_allday_yesterday)
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

    return render_template('ems_test_v21.html', data1=(b_val), data2=(data8))


@app.route("/getPlotCSV")
def getPlotCSV():
    try:
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT * from bokaro_1 WHERE meterID =%s "
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


#@app.route("/getpopup")
#def getpopup():
#    try:
#        db = mysql.connector.connect(user="python", password="Armatrics123$", host="192.168.0.108", database="jspl_wrm",
#                                     port="3306")
#        db_cursor = db.cursor()
#        stmt1 = "SELECT * from jspl_wrm.bokaro_1 "
#        data5_m = meter_id
#        db_cursor.execute(stmt1)
#        data6 = db_cursor.fetchall()
#        db.commit()
#        db.close()
#        b_values = pd.DataFrame(data6, columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency'])
        # print((y_values.T).iloc[:,0:].values)
#        b_val = ((b_values.T).values.tolist())
        # print((y_values.T).to_numpy())
        # print(y_val[0])
#        b_value_c = b_val[0][0]
#    except mysql.connector.Error as err:
#        print("Something went wrong: {}".format(err))
#    response3 = make_response(json.dumps(b_val))
#    response3.content_type = 'applicatopn/json'
#    return response3




@app.route("/getexcel")#, methods=["GET","POST"])
def getexcel():
    try:
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT * from bokaro_1 "
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
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT * from bokaro_1 "
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
        b_val_map = list(map(json.dumps, b_val))

        data0 = []
        for i in range(1, 2):
            for j in range(len(b_val)):
                data0.append(b_val[j][i])



        data1 = []                              #selecting the list elements
        for i in range(2, 3):
            for j in range(len(b_val)):
                data1.append(b_val[j][i])

        data2 = []
        for i in range(3, 4):
            for j in range(len(b_val)):
                data2.append(b_val[j][i])

        data3 = []
        for i in range(4, 5):
            for j in range(len(b_val)):
                data3.append(b_val[j][i])

        data4 = []
        for i in range(5, 6):
            for j in range(len(b_val)):
                data4.append(b_val[j][i])

        data5 = []
        for i in range(6, 7):
            for j in range(len(b_val)):
                data5.append(b_val[j][i])

        data6 = []
        for i in range(7, 8):
            for j in range(len(b_val)):
                data6.append(b_val[j][i])

        data7 = []
        for i in range(8, 9):
            for j in range(len(b_val)):
                data7.append(b_val[j][i])

        data8 = []
        for i in range(9, 10):
            for j in range(len(b_val)):
                data8.append(b_val[j][i])

        data9 = []
        for i in range(10, 11):
            for j in range(len(b_val)):
                data9.append(b_val[j][i])





    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response5 = make_response(json.dumps(b_val_map))
    response5.content_type = 'applicatopn/json'
    #return response4
    return render_template("historic.html", data=(b_val), data0=(data0), data1=(data1), data2=(data2), data3=(data3), data4=(data4), data5=(data5), data6=(data6), data7=(data7), data8=(data8), data9=(data9))

@app.route("/specific_energy", methods=["GET","POST"])
def sp_energy():
    try:
        db = mysql.connector.connect(user="longingoatmeal9", password="4Ubrtd88hgU5YsHCJ9Ls9Q", host="server491829892.mysql.database.azure.com", database="blsdatabase", port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT SUM(energy) from bokaro_1 WHERE time_stamp BETWEEN %s AND %s"
        data_allday_yesterday = (yesterday_midnight.timestamp(), midnight.timestamp())
        data5_m = meter_id
        db_cursor.execute(stmt1, data_allday_yesterday)
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
    return render_template('ems_test_v21.html', data1=(data8))


@app.route("/")
def index():
    data='Please select a meter from home page'
    return render_template('mapping.html', data0=(data))
    #return render_template('datasheet.html')


@app.route("/historic")
def historic():
    return render_template('historic.html')


if __name__ == "__main__":
    app.run(debug=TRUE)
