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


---

-- Intro Database –

|  <div style="width:290px">Questions</div>      | Answers |
| -------------  | --- |
|1. What is database purpose? | Store and manage data.|
|2. When did the Database concepts born? | Thousands of year ago, the Egyptians first ( store and preserve date, curve it into stone).|
|3. How the data gets generated? | We generate manual data, or automatically.|
|4. Who consumes the data? | Applications (software) or/and people.
|5. What for is data being consumed? | Apps/Users|
|6. Databases are used to....  | apps ( efficiently store data and return it when requested)|
|7. What is DBMS? | Database Management Systems|
|8. What is the SQL? | Structured Query Language|
|9. What are the data use cases (1.. 2.. 3.. ) | directly and indirectly, 1) writing and executing queries against data in database, 2)executing searches, or submit/save button, generating a sequence statement to retrieve that date, 3)business/organizations|
|10. Which "hats" you wear when working with data? | backend dev, data analysis, scientist, engineer, data researcher|
|11. Since when the SQL is around here? (19..) | 1974|



|  <div style="width:290px">Questions</div>      | Answers |
| -------------  | --- |
|1. In what order do records appear when executing a SQL query without ORDER BY clause? | no particular order, in order they were added to database
|2. What is the default order for ORDER BY clause? | ASC
|3. Can fields which were not mentioned in the SELECT list be used in the ORDER BY clause? | Yes
|4. Can fields which were not mentioned in the SELECT list be used in the ORDER BY clause? | Yes
|5.as in example, the "top" instruction shows only x mentioned enteties, the "with ties" allow to show more if some of them have the same data|
|6. Can WHERE clause be applied after ORDER BY clause?| No
|7. Will "ID BETWEEN 10 AND 100" statement  return records with ID equal to 10 or 100? | Yes
|8. Is filtering by text data case sensitive? E.g. WHERE Name = 'Ion' |Case insensitive
|9. List the wildcards you've learned and explain their functionality | [ % ]	Represents zero or more characters	</br>[ _ ]	Represents a single character	</br>[ [] ]	Represents any single character within the brackets	</br>[ ^ ]	Represents any character not in the brackets</br> [ - ]	Represents any single character within the specified range	
|10. What is the default masks for Date formats in MS SQL? (choose 2 out of 4) |'MM/DD/YYYY'


</br></br>

# Laboratory work #3 
<h2 align="center">(Functions in queries)</h2> 
<p align="center"> https://www.youtube.com/watch?v=Fm8od9L9HMg</p></br>

|  <div style="width:290px">Questions</div>      | Answers |
| -------------  | --- |
| Each and every function in MS SQL requires at least 1 parameter |False
| What will be the correct version of get current date function call? | SELECT GETDATE()
|Can a result of one function be used as a parameter of another function? | Yes

<h2 align="center">(Text calculations)</h2> 
<p align="center">https://www.youtube.com/watch?v=HJKraiIoYPU</p></br>

|  <div style="width:290px">Questions</div>      | Answers |
| -------------  | --- |
|What is (are) the correct syntax of concatenate function in MS SQL? | [+] and [CONCAT()]
|Do CAST() and CONVERT() functions behave similarly in MS SQL? | (not answered)variants: Yes/No
|You have a table: </br>
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

<table style='width:100%'>
  <tr>
    <th style="width:40%">Questions</th>
    <th>Answers</th>
    
  </tr>
  <tr>
  <td>Which function does not belong to the same group as others?
</td>
  <td>
  ROUND()
</td>
  </tr>
  <tr>
  <td>Look at the query below. Is it a valid one?

```sql
SELECT GroupName, AVG(Mark), COUNT(*)
FROM Students
GROUP BY GroupName;
```

</td>
  <td>Yes</td>
  </tr>
  <tr>
  <td>Look at the query below. Is it a valid one?

```sql
SELECT GroupName,  AVG(Mark), COUNT(*)
FROM Students
ORDER BY GroupName
GROUP BY GroupName;
```
</td>
  <td>Yes</td>
  </tr>
  <tr>
  <td>What is the difference between GROUP BY and GROUP BY WITH ROLLUP?
