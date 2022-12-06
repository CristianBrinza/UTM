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
<hr></br>
</br></br>



</br></br></br>

<p align="right">DB | Boris Galcenco | 17.11.2022</p>
</br>

# General DB design principles

## 2 GOLDEN RULES:
- Avoid Duplication and Redundancy (duplication is bad) 
- Ensure Data Quality (Accuracy and Completeness)


## Basic Design steps
- Check data for duplicates and break them into tables
- Define the relationship between the tables + Define the Primary Key's and Foreign Key's

- Identify the Dependent and Independent tables Normalize and Review for completeness


## The design process:

- Determine the database purpose
- Discover and collect information
- Divide the entities into tables
- Turn the data points into columns
- Identify primary and foreign keys
- Normalize and refine

---
<h2 align="center"> Individual work</h2>
<h3 align="center"> video link : <a>https://www.youtube.com/watch?v=UICZXMhfNCo</a></h3>
</br>
Options:

 1. Build flat customer structure (if. The data doesn’t change too much and easy solution)
 2. Build generic customer structure ( more flexible)

 <table>
  
  <tr>
    <td>
    #1:<i> build flat COstumer structure</i></br>
    Check if the customer exists</br>
    Check if the record exists 
    </td>
    <td>
    <p  align=center ><img align='center' style="height: 50%;
  width: 50%; " src=documetation_resources/p001.png /></p>
    </td>
  </tr>
  <tr>
   <td>
    #2:<i> build gereric Costumer structure</i>  </br>
    Mape mapping tables …</br>
    note: create creation_date for getting the most recent record
    </td>
    <td>
    <p  align=center ><img align='center' style="height: 50%;
  width: 50%; " src=documetation_resources/p002.png /></p>
    </td>
  </tr>
</table> 

---

## Data Analysis & research


0. THe GOAL / purpose 
1. Black box
2. Simplify (define Objects)
3. Decomposition in Siple Objects
4. Loop each object 
    - atributes
    - funcions
    - propreties 


---
exemple of individual work to present

## "Eyelashes" Data analysis


REPORT:
- Term
   - Eyelashes
- Dimensions
  - brush
  - container
  - content
- Final fact
    - depends on revews
    - depends on aspect
    - depends on quality
- Analize & exemple
  - place to sell (targhet audience location and places of intresets)
  - ingredients (statistics)
  - sizes & shapes (feedback)
  
---





identify problem -> ... -> ... -> goal result

... - steps , for every single step u need to ask questions, and research



---
---
---

Midterm

Eyelashes


---
Dimensions
*
Example
Maretial: Mat_ID, Description
Liquid Type: LiqType_ID, Description
DesignType: Design_ID,Description
..............
BodyMartial: BodyMat_ID, Description
Brush Type: BrushType_ID, Description
Color: Color_ID, Description
Content: Content_ID, Description (the eyelash substance)
DesignType: Design_ID,Description

---
Final Fact Table

Bottle_Types

Field                 Type / Func
Bottle_ID          PK
Mat_ID             FK
LiqType_ID      FK
Design_ID        FK
Volume            INT
Size_W             INT
Size_H              INT
DateFirstProduced Date
DateLastProduced Date
..............
Field                 Type / Func
Eylash_ID          PK
BrushType_ID   FK
BodyMat_ID      FK
Color_ID            FK
Content_ID       FK
Design_ID         FK
Volume            INT
Size_X              INT
Size_Y              INT
Size_Z              INT
DateFirstProduced Date
DateLastProduced Date
Eylash_price    INT

---
Analysis type which could be performed

Most often liquid
Most often design
Most popular volume
Most popular size
Bottle life-cycle
..............
*most often size, color, and 
* depends on reviews, aspects,  quality, and brand popularity
* Analyze & examples (in parenthesis is the type)
  - place to sell (target audience location and places of interest)
  - ingredients (statistics)
  - sizes & shapes (feedback)