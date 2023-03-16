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

<b>Algoritm</b> - o metoda de rezolvare pas cu pas a problemelor;<br>
<b>Problema</b> - date de intrare si un enunt (care specifica relatia existenta intre datele
de intrare si solutaia)<br>
<b>Analiza algoritmilor</b> presupune verificarea corectitudinii acestora si a eficientei<br>
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
<h3>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Elaborarea unui algoritm necesita:</b></h3>

<li> Cunostinte specifice domeniului de unde provine problema de rezolvat;</li>
<li>Tehnici generale de rezolvare a problemelor;</li>
<li>Intuitie si gandire algoritmica.</li>
<br>



<h2><b>3. Proprietatile algoritmilor</b></h2>

Un algoritm trebuie sa posede urmatoarele proprietati:
- <b style="font-size:16px;"> Generalitate</b> <br><i style="padding-left: 10px;"> Un algoritm destinat rezolvarii unei probleme trebuie sa permita obtinerea rezultatului pentru orice date de intrare si nu numai pentru date particulare de intrare.</i>
- <b style="font-size:16px;"> Finitudine</b><br><i style="padding-left: 10px;"> Un algoritm trebuie sa admita o descriere finita si fiecare dintre prelucrarile pe care
le contine trebuie sa poate fi executata in timp finit. Prin intermediul algoritmilor nu pot fiprelucrate structuri infinite.</i>
- <b style="font-size:16px;"> Rigurozitate</b><br><i style="padding-left: 10px;"> Prelucrarile algoritmului trebuie specificate riguros, fara ambiguitati. In orice etapa
a executiei algoritmului trebuie sa se stie exact care este urmatoarea etapa ce va fi executata.</i>
- <b style="font-size:16px;"> Eficienta</b><br><i style="padding-left: 10px;"> Algoritmii pot fi efectiv utilizati doar daca folosesc resurse de calcul in volum acceptabil.</i>

<br><br>


<h2><b>4.Date</b></h2><br>

- <b style="font-size:16px;"> Simple</b> -<i> contin o singura valoare (poate fi un numar, o valoare de adevar sau un caracter).</i>
- <b style="font-size:16px;"> Structurate</b> -<i> sunt constituite din mai multe date simple intre care exista o relatie de structura.
Daca toate datele componente au aceeasi natura atunci structura este <b>omogena</b>, altfel este o structura <b>heterogena</b>.</i>
  - <b style="font-size:16px;"> omogene </b>-<i>  utilizate in continuare sunt cele destinate reprezentarii
unor structuri algebrice simple: </i>
    - <b> multime finita </b><i> (ansamblu de valori distincte pentru care nu are
importanta ordinea in care sunt retinute), </i>
    - <b> sir finit </b><i> (ansamblu de valori nu neaparat distincte pentru
care are importanta ordinea in care sunt retinute) </i>
    - <b> matrice </b><i> (tabel bidimensional de valori).</i>
  - <b style="font-size:16px;"> heterogena </b>
<br><br>

Pentru reprezentarea acestor date vom folosi structura de <b><i>tablou</i></b> caracterizata prin faptul ca
fiecare valoare componenta poate fi specificata prin precizarea unuia sau mai multor indici. <br>
<i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Cel mai frecvent sunt folosite tablourile:</i>

- <b style="font-size:16px;"> unidimensionale</b> <i> (pentru reprezentarea sirurilor si multimilor)</i>
- <b style="font-size:16px;"> bidimensionale </b> <i>(pentru reprezentarea matricilor).</i>
<br>
<h2><b>5.Tipuri de Prelucrarica</b></h2><br>



- <b style="font-size:16px;"> Simple </b>
  - <b style="font-size:16px;">  Atribuire</b> -<i> Permite afectarea unei valori unei variabile. Valoarea atribuita poate fi rezultatul
evaluarii unei expresii. O expresie descrie un calcul efectuat asupra unor date si contine operanzii (specifica datele asupra carora se efectueaza calculele) si operatori (specifica prelucrarile
ce se vor efectua).</i>
  - <b style="font-size:16px;"> Transfer</b> -<i> Permit preluarea datelor de intrare ale problemei si furnizarea rezultatului.</i>
  - <b style="font-size:16px;"> Control</b> -<i> In mod normal prelucrarile din algoritm se efectueaza in ordinea in care sunt specificate. In cazul in care se doreste modificarea ordinii naturale se transfera controlul executiei
