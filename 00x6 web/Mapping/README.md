### Category : Web
###### Write-ups by drewbyte
###### Flag : PWNEU{acuart_2_8}
---

Go to the URL and use an SQLi technique the ``'OR 1=1-- - 
or the default account which is ``test:test

To get the admin access and while doing that use burp to intercept the request and save the request.

![[Pasted image 20240318122635.png]]

Use sqlmap to find vulnerabilities and exploit it and this is the tool that we need to get the database.

The command will be : ``sqlmap -r [filename] --dbs

![[Pasted image 20240318122833.png]]

This is the first flag ``acuart

The second flag is  ``2

Now to get inside the database use this command ``sqlmap -r [filename] -D acuart --tables

![[Pasted image 20240318123042.png]]

The last flag will be ``8

