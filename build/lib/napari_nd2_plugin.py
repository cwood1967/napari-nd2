from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from nd2reader import ND2Reader
import numpy as np

from napari_plugin_engine import napari_hook_implementation

PathLike = Union[str, List[str]]
LayerData = Union[Tuple[Any], Tuple[Any, Dict], Tuple[Any, Dict, str]]
ReaderFunction = Callable[[PathLike], List[LayerData]]

def nd2_reader(path: str) -> List[LayerData]:
    ndx = ND2Reader(path)
    sizes = ndx.sizes
    
    if 't' not in sizes:
        sizes['t'] = 1
    if 'z' not in sizes:
        sizes['z'] = 1
    if 'c' not in sizes:
        sizes['c'] = 1

    ndx.bundle_axes = 'zcyx'
    ndx.iter_axes = 't'
    n = len(ndx)

    shape = (sizes['t'], sizes['z'], sizes['c'], sizes['y'], sizes['x'])
    image  = np.zeros(shape, dtype=np.float32)

    for i in range(n):
        image[i] = ndx.get_frame(i)

    params = {
        "channel_axis": 2,
        "name":"My ND2 image",
    }

    return [(image, params)]


@napari_hook_implementation
def napari_get_reader(path: Union[str, List[str]]) -> Optional[ReaderFunction]:
    if isinstance(path, str) and path.endswith('.nd2'):
        return nd2_reader



