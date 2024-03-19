### Category : Steganography
###### Write-ups by drewbyte
###### Flag : PWNEU{ST3GOS4URZ}
---

Download the file and use exiftool command to see the metadata of the image file.

![[Pasted image 20240318214820.png]]

Use CyberChef and its magic function to automatically decrypt.

![[Pasted image 20240318214802.png]]

Save the password and extract the 7zip.

![[Pasted image 20240318215742.png]]

And check the /Flag directory

![[Pasted image 20240318215909.png]]

Use spectrum analyzer to read the flag.

![[Pasted image 20240318221026.png]]

Convert it from base64.

![[Pasted image 20240318224808.png]]