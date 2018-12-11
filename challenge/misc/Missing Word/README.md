## Missing Word

**Category :** Misc

**Points :** -

**Solves :** -

**Description :**
The flag is...

`wgmy{h3r3_1s_y0ur_XXXXXX_br0!}`

Not so fast. ;)

XXXXXX is the missing word (6 characters - regex [a-zA-Z]{6}) that you need to find.

The complete flag's SHA256 hash is `86775fe0718f57c5bcc3c32c198ece3e6a732406e3f32e3aa285059247da6652`

**Hint :**

**Flag :** wgmy{h3r3_1s_y0ur_pRiZEe_br0!}

**How to solve:**

Hashcat with GPU:
`hashcat -m1400 -a3 -1 ?l?u 86775fe0718f57c5bcc3c32c198ece3e6a732406e3f32e3aa285059247da6652 wgmy{h3r3_1s_y0ur_?1?1?1?1?1?1_br0\!} -O -w3 --gpu-temp-disable`

*note:*
1) Using my integrated Intel HD graphic, Hashcat speed was just ~700 kH/s, with e.t.a 7hours of running.
2) My Nvidia GTX980M clocked ~70,000 kH/s (e.t.a < 5mins) during the cracking process. If you got an awesome setup, this could be improved more. ;)
