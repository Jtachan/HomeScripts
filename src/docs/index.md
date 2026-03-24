# Home-Utils

`home-utils` is a library containing python objects for general development.
All of these are intended to be used with debugging purposes.

To install the package, use the GitHub link:
```
pip install git+https://github.com/Jtachan/HomeScripts
```

`home-utils` does not need of any other third-party Python package for its installation. 

## Basic usage

Use the name `home-utils` to import the functionality of the package:

```python
from home-utils.decorators import *


@time_execution
def heavy_computation(n: int) -> list[int]:
    return [i**2 for i in range(n)]


heavy_computation(50_000)
# Function 'heavy_computation' executed in 0.002569 seconds
```

!!! hint
    Consider using a logger for a more custom printing.