import json
import mysql.connector

connection = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="nb_db"
)
cursor = connection.cursor()


def create_and_add_json():
    brand = input('Insert Brand: ')
    model = input('Insert Model: ')
    country = input('Insert Country: ')

    global cursor
    cars_add = "INSERT INTO cars (Brand, Model, Country)" \
               "VALUES (%s, %s, %s)"
    values = (brand, model, country)
    cursor.execute(cars_add, values)
    connection.commit()

    try:
        add_car = {
            "Brand": brand,
            "Model": model,
            "Country": country
        }

        with open('car_info.json', 'r+') as file:
            file_data = json.load(file)
            file_data.append(add_car)
            file.seek(0)
            json.dump(file_data, file, indent=2)

    except FileNotFoundError:
        with open('car_info.json', 'w') as car_info:
            add_car_info = [{'Brand': brand, 'Model': model, 'Country': country}]

            json.dump(add_car_info, car_info, indent=2)
            print('File Not Found and Create New JSON and Database')


create_and_add_json()
