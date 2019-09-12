from hashlib import blake2s


TEMPLATE_FRAGMENT_KEY_TEMPLATE = 'template.cache.%s.%s'


def make_template_fragment_key(fragment_name, vary_on=None):
    hasher = blake2s()

    if vary_on is not None:
        for arg in vary_on:
            hasher.update(str(arg).encode())
            hasher.update(b':')

    return TEMPLATE_FRAGMENT_KEY_TEMPLATE % (fragment_name, hasher.hexdigest())
