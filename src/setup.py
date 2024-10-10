from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="rust_python_integration",
    version="0.1.0",
    rust_extensions=[RustExtension("rust_python_integration.rust_python_integration", binding="pyo3")],
    packages=["rust_python_integration"],
    zip_safe=False,
)
