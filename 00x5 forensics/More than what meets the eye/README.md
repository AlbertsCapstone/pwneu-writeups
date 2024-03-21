### Category : Forensics
###### Write-ups by drewbyte
###### Flag : PWNEU{3A5Y_ENOU63}
---

Download the file and check the file.


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240321002358.png" alt="">
 <br>
 

Check the headers of File.png if it's real PNG 

The hex value of PNG file is 

```
89 50 4E 47 0D 0A 1A 0A
```

Using hex editor edit the header file.


<br>
<img src="https://github.com/drew-byte/pwneu-writeups/blob/main/00x8%20saved%20images/Pasted%20image%2020240321010452.png" alt="">
 <br>
 
 