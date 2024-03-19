### Category : Steganography
###### Write-ups by drewbyte
###### Flag : PWNEU{it's_yumi_y0u_got_!t_r!ght}
---

Download the 2 files provided by the PWNEU.

To find the hidden flag in the image we need a password or we need to bruteforce it but we have ``Text`` that contains a text ``th3-10wk3y-p@55w0rd``

![[Pasted image 20240318180910.png]]

Use steghide to see the hidden text inside.

The command will be ``steghide extract -sf Artist.jpg``

![[Pasted image 20240318181136.png]]
