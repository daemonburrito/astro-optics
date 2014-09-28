# astro-optics Optics calculator in Python

Simple library for examining properties of optical systems commonly found in amateur astronomy.

## Usage

```python
>>> from astro_optics.lib import *
>>> system = System()
>>> system.camera = Canon20D()
>>> system.ota = OrionXT8()
>>> system.magnification
44.37601569801833
```

See `astro_optics.py` for examples of setting up concrete components.

## Project Status

Very much WIP, just written to save me a little time.

Just getting the shape of the API together. Requests, bug reports, and PRs welcome. Packaging help especially appreciated

## License

GPLv3
