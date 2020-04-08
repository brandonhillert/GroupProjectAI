How to Run
Setup DB
  1. run GroupProjectAI/MongoDB naar Postgres/Datascript.py
  2. run GroupProjectAI/MongoDB naar LinkSessionToProfCat.py

Setup Algortimes tables
  3.run GroupProjectAI/Algoritmes/Brand rec.py
  4.run GroupProjectAI/Algoritmes/Categorie_algoritme.py
  5.run GroupProjectAI/Algoritmes/Prijsalgoritme.py
  6.run GroupProjectAI/Algoritmes/voordeelcategorieAlgoritme.py
  
Recommendation table conversion
  7. run GroupProjectAI/Website/data_omzetten_bruikbare_table.py
  
Website hosting
*controleer file path in bat files
  8. run GroupProjectAI/Website/Run Huwebshop/Klik mij 1st.bat
  9. run GroupProjectAI/Website/Run Huwebshop/Klik mij als 2e.bat


Mappen structuur

Algoritmes folder
  Brand rec.py
    -Definitieve versie Brand Algoritme
  Categorie_algoritme.py
    -Definitieve versie Categorie Algoritme
  Prijsalgoritme
    -Definitieve versie Prijs Algoritme
  VoordeelcategorieAlgoritme
    -Definitieve versie voordeelcategorie Algoritme

ERD diagram folder
  ERD Diagram DB Current
    -De Meest recente DB ERD
  GroupProjectAI_new_postgres_create.sql
    -SQL code om een lege voorbeeld DB temaken(redounded)
    
MongoDB naar Postgres folder
  Datascript
    -De main Script om de DataBase helemaal overtezetten van mongo Naar Postgress
  DatascriptSlow
    -alternatieve main Script (Niet bruikbaar genoeg voor ons doeleinde)
  LinkSessionToProfCat.py
    -Script voor het koppellen van Session naar Profiel en een Categorie aanbeveling mee geven    
  LinkSessionToProfBrand.py
    -Script voor het koppellen van Session naar Profiel en een Brand aanbeveling mee geven    

Notulen folder
  Notulen week 1
    -Alle Notules van week 1
  Notulen week 2
    -Alle Notules van week 2
  Notulen week 3
    -Alle Notules van week 3
  
Website folder
  Run Huwebshop folder
    Klik mij 1st.bat
      -Eerste Exe voor het starten van de webshop
    Klik mij 2e.bat
      -tweede Exe voor het starten van de webshop  
  v1gp-master folder
      *Alle bestanden voor de webshop
      huw_recommended.py
        -Onze edit op de recommendation selection voor koppeling van postgress naar de webshop
  data_omzetten_bruikbare_table.py
    -Code voor correct overzetten van verschillende algoritme tabellen naar main recommendation

