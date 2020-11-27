##########################
# Imports
##########################


# Built-in
from hashlib import sha224

# Local
from few_shots_clf.utils import compute_catalog_fingerprint


##########################
# Function
##########################


def compute_fingerprint(catalog_path, config):
    """[summary]

    Args:
        catalog_path ([type]): [description]
        config ([type]): [description]

    Returns:
        [type]: [description]
    """
    # Catalog fingerprint
    catalog_fingerprint = compute_catalog_fingerprint(catalog_path,
                                                      verbose=config.verbose)

    # Config fingerprint
    config_fingerprint = compute_config_fingerprint(config)

    # Final fingerprint
    fingerprint = f"{catalog_fingerprint}{config_fingerprint}"
    fingerprint = sha224(str.encode(fingerprint)).hexdigest()

    return fingerprint


def compute_config_fingerprint(config):
    """[summary]

    Args:
        config ([type]): [description]

    Returns:
        [type]: [description]
    """
    # Init config fingerprint
    config_fingerprint = ""

    # Add feature_descriptor
    config_fingerprint = f"{config_fingerprint}{str(config.feature_descriptor.getDefaultName())}"

    # Add feature_dimension
    config_fingerprint = f"{config_fingerprint}{config.feature_dimension}"

    # Add image_size
    config_fingerprint = f"{config_fingerprint}{config.image_size}"

    # Add keypoint_stride
    config_fingerprint = f"{config_fingerprint}{config.keypoint_stride}"

    # Add keypoint_sizes
    config_fingerprint = f"{config_fingerprint}{str(config.keypoint_sizes)}"

    # Add matcher_distance
    config_fingerprint = f"{config_fingerprint}{config.matcher_distance}"

    # Add matcher_n_trees
    config_fingerprint = f"{config_fingerprint}{config.matcher_n_trees}"

    return config_fingerprint
