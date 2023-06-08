-- Create the database
CREATE DATABASE KEA_FM_sensors;

-- Switch to the newly created database
USE KEA_FM_sensors;

-- Create the Sensor table
CREATE TABLE Sensor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_name VARCHAR(50),
);

-- Insert sensor names into Sensor_Name column within Sensor table
INSERT INTO Sensor (sensor_name)
VALUES     
	('S212'), ('S213'), ('S214'), ('S215'), ('S216'),
    ('S217'), ('S218'), ('S219'), ('S220'), ('S221'),
    ('S222'), ('S223'), ('S224'), ('S225'), ('S226'),
    ('S227'), ('S228'), ('S229'), ('S230'), ('S231'),
    ('S232');
