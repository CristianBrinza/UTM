<h4 align="center">FCIM UTM </h4>
<h1 align='center'> 


▒▐█▀▄░▒▐█▀█▄ </br>
▒▐█▀▀▄▒▐█▌▐█ </br>
▒▐█▄▄▀▒▐█▄█▀ 

</h1>
<h4 align="center">Technical University of Moldova  </h4>
<h4 align="center">FCIM   |   UTM   |   Spring 2022</h4>
<p align=center>                           
  <img align=center style="height: 50%;
  width: 50%; " src="https://utm.md/wp-content/uploads/2020/12/logo-sigla.png" />
</p>

</br><p align=right>  
p. Galcenco Boris
</p>
</br><p align=center>  
Chisinau 2022
</p>

</br></br>
<p align=right>  
c.AMS | FCIM UTM Spring 2022 | 104 | 21.09.2021
</p>

c. BD | Galcenco | 104 | 09.09.2022

-- Intro Database –
1. What is database purpose? – Store and manage data.
2. When did the Database concepts born? - Thousands of year ago, the Egyptians first ( store and preserve date, curve it into stone).
3. How the data gets generated? - We generate manual data, or automatically.
4. Who consumes the data? - Applications (software) or/and people.
5. What for is data being consumed? - Apps/Users
6. Databases are used to....  - apps ( efficiently store data and return it when requested)
7. What is DBMS? - Database Management Systems
8. What is the SQL? - Structured Query Language
9. What are the data use cases (1.. 2.. 3.. ) - directly and indirectly, 1) writing and executing queries against data in database, 2)executing searches, or submit/save button, generating a sequence statement to retrieve that date, 3)business/organizations
10. Which "hats" you wear when working with data? - backend dev, data analysis, scientist, engineer, data researcher
11. Since when the SQL is around here? (19..) – 1974





1. In what order do records appear when executing a SQL query without ORDER BY clause? - no particular order, in order they were added to database
2. What is the default order for ORDER BY clause? - ASC
3. Can fields which were not mentioned in the SELECT list be used in the ORDER BY clause? - Yes
4. Can fields which were not mentioned in the SELECT list be used in the ORDER BY clause? - Yes

5.     as in example, the "top" instruction shows only x mentioned enteties, the "with ties" allow to show more if some of them have the same data
6. Can WHERE clause be applied after ORDER BY clause?
No
7. Will "ID BETWEEN 10 AND 100" statement  return records with ID equal to 10 or 100?
Yes

8. Is filtering by text data case sensitive? E.g. WHERE Name = 'Ion'
Case insensitive
9. List the wildcards you've learned and explain their functionality
%	Represents zero or more characters	
_	Represents a single character	
[]	Represents any single character within the brackets	
^	Represents any character not in the brackets	
-	Represents any single character within the specified range	

10. What is the default masks for Date formats in MS SQL? (choose 2 out of 4)
'MM/DD/YYYY'

</br></br>

# Laboratory work #3 
<h2 align="center">(Functions in queries)</h2> 
<p align="center"> https://www.youtube.com/watch?v=Fm8od9L9HMg</p></br>

- Each and every function in MS SQL requires at least 1 parameter
<p align="center" style="color:#0066ff">False</p>

- What will be the correct version of get current date function call?
<p align="center" style="color:#0066ff">SELECT GETDATE()</p>

- Can a result of one function be used as a parameter of another function?
<p align="center" style="color:#0066ff">Yes</p>

<h2 align="center">(Text calculations)</h2> 
<p align="center">https://www.youtube.com/watch?v=HJKraiIoYPU</p></br>


- What is (are) the correct syntax of concatenate function in MS SQL?
<p align="center" style="color:#0066ff">
+ and 
CONCAT()</p>

- Do CAST() and CONVERT() functions behave similarly in MS SQL?
<p align="center" style="color:#0066ff">Yes
No</p>

- You have a table:

<div style="color:#505050">&nbsp;&nbsp;&nbsp;SELECT ActorName</br>
&nbsp;&nbsp;&nbsp;FROM (</br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SELECT 'Tom BigBoy Cruise' as ActorName</br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UNION</br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SELECT 'Dwayne Rock Johnson' as ActorName</br>
&nbsp;&nbsp;&nbsp;) A;</br>
</div></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Using substring() function instead of right() and left(), write a SQL query which will show the First Name and Last Name only in single field. As an answer please provide a complete SQL query (without any additional text)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;So in our case, expected output is:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tom Cruise</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dwayne Johnson</br>
<p align="center" style="color:#0066ff">-</p>
</br>
<h2 align="center">(Date Calculations)</h2> 
<p align="center">https://www.youtube.com/watch?v=Q2xhAafpRJo</p></br>


