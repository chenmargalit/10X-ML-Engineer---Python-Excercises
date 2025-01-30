
from typing import Callable, List

import numpy as np

from automl.common.dataset import VwNamespaceMap

# Set a random seed for reproducibility
np.random.seed(42)


class TransformerDummy:
    def __init__(self, feature_name: str):
        self.transformed_column_names = [feature_name]
        self.feature_type = ''

    def is_active(self, columns_names: List[str]) -> bool:
        return True

    def init_namespace(self, vw_namespace_map: VwNamespaceMap, columns_names: List[str]) -> None:
        self.destination_letter = vw_namespace_map.map[self.transformed_column_names[0]]
        self.vw_str = "|" + self.destination_letter + " " + self.destination_letter + "DUMMY"

    def transform(self, row: str, vw_str_list: List[str]) -> None:
        vw_str_list.append(self.vw_str)

    def prelog_transform(self, row: str, prelog_row_list: List[str]) -> None:
        prelog_row_list.append("DUMMY")



class TransformerNoises:
    def __init__(self, output_feature_name: str, f: Callable):
        self.transformed_column_names = [output_feature_name]
        self.f = f
        self.feature_type = ''

    def is_active(self, columns_names: List[str]) -> bool:
        return True

    def init_namespace(self, vw_namespace_map: VwNamespaceMap, columns_names: List[str]) -> None:
        self.destination_letter = vw_namespace_map.map[self.transformed_column_names[0]]

    def transform(self, row: str, vw_str_list: List[str]) -> None:
        vw_str_list.append("|" + self.destination_letter + " " + self.destination_letter + str(self.f()))



def generate_gaussian_noise(scale: float = 0.1) -> float:
    """
    Generates a gaussian noise with an STD (=scale). This noise follows a normal distribution centered around 0.
    """
    return np.random.normal(loc=0, scale=scale)


def generate_uniform_noise(low: float = -0.1, high: float = 0.1) -> float:
    """
    Generates a uniform noise within a specified range (low to high).
    All values within this range have the same probability of being chosen.
    """
    return np.random.uniform(low=low, high=high)


def generate_salt_and_pepper_noise(p: float = 0.05) -> int:
    """
    Generates a noise where a certain percentage (p) of the signal is randomly set to either the max/min value
    (in this case 0 or 1).
    """
    return np.random.choice([0, 1], p=[1 - p, p])


def generate_quantization_noise() -> float:
    """
    Generates quantization noise by rounding a random value between 0 and 1 to one decimal place.
    This simulates the noise introduced when converting a continuous signal into a discrete one.
    """
    return np.round(np.random.rand() * 10) / 10


def generate_sparse_noise(p: float = 0.1) -> int:
    """
    Same as the salt and pepper noise, but with a different percentage
    """
    return np.random.choice([0, 1], p=[1 - p, p])


def generate_periodic_noise(amplitude: float = 0.1) -> float:
    """
    Generates periodic noise with a specified amplitude.
    It uses a sin wave with random frequency within the range [0, 4π], modulated by the provided amplitude.
    """
    return amplitude * np.sin(np.random.uniform(0, 4 * np.pi))


# Use this list to add wanted noises transformers to your offline research.
DUMMY_TRANSFORMER_LIST = [
                             TransformerDummy("dummy"),
                             TransformerNoises("gaussian_noise", generate_gaussian_noise),
                             TransformerNoises("uniform_noise", generate_uniform_noise),
                             TransformerNoises("salt_and_pepper_noise", generate_salt_and_pepper_noise),
                             TransformerNoises("quantization_noise", generate_quantization_noise),
                             TransformerNoises("sparse_noise", generate_sparse_noise),
                             TransformerNoises("periodic_noise", generate_periodic_noise)]



import unittest
from pathlib import Path

import numpy as np

if __name__ == '__main__':  # hack so we can run this test independently
    import sys
    sys.path.append("../..")


from automl.convert.dummy_transformers import TransformerDummy, TransformerNoises, generate_gaussian_noise, \
    generate_periodic_noise, generate_quantization_noise, generate_salt_and_pepper_noise, generate_sparse_noise, \
    generate_uniform_noise
from automl.common.dataset import VwNamespaceMap

tests_dir = Path(__file__).absolute().parent
project_dir = tests_dir.parents[1]
test_dir = project_dir / "search/tests/test_data/test_list"
work_dir = f"{test_dir}/instance_pool"
dataset_dir = f"{test_dir}/dataset"


def raise_exc(*args, **kwargs):
    Exception("This function should not have been called")


