CREATE TABLE users (
	id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(30)
);
INSERT INTO users (name) VALUES ("Tom");
CREATE TABLE cars (
	id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	user_id INT,
	model VARCHAR(20)
);
INSERT INTO cars (user_id, model) VALUES
(1, "Volvo"),
(1, "Mercedes");

