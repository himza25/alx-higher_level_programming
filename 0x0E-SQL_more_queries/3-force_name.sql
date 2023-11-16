-- Create table with a mandatory 'name' column
-- Table: force_name
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
