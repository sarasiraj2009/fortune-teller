CREATE DATABASE fdb;
use fdb;

CREATE TABLE fortune (
  colour VARCHAR(10),
  number INT(10),
  sentence_id INT(10)
);

INSERT INTO fortune
  (colour, number, sentence_id)
VALUES
  ('blue', '1', '1'),
  ('green', 'yellow', '2');
