
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Optional
from spatialdata import SpatialData
from spatialdata_io.readers.cosmx import cosmx, CosmxKeys


def cosmx_aux(
    fn: str | Path,
    dataset_id: Optional[str]=None,
    transcripts: bool = True,
    imread_kwargs: Mapping[str, Any] = MappingProxyType({}),
    image_models_kwargs: Mapping[str, Any] = MappingProxyType({}),
):
    """
    Read *Cosmx Nanostring* auxilary data

    This function reads the following files:

        - ``<dataset_id>_`{cx.COUNTS_SUFFIX!r}```: Counts matrix.
        - ``<dataset_id>_`{cx.METADATA_SUFFIX!r}```: Metadata file.
        - ``<dataset_id>_`{cx.FOV_SUFFIX!r}```: Field of view file.
        - ``{cx.OVERLAY_IMAGES_DIR!r}``: Directory containing the images.
        - ``{cx.COMPARTMENTLABELS_DIR!r}``: Directory containing the labels.
    """
    path = Path(path)
    

