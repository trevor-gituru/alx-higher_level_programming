-- import in hbtn_0c_0 database this table dump
-- displays the max temperature of each state (ordered by State name)

SELECT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY state ORDER BY state;