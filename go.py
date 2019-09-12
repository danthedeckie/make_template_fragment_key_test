from old import make_template_fragment_key as OLD
from new import make_template_fragment_key as NEW
from sha import make_template_fragment_key as SHA
from blake2s import make_template_fragment_key as BLAKE

import timeit

NUM = 100000

new_versions = {
        "New (MD5)": "NEW",
        "New (SHA256)": "SHA",
        "New (Blake2s)": "BLAKE",
        }

def compare(vary_on=None, vary_display=None):
    print("\nTesting: vary_on = %s" % (vary_display or vary_on))
    test_code = '%s("hello", %s)'

    original_time = timeit.timeit(test_code % ('OLD', vary_on), globals=globals(), number=NUM)
    print("%s: %f (1.0)" % ( "Original", original_time))

    for title, func in new_versions.items():
        time = timeit.timeit(test_code % (func, vary_on), globals=globals(), number=NUM)
        print("%s: %f (%f x)" % (title, time, original_time / time))

compare()
compare(["Hello World", "This is some more text", 33])
compare(["Single String"])
compare([100, 201740820, 10820804, 12048023864, 1])
compare(["very long string" * 300], "very long string")
