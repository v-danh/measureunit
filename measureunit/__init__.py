# # File: colorxcode/__init__.py

# try:
#     from importlib.metadata import version, PackageNotFoundError
# except ImportError:
#     # Cho các phiên bản Python cũ hơn
#     from importlib_metadata import version, PackageNotFoundError

# try:
#     __version__ = version("measureunit")
# except PackageNotFoundError:
#     __version__ = "unknown"

# version number

__version_info__ = (0, 0, 3)
__version__ = ".".join(str(i) for i in __version_info__)
# print(__version__)