#1
select SNUM,SNAME,CITY,COMM from salespeople;
#2
select distinct SNUM from orders;
#3
select SNAME,COMM from salespeople where CITY = 'Londan';
#4
select CNAME from cust where RATING = 100;
#5
select ONUM,AMT,ODATE from orders;
#6
select CNAME from cust where RATING>200;
#7
select CNAME from cust where CITY='San Jose' or RATING>200;
#8
select AMT from orders where AMT>1000;
#9
select SNAME,CITY FROM salespeople where CITY='London' and
COMM>=0.10;
#10
select CNAME from cust where RATING<=100 and CITY='Rome';
#11
select SNAME from salespeople where COMM between 0.10 and 0.12;
#12
select CNAME FROM cust where CITY=null;
#13
select SNUM,ODATE from orders where ODATE in('03-OCT-1994',
'04-OCT-1994');
#14
select * from cust where CNAME like 'A%' or CNAME like 'B%';
#15
select ONUM from orders where AMT <> 0 and AMT is not  null;
#16
select count(distinct SNUM) as count FROM orders;

select SNUM,max(AMT) AS max from orders 
group by SNUM,ODATE  ORDER BY ODATE,SNUM;
#17
select SNUM,MAX(AMT) as max  FROM orders where AMT>=3000
group by SNUM,AMT
order by SNUM,AMT;
#18
select count(*) from orders where ODATE='3-OCT-1994';
#19
select onum, snum, amt, amt * 0.12 from orders order by snum;
#20
Select 'For the city (' || city || '), the highest rating is : (' ||  max(rating) || ')' from cust group by city;
#21
Select odate, count(onum) from orders group by odate order by count(onum); 
#22
Select sname, cname from salespeople, cust where salespeople.city = cust.city; 
#23
Select cname, sname from cust, salespeople where 
cust.snum = salespeople.snum 
#24
select onum,cname from orders,cust where orders.cnum=cust.cnum;
#25
Select cname, sname, comm from cust, salespeople
where comm > 0.12 and cust.snum = salespeople.snum; 
#26
Select sname, amt * comm from orders, cust, salespeople
where rating > 100 and salespeople.snum = cust.snum and 
salespeople.snum = orders.snum and cust.cnum = orders.cnum ;
#27
select avg(comm) from salespeople where city = ‘London’; 
#28
Select snum, cnum  from orders 
where cnum in (select cnum  from cust where city = 'London'); 
#29
Select cnum, cname from cust where
cnum >( select snum+1000  from salespeople where sname = 'Serres');
#30
Select cnum, rating from cust
 where rating > ( select avg(rating)  from cust where city = 'San Jose'); 


