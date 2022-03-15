from src.mlpytemplate.cli.utils import lazy_module


def test_getattr():
    np = lazy_module.numpy
    assert np.sum(np.ones(42)) == 42.0


def test_lazy_module():
    np = lazy_module.LazyModule("numpy")
    assert np.sum(np.ones(42)) == 42.0
