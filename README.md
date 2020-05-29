This packages is inspired by Kaldi's utils from wsj recipe.

## utils_v3.get_stats
Recursively "walks" into data object
    and gives brief stats.
    e.g:
```
    >>> import numpy as np
    >>> import json
    >>> import utils_v3

    >>> data = [
        {'array_01':np.random.rand(3,4)},
        {'array_02':np.random.rand(3,1)}
    ]

    >>> stats = utils_v3.get_stats(data, 'data')

    >>> print(json.dumps(stats, indent=4))
    {
        "var_name": "data",
        "size": "0.078125 KB",
        "type": "<class 'list'>",
        "len": "2",
        "1st item": {
            "var_name": "data[0]",
            "size": "0.234375 KB",
            "type": "<class 'dict'>",
            "key_count": "1",
            "1st item": {
                "var_name": "data[0][array_01]",
                "size": "0.203125 KB",
                "type": "<class 'numpy.ndarray'>",
                "shape": "(3, 4)",
                "dtype": "float64"
            }
        }
    }
```