class TransformerNoisesTest(unittest.TestCase):
    np.random.seed(42)

    def test_transform_gaussian(self):
        # Adds random values from a normal distribution with mean zero
        columns_names = ["column_A", "column_B"]
        vw_namespace_map = VwNamespaceMap()
        vw_namespace_map.map = {"column_A": "A",
                                "column_B": "B",
                                "gaussian_noise": "C"}

        t = TransformerNoises("gaussian_noise", generate_gaussian_noise)
        self.assertTrue(t.is_active([]))

        t.init_namespace(vw_namespace_map, columns_names)

        vw_str_list = []
        t.transform(["A", "20"], vw_str_list)
        self.assertEqual(vw_str_list, ["|C C0.04967141530112327"])

    def test_transform_uniform(self):
        # Adds random values from a uniform distribution
        columns_names = ["column_A", "column_B"]
        vw_namespace_map = VwNamespaceMap()
        vw_namespace_map.map = {"column_A": "A",
                                "column_B": "B",
                                "uniform_noise": "C"}

        t = TransformerNoises("uniform_noise", generate_uniform_noise)
        self.assertTrue(t.is_active([]))

        t.init_namespace(vw_namespace_map, columns_names)

        vw_str_list = []
        t.transform(["A", "20"], vw_str_list)
        self.assertEqual(vw_str_list, ["|C C-0.08838327756636011"])

    def test_transform_salt_and_pepper(self):
        # Introduces random "spikes" of extremely high or low values
        columns_names = ["column_B"]
        vw_namespace_map = VwNamespaceMap()
        vw_namespace_map.map = {"column_A": "A",
                                "column_B": "B",
                                "salt_and_pepper_noise": "C"}

        t = TransformerNoises("salt_and_pepper_noise", generate_salt_and_pepper_noise)
        self.assertTrue(t.is_active([]))

        t.init_namespace(vw_namespace_map, columns_names)

        vw_str_list = []
        t.transform(["A", "20"], vw_str_list)
        self.assertEqual(vw_str_list, ["|C C0"])

    def test_transform_periodic(self):
        # Introduces periodic oscillations or patterns
        columns_names = ["column_A", "column_B"]
        vw_namespace_map = VwNamespaceMap()
        vw_namespace_map.map = {"column_A": "A",
                                "column_B": "B",
                                "periodic_noise": "C"}

        t = TransformerNoises("periodic_noise", generate_periodic_noise)
        self.assertTrue(t.is_active([]))

        t.init_namespace(vw_namespace_map, columns_names)

        vw_str_list = []
        t.transform(["A", "20"], vw_str_list)
        self.assertIn("0.022434495048755", vw_str_list[0])

    def test_transform_sparse(self):
        # Randomly sets a certain percentage of values to zero
        columns_names = ["column_A", "column_B"]
        vw_namespace_map = VwNamespaceMap()
        vw_namespace_map.map = {"column_A": "A",
                                "column_B": "B",
                                "sparse_noise": "C"}

        t = TransformerNoises("sparse_noise", generate_sparse_noise)
        self.assertTrue(t.is_active([]))

        t.init_namespace(vw_namespace_map, columns_names)

        vw_str_list = []
        t.transform(["A", "20"], vw_str_list)
        self.assertEqual(vw_str_list, ["|C C0"])

    def test_transform_quantization(self):
        #
        columns_names = ["column_A", "column_B"]
        vw_namespace_map = VwNamespaceMap()
        vw_namespace_map.map = {"column_A": "A",
                                "column_B": "B",
                                "quantization_noise": "C"}

        t = TransformerNoises("quantization_noise", generate_quantization_noise)
        self.assertTrue(t.is_active([]))

        t.init_namespace(vw_namespace_map, columns_names)

        vw_str_list = []
        t.transform(["A", "20"], vw_str_list)
        self.assertEqual(vw_str_list, ["|C C0.6"])


class TransformerDummyTest(unittest.TestCase):
    def test_is_active(self):
        t = TransformerDummy("dummy_feature")
        self.assertTrue(t.is_active([]))

    def test_transform1(self):
        columns_names = ["column_A", ]
        vw_namespace_map = VwNamespaceMap()
        vw_namespace_map.map = {"column_A": "A", "dummy_feature": "B"}

        t = TransformerDummy("dummy_feature")
        t.init_namespace(vw_namespace_map, columns_names)

        vw_str_list = []
        t.transform([], vw_str_list)
        self.assertEqual(vw_str_list, ["|B BDUMMY"])