</td>
  <td>GROUP BY is used to group rows in a result set by one or more columns. It returns one row for each group of rows that have the same values in the specified columns.
<br><br>
GROUP BY WITH ROLLUP is an extension of the GROUP BY clause that generates a result set that is similar to that generated by a standard GROUP BY clause, but with additional rows that represent subtotals and grand totals. The rollup operation creates extra rows in the result set that represent subtotals, and grand totals for the groups of rows in the query.</td>
  </tr>
  <tr>
  <td>How behaves GROUP BY WIH ROLLUP if you are grouping by two or more fields?</td>
  <td>When using GROUP BY with ROLLUP and grouping by two or more fields, the result set will include a separate row for each combination of field values, as well as additional rows that show subtotals and grand totals for each field and combination of fields. For example, if you are grouping by fields A and B, you will see separate rows for each unique combination of A and B values, as well as subtotals for each value of A and a grand total for all rows.</td>
  </tr>
  <tr>
  <td>What is the difference between WHERE and HAVING clauses?</td>
  <td>The WHERE clause is used to filter rows before the result set is grouped and aggregated, while the HAVING clause is used to filter rows after the result set is grouped and aggregated. In other words, the WHERE clause is used to filter individual rows based on certain conditions, while the HAVING clause is used to filter groups of rows based on aggregate values.</td>
  </tr>
  <tr>
  <td>Using<b> Address</b> and<b> CustomerAddress</b> tables from<b> AdventureWorksLT2019</b> database, write a query that:
<br><br>
Calculates a count of records under  each separate [Address.CountryRegion] and [CustomerAddress.AddressType] fields combination. The query should not return row if the count is greater than 100. It should also take only the records with non-NULL values in [Address.AddressLine2] field.

Please provide the whole query as the answer</td>
  <td>

```sql
WITH CTE AS 
(
SELECT A.CountryRegion, CA.AddressType, COUNT(*) as Count
FROM AdventureWorksLT2019.SalesLT.Address A
JOIN AdventureWorksLT2019.SalesLT.CustomerAddress CA 
ON A.AddressID = CA.AddressID
WHERE A.AddressLine2 IS NOT NULL
GROUP BY A.CountryRegion, CA.AddressType
)

SELECT * FROM CTE
WHERE Count <= 100
```

</td>
  </tr>
 
  </table>


<h2 align="center">(Subqueries)</h2> 
<p align="center">https://www.youtube.com/watch?v=5KXbdkv9hEM</p></br>


<table style='width:100%'>
  <tr>
    <th style="width:40%">Questions</th>
    <th>Answers</th>
    
  </tr>
  <tr>
  <td>in sql Where subqueries can be used?
</td>
  <td>In both SELECT and WHERE</td>
  <tr>
   <tr>
  <td>Using<b> AdventureWorksLT2019</b> database, write a query that returns all the records from SalesOrderDetail table which have OrderQty equal to or less than the average value of OrderQty from the same table.
<br><br>
Please provide the whole query as the answer</td>
  <td>

```sql
WITH avgOrderQty AS (
    SELECT AVG(OrderQty) as avgQty
    FROM SalesOrderDetail
)
SELECT * 
FROM SalesOrderDetail 
WHERE OrderQty <= (SELECT avgQty FROM avgOrderQty);
```
</td>
  <tr>
   <tr>
  <td>Using AdventureWorksLT2019 database, write a query that returns all the records from Address table which have the same City value as the record with AddressID = 451
<br><br>
Please provide the whole query as the answer</td>
  <td>

```sql
SELECT * FROM Address
WHERE City = (SELECT City FROM Address WHERE AddressID = 451)
```

</td>
  <tr>
   <tr>
  <td>In AdventureWorksLT2019 database, write a script using subqueries which:
<br><br>
Takes all the records from SalesOrderDetail table with unitPrice between 1000 and 2000,
and using their ProductID returns records for the same ProductID but which are for the unitPrice < 1000
<br><br>
Please provide the whole query as the answer</td>
  <td>

