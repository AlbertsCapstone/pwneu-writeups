### Category : Steganography
###### Write-ups by drewbyte
###### Flag : PWNEU{it's_yumi_y0u_got_!t_r!ght}
---

Download the 2 files provided by the PWNEU.

To find the hidden flag in the image we need a password or we need to bruteforce it but we have ``Text`` that contains a text ``th3-10wk3y-p@55w0rd``


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318180910.png" alt="">
 <br>

Use steghide to see the hidden text inside.

The command will be ``steghide extract -sf Artist.jpg``

<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240318181136.png" alt="">
 <br>