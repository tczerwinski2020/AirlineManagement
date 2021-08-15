create database if not exists db_airways;
use db_airways;

CREATE TABLE IF NOT EXISTS `person` (
  `name` varchar(255) PRIMARY KEY,
  `address` varchar(255),
  `phone` varchar(255)
);

CREATE TABLE IF NOT EXISTS `employee` (
  `employee_no` INT PRIMARY KEY,
  `name` varchar(255),
  `salary` numeric(12,2),
    FOREIGN KEY (name) REFERENCES person (name)
);

CREATE TABLE IF NOT EXISTS `pilot` (
  `employee_no` INT PRIMARY KEY,
  `flight_hours` numeric(12,3),
  FOREIGN KEY (employee_no) REFERENCES employee (employee_no)
);

CREATE TABLE IF NOT EXISTS `plane` (
  `maker` varchar(255),
  `model_number` varchar(255) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS `aircraft` (
  `serial_number` INT,
  `model_number` varchar(255),
    PRIMARY KEY (serial_number, model_number),
    FOREIGN KEY (model_number) REFERENCES plane (model_number)
);

CREATE TABLE IF NOT EXISTS `flight` (
    `flight_number` INT PRIMARY KEY,
    `origin` VARCHAR(255),
    `destination` VARCHAR(255),
    `departure_time` DATETIME,
    `arrival_time` DATETIME,
    `status` VARCHAR(255)
 );

CREATE TABLE IF NOT EXISTS `departure` (
    `departure_date` DATETIME,
    `flight_number` INT,
    PRIMARY KEY (departure_date, flight_number),
    FOREIGN KEY (flight_number) REFERENCES flight(flight_number)
 );

CREATE TABLE IF NOT EXISTS `passenger_bookings` (
    `name` VARCHAR(255),
    `departure_date` DATETIME,
    `flight_number` INT,
    `ticket_number` VARCHAR(255),
    PRIMARY KEY (departure_date, flight_number, ticket_number),
    FOREIGN KEY (name) REFERENCES person (name),
    FOREIGN KEY (departure_date) REFERENCES departure (departure_date),
    FOREIGN KEY (flight_number) REFERENCES flight(flight_number)
 );

 CREATE TABLE IF NOT EXISTS `employees_assigned` (
     `employee_no` INT,
     `departure_date` DATETIME,
     `flight_number` INT,
     PRIMARY KEY (employee_no, departure_date, flight_number),
     FOREIGN KEY (employee_no) REFERENCES employee(employee_no),
     FOREIGN KEY (departure_date) REFERENCES departure (departure_date),
     FOREIGN KEY (flight_number) REFERENCES flight(flight_number)
 );

 CREATE TABLE IF NOT EXISTS `can_fly` (
     `employee_no` INT,
     `model_number` VARCHAR(255),
     PRIMARY KEY (employee_no, model_number),
     FOREIGN KEY (employee_no) REFERENCES employee(employee_no),
     FOREIGN KEY (model_number) REFERENCES plane(model_number)
  );
