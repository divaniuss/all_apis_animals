CREATE DATABASE db_for_test_app;
USE db_for_test_app;

CREATE TABLE [Users]
(
    [ID] INT IDENTITY,
	[Time_log] VARCHAR(50),
	[Name] VARCHAR(50) NOT NULL,
    [login] VARCHAR(50) NOT NULL UNIQUE,
    [Password] VARCHAR(255) NOT NULL,
);



CREATE TABLE [Logs] (
    [ID] INT IDENTITY PRIMARY KEY,
    [User] VARCHAR(255) NOT NULL,
    [Test] VARCHAR(255) NOT NULL,
    [Answers] VARCHAR(50) NOT NULL,
	[Time_log] VARCHAR(255),
);

