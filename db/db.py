import sqlite3
import pandas as pd 
import pprint
import platform

if platform.system()=='Linux':
    BASE_PATH = '/home/michael/Documents/Coding/recipe-builder/db/'
elif platform.system()=='Windows':
    BASE_PATH = 'C:\\Users\\mladouceur\\Python\\recipe-builder\\db\\'
DATABASE_FILE_PATH = f'{BASE_PATH}recipe-builder.db'
INGREDIENTS_TABLE = 'ingredients'

class DB:
    def __init__(self):
        self.db = DATABASE_FILE_PATH
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        self.create_ingredient_table()
        self.ingredient_names = self.return_all_names(INGREDIENTS_TABLE)

    def create_ingredient_table(self):
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {INGREDIENTS_TABLE}
                            (name TEXT,
                            category TEXT,
                            serving_quantity REAL,
                            serving_unit TEXT,
                            preferred_brand TEXT,
                            suggested_store TEXT,
                            calories REAL,
                            protein REAL,
                            fat REAL,
                            carbs REAL,
                            fiber REAL,
                            sugar REAL,
                            saturated_fat REAL,
                            monounsaturated_fat REAL,
                            polyunsaturated_fat REAL,
                            omega_3_fat REAL,
                            omega_6_fat REAL,
                            vitamin_a REAL,
                            vitamin_c REAL,
                            vitamin_d REAL,
                            vitamin_e REAL,
                            vitamin_k REAL,
                            vitamin_b6 REAL,
                            vitamin_b12 REAL,
                            thiamin REAL,
                            riboflavin REAL,
                            niacin REAL,
                            folate REAL,
                            pantothenic_acid REAL,
                            calcium REAL,
                            iron REAL,
                            magnesium REAL,
                            phosphorus REAL,
                            potassium REAL,
                            zinc REAL)''')
        self.conn.commit()

    def query_all_db(self,table):
        # self.conn.row_factory = self.dict_factory
        query = self.c.execute(f'SELECT * FROM {table}')
        colname = [d[0] for d in query.description]
        result = [dict(zip(colname,r)) for r in query.fetchall()]
        pprint.pprint(result)
        return result

    def query_by_name(self,table,name):
        query = self.c.execute(f'SELECT * FROM {table} WHERE (name=?)', (name,))
        colname = [d[0] for d in query.description]
        result = [dict(zip(colname,r)) for r in query.fetchall()]
        return result[0]

    def return_all_names(self,table):
        query = self.query_all_db(table)
        result = []
        for i in query:
            result.append(i['name'])
        return result

    def ingredient_to_db(self,data):
        self.c.execute(f'SELECT * FROM {INGREDIENTS_TABLE} WHERE (name=?)', (data['name'],))
        entry = self.c.fetchone()
        if entry is None:
            self.c.execute(f'''INSERT INTO {INGREDIENTS_TABLE} (name,
                                                                category,
                                                                serving_quantity,
                                                                serving_unit,
                                                                preferred_brand,
                                                                suggested_store,
                                                                calories,
                                                                protein,
                                                                fat,
                                                                carbs,
                                                                fiber,
                                                                sugar,
                                                                saturated_fat,
                                                                monounsaturated_fat,
                                                                polyunsaturated_fat,
                                                                omega_3_fat,
                                                                omega_6_fat,
                                                                vitamin_a,
                                                                vitamin_c,
                                                                vitamin_d,
                                                                vitamin_e,
                                                                vitamin_k,
                                                                vitamin_b6,
                                                                vitamin_b12,
                                                                thiamin,
                                                                riboflavin,
                                                                niacin,
                                                                folate,
                                                                pantothenic_acid,
                                                                calcium,
                                                                iron,
                                                                magnesium,
                                                                phosphorus,
                                                                potassium ,
                                                                zinc) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                (data['name'],
                data['category'],
                data['serving_quantity'],
                data['serving_unit'],
                data['preferred_brand'],
                data['suggested_store'],
                data['calories'],
                data['protein'],
                data['fat'],
                data['carbs'],
                data['fiber'],
                data['sugar'],
                data['saturated_fat'],
                data['monounsaturated_fat'],
                data['polyunsaturated_fat'],
                data['omega_3_fat'],
                data['omega_6_fat'],
                data['vitamin_a'],
                data['vitamin_c'],
                data['vitamin_d'],
                data['vitamin_e'],
                data['vitamin_k'],
                data['vitamin_b6'],
                data['vitamin_b12'],
                data['thiamin'],
                data['riboflavin'],
                data['niacin'],
                data['folate'],
                data['pantothenic_acid'],
                data['calcium'],
                data['iron'],
                data['magnesium'],
                data['phosphorus'],
                data['potassium'],
                data['zinc'],))
            self.conn.commit()
            print('Ingredient added')
        else:
            print(f'Ingredient exists: {entry}')