<h4 align="center">FCIM UTM </h4>
<h1 align='center'> 


░▒▄█▀▄░▒▐██▄▒▄██▌▒▄█▀▀█ 
▒▐█▄▄▐█░▒█░▒█░▒█░▒▀▀█▄▄ 
▒▐█░▒▐█▒▐█░░░░▒█▌▒█▄▄█▀
</h1>
<h4 align="center">Technical University of Moldova  </h4>
<h4 align="center">FCIM   |   UTM   |   Spring 2022</h4>
<p align=center>                           
  <img align=center style="height: 50%;
  width: 50%; " src="https://utm.md/wp-content/uploads/2020/12/logo-sigla.png" />
</p>
</br><p align=right>  
p. Radu Melnic
</p>
<p align=right>  
lab. Nina Sava
</p>
</br><p align=center>  
Chisinau 2022
</p>
<hr></br>
</br></br>
<p align=right>  
c.AMS | FCIM UTM Spring 2022 | 104 | 21.09.2021
</p>


Limbaj de programare – are cuinte cheie
Limbaj de modelare – are entitati si relatii

Entitatile ULM:
1) de structura
2) comportament
3) grupare
4) adnotare

<b>Entitati</b> - elementele obiect orientate ale limbajului ULM

- <b style="color:#0066ff">Entitati de structura</b> - substantivele ale limbajului ULM. De regula ele reprezinta partile statice ale modelului care crespund elementelor
  fizice si conceptuale ale sistemului. 

Entitati de structura:
1) <b>Clasa</b> - blueprintul unui obiect. Descrierea multitudinii de obiecte cu aceleasi atribute, metode si semantice
Clasa: Name, Atribute, Methods
Cuvintele cheie scrise intre paranteze figurate {} reprezinta constrangere(constanta).
Numele se incepe cu majuscula si nu poate contine caractere speciale.
2) <b>Interfata</b> - totalitatea de operatii care definesc serviciile oferite de catre clasa sau component
Interfata: Name, Dialog
3) <b>Use Case</b> (caz de utilizare - descrie consecutatea de actiuni indeplinite de catre un sistem si care produc un rezultat semnificativ pentru un anumit actor
4) <b>Colaborarea</b> - defineste o interactiune, care defineste o interactiune, reprezinta o totalitate un efect corporativ.
5) <b>Active class</b> (clasa active) - reprezinta clasa obiectele careia sunt antrenate in una sau mai multe procese si pot initia actiuni administrative
6) <b>Componenta</b> - element fizica a sistemului care corecpunde unui anumit set de interfete si asigura realizarea lor 
7) <b>Nod</b> - element real al sistemului care repezinta un mijloc de calcul cu un anumit volum de memorie, deseori cu posibilitatea prelucrarii informatiei, si exista in timpul functionarii/rularii/execuarii produsului software (reprezentat grafic un "cub")

In afara de acestea 7, mai execta .............. , </br> </br>
<b>Tipuri de componente:</b>
aplicatii, tabele, fisiere, pagini veb, documente, siruri, procese (clase active),biblioteci

</br></br></br>

<h4 align="center"><b>For next lecture:</b></h4>
Entitati de comportament :
elementele dinamice ale limbajului UML, de regula reprezinta verbele limbajului, care descriu comportamentului in timp si spatiu
</br></br>
<hr> </br>
<p align=right>  
c.AMS | FCIM UTM Spring 2022 | 104 | 28.09.2021
</p></br>

- <b style="color:#0066ff">Entitati de comportament :</b>

<b>Interactiune </b> - reprezinta un mod comportament care descrie/defineste schimbul de mesaje intre obiecte in cadrul ununi anumit contez si pentru atingerea unui anumit scop ;
</br>
 
<p  align=center ><img align='center' style="height: 30%;
  width: 30%; " src=p001.png /></p> 

 <b>Automatul</b> - reprezinta un algoritm/mod de comportament care descrie/defineste o succesiune de stari prin care trece obiectul pe parcursul ciclului sau de viata raspunzand la diferite evenimente si reactile lor la aceste evenimete ; ( element - dreptunghi cu colturi rotungite)


- <b style="color:#0066ff">Entitati de grupare</b> - elementele organizatorice ale modului UML, ele reprezintablocuri ale modelului ( care impart modelul in subunitati , de numeste package)

