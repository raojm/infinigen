import ctypes
import os
import sys
dirname, _ = os.path.split(os.path.abspath(__file__))
lib = ctypes.cdll.LoadLibrary("/home/raojm/miniconda3/envs/infinigen/lib/python3.10/site-packages/bpy/3.6/scripts/addons/flip_fluids_addon/pyfluid/lib/libblpyfluidrelease.so")
lib.str_print.argtypes = [ctypes.c_char_p]
lib.str_print.restype = None