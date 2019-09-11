# Comparing make_template_fragment_key speeds.

Output:
```
    Testing ['Hello World', 'This is some more text', 33]
    1.512041092
    0.42538428400000017

    Testing ['Single String']
    0.719327507
    0.27197983300000006

    Testing [100, 201740820, 10820804, 12048023864, 1]
    1.466242991
    0.609576391

    Testing None
    0.28710069500000035
    0.18360156199999977
```

So the new version is faster and uses SHA256 rather than MD5.
