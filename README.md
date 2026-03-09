\# Reaalajalähedane objektituvastus laptopi kaameraga



Autor: Daniel 



\## Projekti eesmärk



Selle projekti eesmärk on kasutada laptopi sisseehitatud kaamerat ja tehisintellekti mudelit objektide tuvastamiseks reaalajas. Programm loeb kaamerapilti ning kasutab YOLOv8 objektituvastusmudelit, et leida kaadris olevaid objekte.



\## Kasutatud tehnoloogiad



Projektis kasutati järgmisi tehnoloogiaid:



\- Python

\- OpenCV

\- Ultralytics YOLOv8 mudel



\## Süsteemi arhitektuur



Süsteem töötab järgmiselt:



1\. Laptopi sisseehitatud kaamera edastab videopildi Python programmile.

2\. Programm töötleb iga kaadrit YOLOv8 objektituvastusmudeliga.

3\. Mudel tuvastab pildil olevad objektid ja märgib need kastidega.

4\. Tuvastatud objektid kuvatakse ekraanil koos tõenäosusega.



\## Programmi käivitamine



Kõigepealt tuleb paigaldada vajalikud paketid:



pip install -r requirements.txt



Seejärel saab programmi käivitada käsuga:



python main.py



\## Programmi kasutamine



Programmi käivitamisel avaneb kaamera aken.



Kasutaja saab kasutada järgmisi klahve:



\- \*\*s\*\* – salvestab kaadri koos tuvastatud objektidega

\- \*\*q\*\* – sulgeb programmi



Salvestatud pildid lisatakse kausta \*\*results\*\*.



\## Tulemused



Testimise käigus tuvastas süsteem edukalt mitmeid igapäevaesemeid. Näiteks tuvastati piltidel klaviatuur, pudel, tass ja apelsin. Näidispildid süsteemi tööst on lisatud kausta \*\*results\*\*.



\## Kasutatud mudel



Projektis kasutati eeltreenitud objektituvastusmudelit \*\*YOLOv8 nano (yolov8n.pt)\*\*, mis on kerge ja sobib reaalajalähedaseks objektituvastuseks.