```sql
SELECT * 
FROM SalesOrderDetail 
WHERE ProductID IN (
    SELECT ProductID 
    FROM SalesOrderDetail 
    WHERE UnitPrice BETWEEN 1000 AND 2000
) 
AND UnitPrice < 1000

```
</td>
  
  </table>

  <h2 align="center">(Correlated Subqueries)</h2> 
<p align="center">https://www.youtube.com/watch?v=0ETfzlAQqBQ</p></br>


<table style='width:100%'>
  <tr>
    <th style="width:40%">Questions</th>
    <th>Answers</th>
    
  </tr>
  <tr>
  <td>What is mandatory for correlated subquery?
</td>
  <td>Both</td>
  <tr>
   <tr>
  <td>In AdventureWorksLT2019 database, write a script using subqueries which:
<br><br>
Returns records with highest CustomerID from Customer table for each CompanyName.
<br><br>
For example ,there are two records CompanyName = 'A Great Bicycle Company'
So, for this compane only record with CustomerID = 29872 should be returned.
<br><br>
Please provide the whole query as the answer
</td>
  <td>

```sql
SELECT CompanyName, MAX(CustomerID) as CustomerID
FROM Customer
GROUP BY CompanyName

```

</td>
  <tr>
  
  </table>





</br></br></br>

# Laboratory work #5
<table style='width:100%'>
  <tr>
    <th style="width:40%">Questions</th>
    <th>Answers</th>
    
  </tr>
  <tr>
    <td>Table HumanResources.Employee from AdventureWorks2019 database contains a field called LoginID. It is filled with the data using the pattern [db_name]\[username] as shown at the screenshot below.<br>
