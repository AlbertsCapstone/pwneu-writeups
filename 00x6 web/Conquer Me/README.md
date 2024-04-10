### Category : Web
###### Write-ups by drewbyte
###### Flag : PWNEU{wvs@acunetix.com_4_192.168.0.26}
---

There's a lot of questions we need to answer in this challenge.
<br>
<br>

```
Can you find all of this we need to conquer it! It's on the deadline!!!

    What is the email of the website?
    How many zendesk email are there?
    What is the secret ip hidden inside the website?

URL: http://testphp.vulnweb.com
```
<br>
<br>

Use ``whatweb [domain]``

<br>
<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/con1.png" alt="">
 <br>
  <br>

First flag ``wvs@acunetix.com``

<br>
<br>

Use ``theHarvester -d acunetix.com -l 500 -b crtsh``

<br>
<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/con2.png" alt="">
 <br>
  <br>

Second flag ``4``
<br>
<br>

Use ``ffuf -w /usr/share/wordlists/dirb/common.txt -u http://testphp.vulnweb.com/FUZZ``

<br>
<br>
For directory busting but you can use any directory busting tool you preferred.

<br>
<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/con3.png" alt="">
 <br>
  <br>

 Navigate to ``/pictures``

<br>
<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/con4.png" alt="">
 <br>
  <br>

   Display the content of ``/ipaddresses.txt``

<br>
<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/con5.png" alt="">
 <br>
  <br>

  Last flag ``192.168.0.26``