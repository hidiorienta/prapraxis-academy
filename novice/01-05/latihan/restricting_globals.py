import pickle
pickle.loads(b"cos\nsystem\n(S'echo hello world'\ntR.")


import builtins
import io
import pickle

safe_builtins = {
    'range',
    'complex',
    'set',
    'frozenset',
    'slice',
}

class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name in safe_builtins:
            return getattr(builtins, name)
        # Forbid everything else.
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" %(module, name))

def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()

restricted_loads(pickle.dumps([1, 2, range(15)]))

restricted_loads(b"cos\nsystem\n(S'echo hello world'\ntR.")

restricted_loads(b'cbuiltins\neval\n'
                 b'(S\'getattr(__import__("os"), "system")'
                 b'("echo hello world")\'\ntR.')
