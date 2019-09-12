# Comparing make_template_fragment_key speeds.

Output:
```
    Testing: vary_on = None
    Original: 0.304896 (1.0)
    New (MD5): 0.180153 (1.692427 x)
    New (SHA256): 0.187187 (1.628828 x)
    New (Blake2s): 0.108020 (2.822575 x)

    Testing: vary_on = ['Hello World', 'This is some more text', 33]
    Original: 1.488445 (1.0)
    New (MD5): 0.434238 (3.427719 x)
    New (SHA256): 0.439837 (3.384082 x)
    New (Blake2s): 0.312340 (4.765460 x)

    Testing: vary_on = ['Single String']
    Original: 0.736225 (1.0)
    New (MD5): 0.281357 (2.616693 x)
    New (SHA256): 0.282072 (2.610059 x)
    New (Blake2s): 0.177312 (4.152141 x)

    Testing: vary_on = [100, 201740820, 10820804, 12048023864, 1]
    Original: 1.480063 (1.0)
    New (MD5): 0.632621 (2.339574 x)
    New (SHA256): 0.640986 (2.309041 x)
    New (Blake2s): 0.448273 (3.301699 x)

    Testing: vary_on = very long string
    Original: 47.067326 (1.0)
    New (MD5): 1.337903 (35.179913 x)
    New (SHA256): 1.854285 (25.383011 x)
    New (Blake2s): 1.374788 (34.236063 x)
```

So the new version is faster - especially with long strings!
And the better hash functions perform well too, always beating the original
function.