- Try it yourself in DB and answer: what will happen if you will wrongly specify less number of chars than required by date mask?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For example:</br>
      convert(char(8), SomeDateField, 103)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When 103 date style requires 10 symbols?
<p align="center" style="color:#0066ff">2008-06-01 00:00:00.000 --- > 01/06/20</p>


- Try it yourself in DB and answer: what will happen if you will specify more number of chars than required by date mask?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For example:
      convert(char(10), SomeDateField, 3)

When 3 date style requires 8 symbols?
*
Write a query to select a month from the RegistryDate field
*
Considering that we have the following field with a single row:

select CAST('2024-09-26 00:00:00.000' AS DATETIME) as FutureModifiedDate

- What will be the output of the following function call?

DATEDIFF(YY, FutureModifiedDate, GETDATE())
*
2
-2
</br></br>
# Laboratory work #4
 
<h2 align="center">(Group By and Having)</h2> 
<p align="center">https://www.youtube.com/watch?v=oWkvHodS9cA</p></br>

Which function does not belong to the same group as others?
*
MIN()
COUNT()
ROUND()
AVG()
Look at the query below. Is it a valid one?

SELECT GroupName, AVG(Mark), COUNT(*)
FROM Students
GROUP BY GroupName;
*
Yes
No
Look at the query below. Is it a valid one?

SELECT GroupName, AVG(Mark), COUNT(*)
FROM Students
ORDER BY GroupName
GROUP BY GroupName;
*
Yes
No
What is the difference between GROUP BY and GROUP BY WITH ROLLUP?
*
How behaves GROUP BY WIH ROLLUP if you are grouping by two or more fields?
*
What is the difference between WHERE and HAVING clauses?
*
Using Address and CustomerAddress tables from AdventureWorksLT2019 database, write a query that:

Calculates a count of records under  each separate [Address.CountryRegion] and [CustomerAddress.AddressType] fields combination. The query should not return row if the count is greater than 100. It should also take only the records with non-NULL values in [Address.AddressLine2] field.

Please provide the whole query as the answer
*
Captionless Image





</br></br>
# Laboratory work #4
 




Table HumanResources.Employee from AdventureWorks2019 database contains a field called LoginID. It is filled with the data using the pattern [db_name]\[username] as shown at the screenshot below.
Write a query which returns usernames only (data after "\" symbol) as shown at highlighted part of the screenshot


Please provide the whole query as the answer
<p align="center" style="color:#0066ff">
USE AdventureWorks2019
SELECT RIGHT(LoginID,len(LoginID)-CHARINDEX('\',LoginID )) AS LoginID FROM HumanResources.Employee
</p>
</br></br>
Check the content of Person.Person, Person.PersonPhone and Person.PhoneNumberType tables from  AdventureWorks2019 database.

Write a query that shows each person's First Name, Last Name, Phone Number, but only for the recors with "Employee" Person Type and "Work" Phone Type (please do not "hardcode" the phone type, use subquery or join instead)

Please provide the whole query as the answer
*
Prerequisite: run the following query in the AdventureWorks2019 database connection script:

delete from Person.EmailAddress where BusinessEntityID between 286 and 298;

Then using tables Person.Person and Person.EmailAddress write a query which will show all the fields from the Person table only for the entries which does not have an email set up in EmailAddress table.

Please provide the whole query as the answer
*
Prerequisite: run the following query in AdventureWorks2019 database :

Update HumanResources.JobCandidate set BusinessEntityID = 212 where jobCandidateId = 6;

Table HumanResources.JobCandidate contains info about candidates. Entries with non-NULL BusinessEntityID field already have an interviewer assigned - this BusinessEntityID represents interviewer's ID.

So, using the following tables:

HumanResources.JobCandidate
HumanResources.Employee
Person.Person
Person.PersonPhone
Person.PhoneNumberType

Write a query which returns info about all currently assigned  interviewers in JobCandidate table: their FirstName and LastName, and a PhoneNumber if the type of PhoneNumber is "Work"; if it's not "Work" - default Phone Number to '8-800-555-35-35'
Info about the same interviewer should appear only ONCE.

Please provide the whole query as the answer
*
Captionless Image
This excercise uses AdventureWorksLT2019 database, not AdventureWorks2019 - be careful

Write a query which will show all Customer FN/LN from table Customers and their respective Address ID's from table CustomerAddress. In case if there's more than one address for a particluar customer in the CustomerAddress table, choose the record with AddressType = 'Main Office'. Result dataset should contain only 1 row for each Customer.

Don't be shy to use subqueries.

Please provide the whole query as the answer 


<p align="center" style="color:#0066ff">False</p>
<p align="center" style="color:red">False</p>