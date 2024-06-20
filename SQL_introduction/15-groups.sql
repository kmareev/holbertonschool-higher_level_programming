-- Lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Results should display: the score, number of records fr this score with the label number
-- The list should be sorted by the number of records (descending)

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER by score desc;