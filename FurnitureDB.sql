-- Create the database
CREATE DATABASE KEA_FM_furniture;

-- Switch to the newly created database
USE KEA_FM_furniture;

-- Create the Chair table
CREATE TABLE Chair (
    id INT AUTO_INCREMENT,
    name VARCHAR(50),
    PRIMARY KEY (id)
);

-- Insert 20 items into the Chair table
INSERT INTO Chair (name)
VALUES ('Chair 1'), ('Chair 2'), ('Chair 3'), ('Chair 4'), ('Chair 5'), 
       ('Chair 6'), ('Chair 7'), ('Chair 8'), ('Chair 9'), ('Chair 10'), 
       ('Chair 11'), ('Chair 12'), ('Chair 13'), ('Chair 14'), ('Chair 15'), 
       ('Chair 16'), ('Chair 17'), ('Chair 18'), ('Chair 19'), ('Chair 20');

-- Create the Desk table
CREATE TABLE Desk (
    id INT AUTO_INCREMENT,
    name VARCHAR(50),
    PRIMARY KEY (id)
);

-- Insert 20 items into the Desk table
INSERT INTO Desk (name)
VALUES ('Desk 1'), ('Desk 2'), ('Desk 3'), ('Desk 4'), ('Desk 5'), 
       ('Desk 6'), ('Desk 7'), ('Desk 8'), ('Desk 9'), ('Desk 10'), 
       ('Desk 11'), ('Desk 12'), ('Desk 13'), ('Desk 14'), ('Desk 15'), 
       ('Desk 16'), ('Desk 17'), ('Desk 18'), ('Desk 19'), ('Desk 20');

-- Create the Whiteboard table
CREATE TABLE Whiteboard (
    id INT AUTO_INCREMENT,
    name VARCHAR(50),
    PRIMARY KEY (id)
);

-- Insert 20 items into the Whiteboard table
INSERT INTO Whiteboard (name)
VALUES ('Whiteboard 1'), ('Whiteboard 2'), ('Whiteboard 3'), ('Whiteboard 4'), ('Whiteboard 5'), 
       ('Whiteboard 6'), ('Whiteboard 7'), ('Whiteboard 8'), ('Whiteboard 9'), ('Whiteboard 10'), 
       ('Whiteboard 11'), ('Whiteboard 12'), ('Whiteboard 13'), ('Whiteboard 14'), ('Whiteboard 15'), 
       ('Whiteboard 16'), ('Whiteboard 17'), ('Whiteboard 18'), ('Whiteboard 19'), ('Whiteboard 20');
