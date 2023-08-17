SELECT update_origin, count(*) as my_count
FROM darwin
group by update_origin
order by 2 desc
;