DEF: </br>
        <b>Package</b> - macanizm universal de organizare a efenimentelor in grup

- <b style="color:#0066ff">Entitati de adnotare:</b> 
reprezinta elementul explicativ al modelului UML, de regula sunt comentarii, explicatii sau observatii </br>


<b>Remarca</b> - simplu simbol ce reprezinta comentariile sau constrangerile (restrictiile), se reprezinta prin dreptunghi cu colt indoiat (pliat);

</br></br>
<h1 align=center>Relatiile</h1>

<b>Tipuri de relatii:</b>
1. Dependenta
2. Asocierea
3. Generalizarea
4. Realizarea

- <b style="color:#0066ff">Dependenta </b>- relatie semantintica intre doua entititati unde modificare unei din ele ( entitatea independenta) poate celei de-a doua(intitatea dependenta) ( reprezentata cu o sageata cu linie intrerupta directionata spre entitatea dependenta, de la entitatea independenta); </br>
- <b style="color:#0066ff">Asocierea </b>- relatie de structura ce reprezinta legatura intre entitati ( poate avea moltitudini:  0->1, 0->M, 1->M, M->M);
<p  align=center ><img align='center' style="height: 30%;
  width: 30%; " src=p002.png /></p>  </br>
  <p align=center>
!!! &nbsp;&nbsp;&nbsp;
  Cuvintele cheie de tip ITALIC , in UML sunt comentarii &nbsp;&nbsp;&nbsp;
!!!
</p> </br>

&nbsp;&nbsp; <b>Asocierea</b> - are caz particular / forma speciala -> "Agregare", acesta la randul sau are o forma speciala -> "Compozitia" ; 
Agregarea - reprezinta relatia dintre partea intraga si partea componenta (la distrugerea partii intregi nu distruge si partea componenta);</br></br>
&nbsp;&nbsp; <b>Compozitia</b> - relatia dintre partea intreaga si partea componenta, insa cu o forma mai specifica, de parca partea componenta este in interiorul partii intregi; ( partea componenta nu poate exista fara partea intreaga, cu alte cuvinte la distrugerea partii intregi se distruge si partea componenta) </br>

- <b style="color:#0066ff">Generalizarea </b> - relatie de tip specializare/generalizare unde un obiect specializat poate inlocui un obiect generealizat (obiectul specializat vine in locul celui generalizat (relatie de tip mostenire)), (o linie cu un triunghi la capat (sageata cu varf alb))

- <b style="color:#0066ff">Realizarea </b> -relatie semantica dintre doua entitati unde una dintre ele reprezinta un contract iar cea de-a doua o realizeaza( sageata cu linie intrerupta si varf de culoare alba)
</br></br>
se utilizeasa in doua cazuri: 
 1. intre interfata si clase sau componte ce o realizeaza ( pe aceasta interfata)
2. intre cazuri de utilizare si colaborarea ce o realizeaza


</br></br>
<h1 align=center>Diagrame</h1>
Tipuri de diagrame:

1. use-case
2. de interactiune ( de segventa si de colaborare )
3. de clase
4. de comportament ( de stare si de de activitate )
5. de componente
6. de plasare
</br>
( daca 5. si 6. diagrama este de "realizare")
</br></br>

Starea din diagrama de stari reprezinta o activitate

Starea din diagrama de activitati reprezinta o actiune
</br></br>
<b>Cazuri de utilizare</b>- un sir actiuni care trebuie sa fie executate de catre sistem in colabirare cu un anumit actor


<b>Actor</b> - entitiate externa fata de sistemul proiectat/modelat care colaboreaza/interactioneaza cu sistemul utilizand functionalitatile lui pentru un anumit scop (numele lui se scrie cu majuscula)

<b>Interfata</b> - repezinta o totalitate de operatii ce asigura serviciile necesare pentru actori ( pot contine doar operatii fara indicarea specificatilor lor de relizare, nu pot contine atribute sau/nici stari) (ex: o interfata formal poate fi considerata clasa abstracta faca atribute si metode, doar cu reprezentarea operatiolor abstracte)


<b>Colaborare</b> - defineste o interactiune care reprezinta un efect corporativ

<b>Tipuri de relatii</b> (Colaborare):
- Actor -> Actor
- Actor -> Use-Case
- Use-Case -> Use-Case
- Use-Case -> Interface
- Use-Case -> Colaborare 
<b></b>