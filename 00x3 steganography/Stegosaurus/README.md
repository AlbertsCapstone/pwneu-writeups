### Category : Steganography
###### Write-ups by drewbyte
###### Flag : PWNEU{ST3GOS4URZ}
---

Download the file and use exiftool command to see the metadata of the image file.


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318214820.png" alt="">
 <br>

 
Use CyberChef and its magic function to automatically decrypt.


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318214802.png" alt="">
 <br>


Save the password and extract the 7zip.


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318215742.png" alt="">
 <br>
And check the /Flag directory


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318215909.png" alt="">
 <br>


Use spectrum analyzer to read the flag.


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318221026.png" alt="">
 <br>


Convert it from base64.


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318224808.png" alt="">
 <br>