la o anumita prelucrare.</i>
- <b style="font-size:16px;"> Structurate </b>
  - <b style="font-size:16px;">  Secventiala</b> -<i> Este o succesiune de prelucrari (simple sau structurate). Executia structurii
secventiale consta in executia prelucrarilor componente in ordinea in care sunt specificate.</i>
  - <b style="font-size:16px;"> De decizie </b>(alternativa)-<i>  Permite specificarea situatiilor in care in functie de realizarea sau
nerealizarea unei conditii se efectueaza o prelucrare sau o alta prelucrare. Conditia este
de regula o expresie a carui rezultat este o valoare logica (adevarat sau fals). O astfel de
prelucrare apare de exemplu in evaluarea unei functii definite prin:</i> <p style="margin-bottom:0; margin-top:0;"  align=center ><img align='center' style="height: 30%;
  width: 30%; " src=documetation_resources/p001.png /></p>
  - <b style="font-size:16px;"> De ciclare </b> (repetitiva) - Permite modelarea situatiilor cand o prelucrare trebuie repetata.
Se caracterizeaza prin existenta unei prelucrari care se repeta si a unei conditii de oprire(sau de continuare). In functie de momentul in care este analizata conditia exista <b>prelucrari</b> repetitive :
    - <b style="font-size:16px;"> conditionate anterior</b> (conditia este analizata inainte de a efectua prelucrarea) 
    - <b style="font-size:16px;">  conditionate posterior</b> (conditia este analizata dupa efectuarea prelucrarii). O astfel
de prelucrare apare de exemplu in calcului unei sume finite  (In acest caz prelucrarea
care se repeta este adunarea iar conditia de oprire o reprezinta faptul ca au fost adunati toti
cei n termeni.)<p style="margin-bottom:0;" align=center ><img align='center' style="height: 15%;
  width: 15%; " src=documetation_resources/p002.png /></p> 

<br><br>
<h2 align="center"><b> Problema:</b></h2>

Grandma gave each grandchild <b>a</b> pen and <b>two</b> pencils, she had 5 pens and 19 pencils left. How many grandchildren does the grandmother have, if initially there were three times as many pencils?
<br><br>

<h3 align="center">"<b>C</b>" - Cost	| "<b>N2</b>" - Nr. repetari </h3>

<p align="center">Timpul de execu)tie a algoritmului poate fi determinat folosind <b><i>tabelul de costuri</i></b>:
</p>

```
Code                     C      N2
----------------------+----+---------
suma (n)              |    |  
    s <- 0            | 1  |  1
    i <- 1            | 1  |  1
    while  i<=n do    | 1  |  n+1
        s <- s + i    | 2  |  n
        i <- i + 1    | 2  |  n
return s              |    |
----------------------+----+---------
                  7n+3 (liniar)=> O(n)
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
------------------------------------------------------+----+---------
                                                   T(m*p*n)| O(n³), n->N
```




```
Code                        C      N2
--------------------------+----+---------
minim(x[1..n])            | c1 | 
    m <- x[1]             | 1  | 1
    for i=2 to n          | 3  | n
        if a[i]<m then    | 2  | n-1
            m <- a[i]     | 1  |tau(n)
return m                  |    |
                     T(n) |
```

<br>
<h2 align="center">🏡 Pentru acasa: &nbsp;&nbsp;<i>(solved)</i> </h2>

```
Code                               C      N2
--------------------------------+----+---------
m <- 1                          | 1  |  1
for i <- 1, n do                | 1  |  n
    m <- 3*m                    | 2  |  2n
    for j <- 1, m doo           | 1  |  3ⁿ
        O(c1)                   | 1  |  3ⁿc


```

<hr>
<br>
<p align=right>  
c. AA | FCIM UTM Spring 2022 | 3-104 | 15.02.2023
</p>



<h2 align="center">🏡 Pentru acasa: &nbsp;&nbsp;<i>(solved)</i> </h2>

