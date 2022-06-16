# Usage

Currently, the `pygis` package only helps you install optional dependencies for [geemap](https://geemap.org/) and [leafmap](https://leafmap.org/) with only one command, making it easier to set up a conda environment for geospatial analysis and avoid dependency conflicts during installation. The `pygis` package itself does not have any meaningful functions yet. After installation, you can continue to the commonly used geospatial packages as usual. For example:

```python
import leafmap
m = leafmap.Map()
m
```
