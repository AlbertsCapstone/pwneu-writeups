### Category : Web
###### Write-ups by drewbyte
###### Flag : PWNEU{acuart_2_8}
---

Go to the URL and use an SQLi technique the ``'OR 1=1-- -``


or the default account which is ``test:test``


To get the admin access and while doing that use burp to intercept the request and save the request.


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318122635.png" alt="">
 <br>
 
 
Use sqlmap to find vulnerabilities and exploit it and this is the tool that we need to get the database.


The command will be : ``sqlmap -r [filename] --dbs``


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318122833.png" alt="">
 <br>
 
 
This is the first flag ``acuart``


The second flag is  ``2``


Now to get inside the database use this command ``sqlmap -r [filename] -D acuart --tables``


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318123042.png" alt="">
 <br>
 
 
The last flag will be ``8``

