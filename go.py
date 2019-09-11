from old import make_template_fragment_key as OLD
from new import make_template_fragment_key as NEW

import timeit

NUM = 100000

STRS = ["Hello World", "This is some more text", 33]

print("Testing %s" % STRS)
print(timeit.timeit('OLD("hello", STRS)', globals=globals(), number=NUM))
print(timeit.timeit('NEW("hello", STRS)', globals=globals(), number=NUM))

STRS = ["Single String"]

print("Testing %s" % STRS)
print(timeit.timeit('OLD("hello", STRS)', globals=globals(), number=NUM))
print(timeit.timeit('NEW("hello", STRS)', globals=globals(), number=NUM))

STRS = [100, 201740820, 10820804, 12048023864, 1]

print("Testing %s" % STRS)
print(timeit.timeit('OLD("hello", STRS)', globals=globals(), number=NUM))
print(timeit.timeit('NEW("hello", STRS)', globals=globals(), number=NUM))

print("Testing None")
print(timeit.timeit('OLD("hello")', globals=globals(), number=NUM))
print(timeit.timeit('NEW("hello")', globals=globals(), number=NUM))