<br>
<h2 align="center"><b> Problema:</b></h2>
<i>&nbsp;&nbsp;&nbsp;&nbsp; There are 12 coins. One of them is false; it weights differently. It is not known, if the false coin is heavier or lighter than the right coins. How to find the false coin by three weighs on a simple scale?</i>


1. Start by numbering the coins 1..12.
    - put 1,2,3,4 on the left scale, 5,6,7,8 on the right.
2. <b>outcome (1):</b> even balance => one of the last 4 coins is false. Now put 9, 10 and 11 on the left and 1, 2 and 3 on the right side.
    - <b>outcome (1.1)</b> even balance => coin 12 is false. Compare 1 and 12 to find out if 12 is lighter or heavier.
    - <b>outcome (1.2)</b> left goes down => 9, 10 or 11 is heavier. Compare 9 and 10 to see which one is heavier, or, if equal, 11 is heavier.
    - <b>outcome (1.3)</b> right side goes down => 9, 10 or 11 is lighter. Figure out which one like (1.2)
3. <b>outcome (2):</b> left side goes down => 1,2,3 or 4 is too heavy or 5, 6, 7 or 8 too light. Put 1,2 and 5 on the left side and 3,4 and 6 on the right.
    - <b>outcome (2.1)</b> even balance: 7 or 8 is too light. compare them to find out which one.
    - <b>outcome (2.2)</b> left side goes down => 1 or 2 is too heavy or 6 is too light. compare 1 and 2 to find out which one is heavier. if even balance, 6 is too light.
    - <b>outcome (2.3)</b> right side goes down => 3 or 4 too heavy, or 5 is too light. Figure out which one by comparing 3 and 4.
4. <b>outcome (3):</b> right side goes down => 1,2,3,4 too light or 5,6,7,8 too heavy. Similar to (2).e 


or... (second method)

1. We put half of the coins on one side of the scale and half on the other side of the scale.
2. We shall be able to find the six coins including the false coin.
3. We divide these six coins including the false coin into two groups each having three coins. We put three coins one side of the scale and the other three on the other side of the scale.
4. We shall be able to identify 3 coins with false coin included.
5. We can put one coin from these three coins on one side of the scale and another on the other side. These two coins will weigh equal or one will be different. We shall be able to identify the false coin



<br>
<h2 align="center"><b> Problema:</b></h2>
<i>&nbsp;&nbsp;&nbsp;&nbsp; I am in a 100-story building. I have with me two glass balls. I know that if I throw the ball out of the window, it will not break if the floor number is less than X, and it will always breaks if the floor number is equal to or greater than X.<br>
&nbsp;&nbsp;&nbsp;&nbsp; Assuming that I can reuse the balls which don't break, find X in the minimum number of throws.</i><br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;This is a classic puzzle known as the Two Glass Balls or Two Eggs Problem. The goal is to minimize the worst-case number of throws to find the floor number X, where the glass ball breaks.
<br>
<br>
<p align="center">Here's the optimal strategy:</p>

1. Start by dividing the 100 floors into intervals. You can choose an interval size N, and throw the first ball at every Nth floor, starting from floor N, then 2N, 3N, and so on.
    - If the first ball breaks at floor Ni, you know that X is between (N(i-1)+1) and N*i (inclusive).
2. Now, take the second ball and start testing each floor within that interval, starting from the floor (N*(i-1)+1) and going up one floor at a time.
3. To minimize the maximum number of throws, you need to find the optimal interval size N. 
    - In the worst case, you might need to throw the first ball N times and the second ball (N-1) times. So the worst-case number of throws is N + (N-1), which should be minimized.

<p align="center">For a 100-story building, the optimal interval size is 14. 
</p>
This means you throw the first ball at floors 14, 28, 42, 56, 70, 84, and 100. In the worst case, you would need 14 throws for the first ball and 13 throws for the second ball, resulting in a maximum of 27 throws in total.

<br>
<p align="center"><b>So, using this strategy, you can find the floor number X in at most 27 throws.</b></p>


<hr>
<br>
<p align=right>  
c. AA | FCIM UTM Spring 2022 | 3-104 | 15.03.2023
</p>

