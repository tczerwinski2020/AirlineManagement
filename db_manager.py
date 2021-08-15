# Author: Taylor Czerwinski
# Summer 2021

import mysql.connector
from datetime import datetime

# Manages the local database db_airways
class DBManager:
    # Initializes first connection with the database
    def __init__(self):
        self._conn = mysql.connector.connect(host='localhost', user="root",
                                             password="April1499", database="db_airways")
        sql_command = "SELECT COUNT(*) FROM departure;"
        cursor = self._conn.cursor()
        # If database is empty, creates and initializes tables
        try :
            cursor.execute(sql_command)
            records = cursor.fetchone()[0]
            if records >= 1:
                print("Tables already initialized.")
                pass
            else:
                self.init_tables()
        except Exception as ex:
            print(ex)
            self.create_tables()
            self.init_tables()
            self.init_procedure()
        pass

    # Establishes connection with the database using mysql connector
    def open_connection(self):
        self._conn = mysql.connector.connect(host='localhost', user="root",
                                             password="April1499", database="db_airways")

    # Closes the connection
    def close_connection(self):
        self._conn.close()

    # Creates tables based on db_airways copy.sql file
    def create_tables(self):
        sql_file = "db_airways copy.sql"
        file = open(sql_file)
        sql = file.read()
        cursor = self._conn.cursor ()
        for  result  in  cursor.execute(sql , multi=True):
            if  result.with_rows:
                print(f"Rows  produced  by  statement  ’{result.statement}’:")
                print(result.fetchall ())
            else:
                print(f"Number  of rows  affected  by  statement  ’{result.statement}’: { result.rowcount}")

    # Loads data from file_name to a table in the database
    def load_data(self, table, file_name):
        cursor = self._conn.cursor()
        with open(file_name, 'r') as file:
                # First line is attribute names
            table_attributes = file.readline().strip().split(",")
            reader = file.readlines()
                # Adapts the number of '%s' that are needed for sql_command
            values_s = '%s,' * len(table_attributes)
            values_s = values_s[0:len(values_s) - 1]

            for row in reader:
                record = row.strip().replace("\"", "").replace("\t", "").split(",")
                print(record)
                sql_command = "INSERT INTO " + table + " (" + ",".join(
                    table_attributes) + ") VALUES (" + values_s + "); "
                cursor.execute(sql_command, record)
                self._conn.commit()

    # Loads flight's table data
    def insert_data_flight(self, table, file_name):
        cursor = self._conn.cursor()
        with open(file_name, 'r') as file:
                # First line is attribute names
            table_attributes = file.readline().strip().split(",")
            reader = file.readlines()
                # Adapts the number of '%s' that are needed for sql_command
            values_s = '%s,' * len(table_attributes)
            values_s = values_s[0:len(values_s) - 1]

            for row in reader:
                record = row.strip().replace("\"", "").replace("\t", "").split(",")
                record[3] = datetime.strptime(record[3], '%H:%M')
                record[4] = datetime.strptime(record[4], '%H:%M')
                print(record)
                sql_command = "INSERT INTO " + table + " (" + ",".join(
                    table_attributes) + ") VALUES (" + values_s + "); "
                cursor.execute(sql_command, record)
                self._conn.commit()

    # Loads departure data into table
    def insert_depart_data(self, table, file_name):
        cursor = self._conn.cursor()
        with open(file_name, 'r') as file:
            # First line is attribute names
            table_attributes = file.readline().strip().split(",")
            reader = file.readlines()

            # Adapts the number of '%s' that are needed for sql_command
            values_s = '%s,' * len(table_attributes)
            values_s = values_s[0:len(values_s) - 1]

            for row in reader:
                record = row.strip().split("\",")
                record = (record[0].replace("\"", "").strip(), record[1])
                datetime_obj = datetime.strptime(record[0], '%b %d,%Y')
                record = (datetime_obj, record[1])
                print(record)
                sql_command = "INSERT INTO " + table + " (" + ",".join(
                    table_attributes) + ") VALUES (" + values_s + "); "
                cursor.execute(sql_command, record)
                self._conn.commit()

    # Loads passenger bookings' data into table
    def insert_passenger_bookings(self, table, file_name):
        cursor = self._conn.cursor()
        with open(file_name, 'r') as file:
            # First line is attribute names
            table_attributes = file.readline().strip().split(",")

            reader = file.readlines()
            # Adapts the number of '%s' that are needed for sql_command
            values_s = '%s,' * len(table_attributes)
            values_s = values_s[0:len(values_s) - 1]

            for row in reader:
                record = row.strip().replace("\"", "").replace("\'", "").split(",")
                print(record)
                datetime_obj = datetime.strptime(record[1] + record[2], '%B %d %Y')
                record = (record[0], datetime_obj, record[3], record[4])
                print(record)
                sql_command = "INSERT INTO " + table + " (" + ",".join(
                    table_attributes) + ") VALUES (" + values_s + "); "
                cursor.execute(sql_command, record)
                self._conn.commit()

    # Loads employees_assigned data into table
    def insert_employees_assigned(self, table, file_name):
        cursor = self._conn.cursor()
        with open(file_name, 'r') as file:
            # First line is attribute names
            table_attributes = file.readline().strip().split(",")

            reader = file.readlines()
            # Adapts the number of '%s' that are needed for sql_command
            values_s = '%s,' * len(table_attributes)
            values_s = values_s[0:len(values_s) - 1]

            for row in reader:
                record = row.strip().replace("\"", "").replace("\'", "").split(",")

                datetime_obj = datetime.strptime(record[1] + record[2], '%B %d %Y')
                record = (record[0], datetime_obj, record[3])
                print(record)
                sql_command = "INSERT INTO " + table + " (" + ",".join(
                    table_attributes) + ") VALUES (" + values_s + "); "
                cursor.execute(sql_command, record)
                self._conn.commit()

    # Creates passenger table in database
    def add_passenger_table(self):
        cursor = self._conn.cursor()
        sql_command = """CREATE TABLE IF NOT EXISTS passenger
    (ticket_number VARCHAR(255),
    name VARCHAR(255),
    PRIMARY KEY (ticket_number),
    FOREIGN KEY (name) REFERENCES person(name)
    );"""
        cursor.execute(sql_command)
        print(cursor.fetchall())
        self._conn.commit()

    # Populates passenger table from passenger_bookings
    def populate_passenger(self):
        cursor = self._conn.cursor()
        sql_command = """INSERT INTO passenger
    (name, ticket_number)
    SELECT name, ticket_number
    FROM passenger_bookings;"""
        cursor.execute(sql_command)
        print(cursor.fetchall())
        self._conn.commit()

    # Initializes all tables in the database
    def init_tables(self):
        self.load_data('person', 'CSV_files/person copy.csv')
        self.load_data('employee', 'CSV_files/employee copy.csv')
        self.load_data('pilot', 'CSV_files/pilot copy.csv')
        self.load_data('plane', 'CSV_files/plane copy.csv')
        self.load_data('aircraft', 'CSV_files/aircraft copy.csv')
        self.insert_data_flight('flight', 'CSV_files/flight copy.csv')
        self.load_data('can_fly', 'CSV_files/can_fly copy.csv')

        self.insert_depart_data('departure', 'CSV_files/departure copy.csv')
        self.insert_passenger_bookings('passenger_bookings', 'CSV_files/passenger_bookings copy.csv')
        self.insert_employees_assigned('employees_assigned', 'CSV_files/employees_assigned copy.csv')
        self.add_passenger_table()
        self.populate_passenger()

    # Creates estimate_pilot_years procedure
    def init_procedure(self):
        self.open_connection()
        cursor = self._conn.cursor()
        sql_command = """
        CREATE PROCEDURE estimate_pilot_years (IN user_input_employee_no INT, OUT number_of_years_flown FLOAT)
        BEGIN 
        SELECT (flight_hours / (75 * 12)) INTO number_of_years_flown
        FROM pilot WHERE employee_no = user_input_employee_no;
        END
        """
        cursor.execute(sql_command)
        self.close_connection

    # Retrieves single record from passenger_bookings and flight based on a ticket number
    def search_by_ticket_number(self, ticket_number):
        bookings_record = self.get_bookings_info(ticket_number)
        if bookings_record is None:
            return
        flight_record = self.get_flight_info(bookings_record[2])
        final_record = (bookings_record, flight_record)
        return final_record

    # Retrieves a record from passenger_bookings based on a ticket number
    def get_bookings_info(self, ticket_number):
        self.open_connection()
        cursor = self._conn.cursor()
        cursor.execute("""SELECT * FROM passenger_bookings WHERE ticket_number LIKE \'%""" + ticket_number + """%\'""")
        row = cursor.fetchone()
        self.close_connection()
        return row

    # Retrieves a record from flight based on flight number
    def get_flight_info(self, flight_number):
        self.open_connection()
        cursor = self._conn.cursor()
        cursor.execute("""SELECT * FROM flight WHERE flight_number LIKE \'%""" + str(flight_number) + """%\'""")
        row = cursor.fetchone()
        self.close_connection()
        return row

    # Retrieves all employees_assigned for a specific flight number
    def get_employees_assigned(self, flight_number):
        self.open_connection()
        cursor = self._conn.cursor()
        cursor.execute("""SELECT * FROM employees_assigned WHERE flight_number LIKE \'%""" + str(flight_number)+ """%\'""")
        rows = cursor.fetchall()
        date = rows[0][1]
        employees = []
        for row in rows:
            if row[1] == date:
                employees.append(row)
        self.close_connection()
        return employees

    # Retrieves employee name based on employee number
    def get_employee_name(self, employee_no):
        self.open_connection()
        cursor = self._conn.cursor()
        cursor.execute("""SELECT name FROM employee WHERE employee_no LIKE \'%""" + str(employee_no) + """%\'""")
        name = cursor.fetchone()
        self.close_connection()
        self.invoke_proc(employee_no)
        return name

    # Retrieves passengers records based on flight number and departure date
    def get_passengers(self, flight_number, depart_date):
        self.open_connection()
        cursor = self._conn.cursor()
        cursor.execute("""SELECT name, ticket_number FROM passenger_bookings WHERE flight_number LIKE \'%""" + str(flight_number)+ """%\' 
        AND departure_date LIKE \'%""" + str(depart_date)+ """%\'""")
        passengers = cursor.fetchall()
        self.close_connection()
        return passengers

    # Returns flight numbers for a single departure date
    def get_flight_numbers(self, departure_date):
        self.open_connection()
        cursor = self._conn.cursor()
        sql_command = ("""SELECT flight_number FROM departure WHERE departure_date LIKE \'%""" + departure_date.toString("yyyy-MM-dd") + """%\'""")
        cursor.execute(sql_command)
        rows = cursor.fetchall()
        self.close_connection()
        return rows

    # Invokes the procedure estimate_pilot_years based on an employee number
    def invoke_proc(self, employee_number):
        self.open_connection()
        cursor = self._conn.cursor()
        args = [employee_number, 0]
        hours = cursor.callproc("estimate_pilot_years", args)
        return hours

    # Retrieves single record from employee based on employee number
    def get_employee_stat(self, employee_number):
        self.open_connection()
        cursor = self._conn.cursor()
        sql_command = """SELECT * FROM employee WHERE employee_no LIKE \'%""" + str(employee_number) + """%\'"""
        cursor.execute(sql_command)
        employ = cursor.fetchone()
        self.close_connection()
        return employ

    # Retrieves all flights a specific employee is assigned based on their employee number
    def work_flights(self, employee_no):
        self.open_connection()
        cursor = self._conn.cursor()
        sql_command = """SELECT * FROM employees_assigned WHERE employee_no LIKE \'%""" + employee_no + """%\'"""
        cursor.execute(sql_command)
        flight_info = cursor.fetchall()
        self.close_connection()
        return flight_info