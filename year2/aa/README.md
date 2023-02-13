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

<h2 ><b>1. Introducere in algoritmi</b></h2><br>

<b>Algoritm</b> - o metoda de rezolvare pas cu pas a problemelor;

<b>Problema</b> - date de intrare si un enunt (care specifica relatia existenta intre datele
de intrare si solutaia)

<b>Analiza algoritmilor</b> presupune verificarea corectitudinii acestora si a eficientei

<b>Resurse de calcul</b> - volumul de memorie si timpul necesar pentru executie.
<br><br>
<p align="center"><i> "Un algoritm este o succesiune bine precizata de prelucrari care aplicate asupra datelor
de intrare ale unei probleme permit obtinerea in timp finit a solutiei acesteia."</i></p>
<br>

- Algoritm provine de la numele-  al-Khowarizmi (matematician persan), sec IX-lea, a scris o lucrare despre efectuarea calculelor
- Primul algoritm <b> "algoritmul lui Euclid"</b>
<br><br>


<h2><b>2. Obiectul disciplinei</b></h2>

<h4 align="center">"Studiul algoritmilor din perspectiva elaborarii si analizei lor."</h4> <br>
<h3>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Elaborarea unui algoritm necesita:</h3>

<li> Cunostinte specifice domeniului de unde provine problema de rezolvat;</li>
<li>Tehnici generale de rezolvare a problemelor;</li>
<li>Intuitie si gandire algoritmica.</li>
<br>



<h2><b>3. Proprietatile algoritmilor</b></h2>

Un algoritm trebuie sa posede urmatoarele proprietati:
- Generalitate. Un algoritm destinat rezolvarii unei probleme trebuie sa permita obtinerea rezultatului pentru orice date de intrare si nu numai pentru date particulare de intrare.
- Finitudine. Un algoritm trebuie sa admita o descriere finita si fiecare dintre prelucrarile pe care
le contine trebuie sa poate fi executata in timp finit. Prin intermediul algoritmilor nu pot fiprelucrate structuri infinite.
- Rigurozitate. Prelucrarile algoritmului trebuie specificate riguros, fara ambiguitati. In orice etapa
a executiei algoritmului trebuie sa se stie exact care este urmatoarea etapa ce va fi executata.
- Eficienta. Algoritmii pot fi efectiv utilizati doar daca folosesc resurse de calcul in volum acceptabil.

<br><br>


<h2><b>4.Date</b></h2><br>

- <b>Simple</b> - contin o singura valoare (poate fi un numar, o valoare de adevar sau un caracter).
- <b>Structurate</b> - sunt constituite din mai multe date simple intre care exista o relatie de structura.
Daca toate datele componente au aceeasi natura atunci structura este <i>omogena</i>, altfel este o structura <i>heterogena</i>.
  - omogene -  utilizate in continuare sunt cele destinate reprezentarii
unor structuri algebrice simple: 
    - <b> multime finita </b> (ansamblu de valori distincte pentru care nu are
importanta ordinea in care sunt retinute), 
    - <b> sir finit </b> (ansamblu de valori nu neaparat distincte pentru
care are importanta ordinea in care sunt retinute) 
    - <b> matrice </b> (tabel bidimensional de valori).

<br>
Pentru reprezentarea acestor date vom folosi structura de <b><i>tablou</i></b> caracterizata prin faptul ca
fiecare valoare componenta poate fi specificata prin precizarea unuia sau mai multor indici. <br>
<i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Cel mai frecvent sunt folosite tablourile:</i>

- unidimensionale (pentru reprezentarea sirurilor si multimilor)
- bidimensionale (pentru reprezentarea matricilor).
<br>
<h2><b>5.Tipuri de Prelucrarica</b></h2><br>



- <b>Simple </b>
  - <b> Atribuire</b> - Permite afectarea unei valori unei variabile. Valoarea atribuita poate fi rezultatul
evaluarii unei expresii. O expresie descrie un calcul efectuat asupra unor date si contine operanzii (specifica datele asupra carora se efectueaza calculele) si operatori (specifica prelucrarile
ce se vor efectua).
  - <b> Transfer</b> - Permit preluarea datelor de intrare ale problemei si furnizarea rezultatului.
  - Control. In mod normal prelucrarile din algoritm se efectueaza in ordinea in care sunt specificate. In cazul in care se doreste modificarea ordinii naturale se transfera controlul executiei
la o anumita prelucrare.
- <b>Structurate </b>
  - <b> Secventiala</b> - Este o succesiune de prelucrari (simple sau structurate). Executia structurii
secventiale consta in executia prelucrarilor componente in ordinea in care sunt specificate.
  - <b>De decizie </b>(alternativa)-  Permite specificarea situatiilor in care in functie de realizarea sau
nerealizarea unei conditii se efectueaza o prelucrare sau o alta prelucrare. Conditia este
de regula o expresie a carui rezultat este o valoare logica (adevarat sau fals). O astfel de
prelucrare apare de exemplu in evaluarea unei functii definite prin: <p style="margin-bottom:0; margin-top:0;"  align=center ><img align='center' style="height: 30%;
  width: 30%; " src=documetation_resources/p001.png /></p>
  - <b> De ciclare </b> (repetitiva) - Permite modelarea situatiilor cand o prelucrare trebuie repetata.
Se caracterizeaza prin existenta unei prelucrari care se repeta si a unei conditii de oprire(sau de continuare). In functie de momentul in care este analizata conditia exista <b>prelucrari</b> repetitive :
    - <b> conditionate anterior</b> (conditia este analizata inainte de a efectua prelucrarea) 
    - <b>  conditionate posterior</b> (conditia este analizata dupa efectuarea prelucrarii). O astfel
de prelucrare apare de exemplu in calcului unei sume finite <p style="margin-bottom:0;" align=center ><img align='center' style="height: 15%;
  width: 15%; " src=documetation_resources/p002.png /></p> In acest caz prelucrarea
care se repeta este adunarea iar conditia de oprire o reprezinta faptul ca au fost adunati toti
cei n termeni.

Probleme:

Grandma gave each grandchild <b>a</b> pen and <b>two</b> pencils, she had 5 pens and 19 pencils left. How many grandchildren does the grandmother have, if initially there were three times as many pencils?


```
Code                     C      N2
----------------------+----+---------
suma (n)              | 1  |  1
    s <- 0            | 1  |  1
    i <- 1            |    |
    while  i<=n do    | 1  |  1
        s <- s + i    | 2  |  2
        i <- i + 1    | 2  |  2
return s              |    |
```

```
Code                                                    C      N2
------------------------------------------------------+----+---------
produs (a[1..m][1..n], b[1..n][1..p])                 | c1 |  
    for i = 1..m   do                                 | 2  |  m
        for j = 1..p   do                             | 2  |  m*p
            c[i,j]                                    | 1  |  m*p
            for k = 1..n   do                         | 2  |  m*p*n
                    c[i,j] <- c[i,j] + a[i,k]*b[k,j]  | c2 |  m*p*n
return c[1..m, 1..p]                                  |    |

//T(m p n), O(n³), n->N
```

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

<br>
<h2 align="center">🏡 Pentru acasa: </h2>

```
m <- 1
for i <- 1, n do
    m <- 3*m
    for j <- 1, m doo
        O(c1)
```

<hr>