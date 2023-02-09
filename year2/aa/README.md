<h4 align="center">FCIM UTM </h4>
<h1 align='center'> 
▒▄▀▄▒▄▀▄<br>
░█▀█░█▀█
</h1>
<h4 align="center">Technical University of Moldova  </h4>
<h4 align="center">FCIM   |   UTM   |   Spring 2022</h4>
<p align=center>                           
  <img align=center style="height: 50%;
  width: 50%; " src="https://utm.md/wp-content/uploads/2020/12/logo-sigla.png" />
</p>
</br><p align=right>  
p. Analiza Algoritmilor
</p>
<p align=right>  
lab. Cristofor FIstic
</p>
</br><p align=center>  
Chisinau 2022
</p>
<hr></br>
</br></br>
<p align=right>  
c. AA | FCIM UTM Spring 2022 | 3-104 | 08.02.2023
</p>

Problem:

Grandma gave each grandchild <b>a</b> pen and <b>two</b> pencils, she had 5 pens and 19 pencils left. How many grandchildren does the grandmother have, if initially there were three times as many pencils?

<h2></h2>
<table>
<tr>
    <th style="width:40%">Code</th>
    <th style="width:10%">Cost</th>
    <th style="width:10%">N2</th>
    
  </tr>
  <tr>
    <td>

```
suma (n)
    s <- 0
    i <- 1
    while  i<=n do
        s <- s + i
        i <- i + 1
return s
```

</td>
    <td>
    1<br>
    1<br><br>
    1<br>
    2<br>
    2<br>
    <br><br>
    </td>
    <td>
    1<br>
    1<br><br>
    1<br>
    2<br>
    2<br>
    <br><br></td>
  </tr>
</table>
<table>
<tr>
    <th style="width:80%">Code</th>
    <th>Cost</th>
    <th>N2</th>
    <th style="width:80%"></th>
    
  </tr>
  <tr>
    <td>

```
produs (a[1..m][1..n], b[1..n][1..p])                   
    for i = 1..m   do
        for j = 1..p   do
            c[i,j]
            for k = 1..n   do
                    c[i,j] <- c[i,j] + a[i,k]*b[k,j]
return c[1..m, 1..p]
```

</td>
    <td>
    c1<br>
    2<br>
    2<br>
    1<br>
    2<br>
    c2<br><br><br>
    </td>
    <td>
    <br>
    m<br>
    m*p<br>
    m*p<br>
    m*p*n<br>
    m*p*n<br><br><br></td>
    <td>T(m p n),<br> O(n&#xB3), n->N</td>
  </tr>

</table>

```
Code                                                     C      N2
-------------------------------------------------------+----+---------
produs (a[1..m][1..n], b[1..n][1..p])                  | c1               
    for i = 1..m   do                                  | 2
        for j = 1..p   do                              | 2
            c[i,j]                                     | 1
            for k = 1..n   do                          | 1
                    c[i,j] <- c[i,j] + a[i,k]*b[k,j]   | 2
return c[1..m, 1..p]                                   | c2
```


```
Code                        C      N2
--------------------------+----+---------
minim(x[1..n])            | c1 | 
    m <- x[1]             | 1  | 1
    for i=2 to n          | 3  | n
        if a[1]<m then    | 2  | n-1
            m <- a[i]     | 1  |tau(n)
return m                  |    |
```


Pentru acasa: 

```
m <- 1
for i <- 1, n do
    m <- 3*m
    for j <- 1, m doo
        O(c1)
```

<hr>