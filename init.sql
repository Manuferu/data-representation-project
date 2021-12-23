use datarepresentation;

create table student(
    ID_number int PRIMARY KEY,
    Subjects int,
    Name varchar(250),
    Age int,
    Marks int
);
create table Subjects(
    Subjects_ID int PRIMARY KEY,
    Subjects_Name varchar(250),
    Teacher_name varchar(250),
    OnLeavingCert int
)

create table cars(
    id INT AUTO_INCREMENT PRIMARY KEY,
    plate VARCHAR(250),
    model VARCHAR(250),
    year INT,
    fuel VARCHAR(250)
);
id INT AUTO_INCREMENT PRIMARY KEY, model VARCHAR(250), year INT, fuel VARCHAR(250)