Write a query which returns usernames only (data after "\" symbol) as shown at highlighted part of the screenshot<br><br>

Please provide the whole query as the answer
<p  align=center ><img align='center' src=./documetation_resources/p004.png /></p> 

<br>
</td>
    <td>
    You can use the SUBSTRING function along with the CHARINDEX function to achieve this. The query would look something like this:

<br>

```sql
SELECT SUBSTRING(LoginID, CHARINDEX('\', LoginID) + 1, LEN(LoginID)) AS username
FROM HumanResources.Employee;
```

</td>
  </tr>
  <tr>
    <td>Check the content of <b>Person.Person, Person.PersonPhone</b> and <b>Person.PhoneNumberType</b> tables from <b> AdventureWorks2019</b> database. <br>
    <br>

Write a query that shows each person's First Name, Last Name, Phone Number, but only for the recors with "Employee" Person Type and "Work" Phone Type (please do not "hardcode" the phone type, use subquery or join instead)
<br><br>
Please provide the whole query as the answer</td>
    <td>
    
```sql
SELECT p.FirstName, p.LastName, pp.PhoneNumber
FROM Person.Person p
INNER JOIN Person.PersonPhone pp ON p.BusinessEntityID = pp.BusinessEntityID
INNER JOIN (
    SELECT BusinessEntityID
    FROM Person.PhoneNumberType
    WHERE Name = 'Work'
) pnt ON pp.PhoneNumberTypeID = pnt.PhoneNumberTypeID
WHERE p.PersonType = 'EM'

```

</td>
  </tr>
  <tr>
    <td><b>Prerequisite:</b> run the following query in the <b> AdventureWorks2019 </b>database connection script:

delete from Person.EmailAddress where BusinessEntityID between 286 and 298;

Then using tables Person.Person and Person.EmailAddress write a query which will show all the fields from the Person table only for the entries which does not have an email set up in EmailAddress table.

Please provide the whole query as the answer</td>
    <td>
    
```sql
SELECT Person.*
FROM Person
LEFT JOIN EmailAddress ON Person.BusinessEntityID = EmailAddress.BusinessEntityID
WHERE EmailAddress.EmailAddressID IS NULL;
```

</td>
  </tr>
  <tr>
    <td>Prerequisite: run the following query in AdventureWorks2019 database :
<br><br>
Update HumanResources.JobCandidate set BusinessEntityID = 212 where jobCandidateId = 6;
<br><br>
Table HumanResources.JobCandidate contains info about candidates. Entries with non-NULL BusinessEntityID field already have an interviewer assigned - this BusinessEntityID represents interviewer's ID.<br><br>

So, using the following tables:<br>

```sql
HumanResources.JobCandidate
HumanResources.Employee
Person.Person
Person.PersonPhone
Person.PhoneNumberType
```

Write a query which returns info about all currently assigned  interviewers in JobCandidate table: their FirstName and LastName, and a PhoneNumber if the type of PhoneNumber is "Work"; if it's not "Work" - default Phone Number to '8-800-555-35-35'
Info about the same interviewer should appear only ONCE.

Please provide the whole query as the answer
<p  align=center ><img align='center' src=./documetation_resources/p005.png /></p> 
</td>
    <td>

```sql
SELECT DISTINCT
    p.FirstName,
    p.LastName,
    COALESCE(
        (SELECT top 1 pp.PhoneNumber 
         FROM Person.PersonPhone pp 
         JOIN Person.PhoneNumberType pnt ON pp.PhoneNumberTypeID = pnt.PhoneNumberTypeID
         WHERE pnt.Name = 'Work' AND pp.BusinessEntityID = e.BusinessEntityID), 
        '8-800-555-35-35') AS PhoneNumber
FROM HumanResources.JobCandidate jc
JOIN HumanResources.Employee e ON jc.BusinessEntityID = e.BusinessEntityID
JOIN Person.Person p ON e.BusinessEntityID = p.BusinessEntityID
WHERE jc.BusinessEntityID IS NOT NULL

```

</td>
  </tr>
  <tr>
    <td>
    This excercise uses AdventureWorksLT2019 database, not AdventureWorks2019 - be careful<br><br>

Write a query which will show all Customer FN/LN from table Customers and their respective Address ID's from table CustomerAddress. In case if there's more than one address for a particluar customer in the CustomerAddress table, choose the record with AddressType = 'Main Office'. Result dataset should contain only 1 row for each Customer.<br>
<br>
Don't be shy to use subqueries.<br>

Please provide the whole query as the answer</td>
    <td>
```sql
SELECT c.FirstName, c.LastName, ca.AddressID
FROM Customers c
JOIN (SELECT CustomerID, AddressID
      FROM CustomerAddress
      WHERE AddressType = 'Main Office'
      UNION
      SELECT CustomerID, AddressID
      FROM CustomerAddress
      WHERE AddressType != 'Main Office'
      AND NOT EXISTS (SELECT 1 FROM CustomerAddress WHERE AddressType = 'Main Office' AND CustomerID = CustomerAddress.CustomerID)) ca
ON c.CustomerID = ca.CustomerID
```

</td>
  </tr>
</table>
 </br></br></br>


# Laboratory work #6
<h2 align="center">(SP basics)</h2> 
<p align="center"> https://www.youtube.com/watch?v=fjNsRV4zLdc</p></>
<h2 align="center">(
SP with parameters)</h2> 
<p align="center"> https://www.youtube.com/watch?v=Vs-atxMs4mw</p></>




<table style='width:100%'>
  <tr>
    <th style="width:40%">Questions</th>
    <th>Answers</th>
    
  </tr>
  <tr>
    <td>What is obligatory for a SP creation?</td>
    <td>Provide a name to the SP</td>
  </tr>
  <tr>
    <td>What is the correct syntax to execute getFirstName procedure?</td>
    <td>EXECUTE getFirstName</td>
  </tr>
    <tr>
    <td>What should be used in case is you want to change the code of SP?</td>
    <td>We change the word "CREATE" to "ALTER"</td>
  </tr>
  <tr>
    <td>What should be used in case is you want to delete the SP?</td>
    <td>you can use the DROP PROCEDURE statement. The syntax is as follows:

``` sql
DROP PROCEDURE [schema_name.]procedure_name;
```

</td>
  </tr>
  <tr>
    <td>Assuming that you have the following procedure (you can try to create it in
AdventuryWorks2019 database): <br>

```sql
CREATE PROC getProduct AS
SELECT *
FROM Production.Product
WHERE SafetyStockLevel >= 100;
```
Modify it: is should receive as a perameter the min value of SafetyStockLevel
(instead of hardcoding it to 100)<br><br>
Please provide the whole SQL query as an answer
</td>
    <td>

```sql
    CREATE PROC getProduct (@MIN AS INT)
AS
SELECT *
FROM Production.Product
WHERE SafetyStockLevel >= @MIN;
```
</td>
  </tr>
  <tr>
    <td>
Considering that @Name - is a parameter of any SP, what is the correct way to
apply this parameter to any hardcoded string?
    </td>
    <td>@Name + ' is a student'</td>
  </tr>
  <tr>
    <td>What should you use if you need to specify a default value for any of SP
parameter?</td>
    <td>
    
```sql
    After the AS statement, we simply write = sign and the default value
Example: @MIN AS INT = 30
```
</td>
  </tr> <tr>
    <td>Check the content of Production.ProductListPriceHistory and
Production.Product tables from AdventureWorks2019 database.<br>
Write a SP that:<br>
takes as a parameter @countNumber;<br>
returns all the ProductIDs, product Names, count of occurencies and maximum
value of ListPrice for all the products that appear in ProductListPriceHistory table
@countNumber times.<br><br>
Please provide the whole SQL query as an answer</td>
    <td>
    
```sql
create or alter procedure getProds(@countNumber int) as
begin
    select Prod.ProductID,
           Prod.Name,
           count(ProdHist.ProductID) Occurencies,
           max(ProdHist.ListPrice)   "Max list price"
    from Production.ProductListPriceHistory ProdHist
             left join Production.Product Prod on ProdHist.ProductID = Prod.ProductID
    group by Prod.ProductID, Prod.Name
    having count(ProdHist.ProductID) = @countNumber
end
```
</td>
  </tr>
 </table>




</br></br></br>


# Laboratory work #7 
<h2 align="center">(Variables)</h2> 
<p align="center"> https://www.youtube.com/watch?v=NmYaOlcbfZM</p></>
<h2 align="center">(
Output Parameters & Return Values</h2> 
<p align="center"> https://www.youtube.com/watch?v=GvRv4V-AK70</p></>

<table style='width:100%'>
  <tr>
    <th style="width:40%">Questions</th>
    <th>Answers</th>
    
  </tr>
  <tr>
    <td>The query below returns top 4 records from table Employee (AdventureWorks2019 database)

```sql
SELECT TOP 4 *
FROM HumanResources.Employee;
```

Please add a parameter @Num which can be used instead of hardcoded value and check that the query works in a database. Hint: most probably just raplacing 4 with @Num will not work.
<br><br>
Please provide the whole query as the answer.</td>
    <td>
  
  ```sql
  DECLARE @Num INT = 4

SELECT TOP (@Num) *
FROM HumanResources.Employee;
  ```
  
  </td>
  </tr>
  <tr>
    <td>Can we use a subquery in order to assign an initial value to the variable just in DECLARE statement? Please check in DB</td>
    <td>yes
    <br>
    (exemple (not in question): DECLARE @variable_name INT = (SELECT value FROM table WHERE condition);)</td>
  </tr>
  <tr>
    <td>What function can be used in case if you want to show some text output in the "Messages" tab of the script output window?</td>
    <td></td>
  </tr>
  <tr>
    <td>How can you suppress the default message about how much rows have been affected by the query in the "Messages" tab of the script output window?
    <p  align=center ><img align='center' src=./documetation_resources/p001.png /></p> 
    </td>
    <td></td>
  </tr>
  <tr>
    <td>Look at the query and it's output at the screenshot below.
<br><br>
How do you think, what will happen if we'll try to assign the output of this query to a single variable of type int as in the script below?

```sql
DECLARE @test AS INT

SELECT TOP 3 @test = BusinessEntityID
FROM HumanResources.Employee
ORDER BY BusinessEntityID DESC
```
<br>
<p  align=center ><img align='center' src=./documetation_resources/p002.png /></p> 
</td>
    <td></td>
  </tr>
  <tr>
    <td>At the previous work #6 we've created a Stored Procedure which returns some select output - you can double check it on https://docs.google.com/forms/d/1Fzqykk-BZvS1I3X417xWtGRzO4Z1L4DuN-PkleCLCdE/ 
<br><br>
Now, please create a new one proc which actually soes the same but in another format:

- takes as a parameter @countNumber;<br>
- returns you as output parameter the set of ProductId values in a single concatenated string<br>
- values should be separated by comma for the products that appear in ProductListPriceHistory table @countNumber times<br>
- returns you as output parameter the number of rows affected
<br><br>
These two output parameters must be accessable outside of SP after it's invocation
<br><br>
Please see the example at the screenshot below:
<p  align=center ><img align='center' src=./documetation_resources/p003.png /></p> </td>
    <td></td>
  </tr>
  </table>

</br></br></br>


# Laboratory work #8

<h3 align="center"><i>Skipped topics:</i> If statements, While loops (should be familiar from other Programming Languages)</h3> <br>
<h2 align="center">(User defined functions)</h2> 
<p align="center">  https://www.youtube.com/watch?v=6BslHItOTjU</p></talbe>
<h2 align="center">(Temporary tables)</h2> 
<p align="center"> https://www.youtube.com/watch?v=3ZtYrELHP8M </p></>


<table style='width:100%'>
  <tr>
    <th style="width:40%">Questions</th>
    <th>Answers</th>
    
  </tr>
  <tr>
    <td>You need<b> to create a Function</b> called<b> getPbdDate</b> which takes as a parameter any date and returns it's Previous Business Day value (do not take into consideration holidays, only weekends).
<br><br>
Look at the screenshot below - I've created such function and you can chack how it behaves.
<br><br>
As a sample data you can also use  Production.BillOfMaterials table from
AdventureWorks2019 Database - StartDate field has a lot of different values for different dates.
 <br><br>
Please<b>provide the whole CREATE FUNCTION</b> statement as the answer.<br>
<p  align=center ><img align='center' src=./documetation_resources/p006.png /></p> 
  
</td>
    <td></td>
  </tr>
   <tr>
    <td>Let's take a look at the<b> HumanResources.Employee<./b> table in AdventureWorks2019 Database: it contains 290 records; each of them has it's own BusinessEntityID which is unique ID value starting from 1 to 290.
<br><br>
Let's assume that there's a Process which can be run in N parallel threads; each of these threads should pick up the data from<b> HumanResources.Employee</b> table - so if the process is running in 2 threads, the first thread will pick up 145 records out of 290, and the second - remaining 145 records out of 290.
<br><br>
So you need to write a function called<b> getThreadNumber</b> which will take as an input parameters BusinessEntityID field and N - number of parallel threads, and will return the ID of thread assigned for each particular row.<br>
<p  align=center ><img align='center' src=./documetation_resources/p007.png /></p> 
  </td>
    <td></td>
  </tr> <tr>
    <td>What is the scope of visibility of the temporary table #Test?</td>
    <td></td>
  </tr>
   <tr>
    <td>Prerequisite: run the following query in the AdventureWorks2019 database connection script:<br>

```sql
delete from Person.EmailAddress where BusinessEntityID between 286 and 298;

delete
from Person.PersonPhone
where BusinessEntityID between 32 and 40;
```
<br>
Then using tables Person.Person, Person.EmailAddress and Person.PersonPhone, write a query which will show [BusinessEntityID, FirstName, LastName, EmailAddress, PhoneNumber] for persons which does not have an email set up in EmailAddress table or PhoneNumber set up in a PersonPhone table. Result should be written in a temporary table
<br><br>
Please provide the whole query as the answer<br>
<p  align=center ><img align='center' src=./documetation_resources/p008.png /></p> 
 </td>
    <td></td>
  </tr>
 
  </table>