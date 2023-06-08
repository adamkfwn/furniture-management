-- Create the database
CREATE DATABASE KEA_FM_location;

-- Switch to the newly created database
USE KEA_FM_location;

-- Create the hallway table
CREATE TABLE Hallway (
    hallway_id INT AUTO_INCREMENT PRIMARY KEY,
    hallway_name VARCHAR(5)
);

-- Create the Room table
CREATE TABLE Classroom (
    classroom_id INT AUTO_INCREMENT PRIMARY KEY,
    classroom_name VARCHAR(5)
);

-- 20 rows of data for the hallway table
INSERT INTO Hallway (hallway_name)
VALUES 
    ('H212'), ('H213'), ('H214'), ('H215'), ('H216'),
    ('H217'), ('H218'), ('H219'), ('H220'), ('H221'),
    ('H222'), ('H223'), ('H224'), ('H225'), ('H226'),
    ('H227'), ('H228'), ('H229'), ('H230'), ('H231'),
    ('H232');
    
-- 20 rows of data for the classroom table
INSERT INTO Classroom (classroom_name)
VALUES 
    ('E212'), ('E213'), ('E214'), ('E215'), ('E216'),
    ('E217'), ('E218'), ('E219'), ('E220'), ('E221'),
    ('E222'), ('E223'), ('E224'), ('E225'), ('E226'),
    ('E227'), ('E228'), ('E229'), ('E230'), ('E231'),
    ('E232');
