## AumWAF 2.0

**Category :** Web

**Points :** -

**Solves :** -

**Description :**

AumWAF is back! with a new detection engine and a bug bounty program.  
link: [http://waf2.wargames.my](http://waf2.wargames.my)

```php
    preg_match('/[\/\\\\]/', $input) ||
    preg_match('/(and|or|null|not)/i', $input) ||
    preg_match('/(\||=|&|!|>|<)/', $input) ||
    preg_match('/(union|select|from|where)/i', $input) ||
    preg_match('/(group|order|group_concat|concat|having|limit)/i', $input) ||
    preg_match('/(if|like|substr|substring|mid)/i', $input) ||
    preg_match('/(into|file|case)/i', $input) ||
    preg_match('/(--|#|\/\*)/', $input) ||
    preg_match('/%[0-9a-fA-F]{2}/', $input) ||
    preg_match('/\s+/', $input) ||
    preg_match('/(\'|")/', $input)
```

**Hint :**

- are you blind?


