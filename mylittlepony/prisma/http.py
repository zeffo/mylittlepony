# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pylint: disable=all
# pyright: reportUnusedImport=false
# fmt: off

# global imports for type checking
import sys
import datetime
from typing import (
    TYPE_CHECKING,
    Optional,
    Iterable,
    Iterator,
    Callable,
    Generic,
    Mapping,
    Tuple,
    Union,
    List,
    Dict,
    Type,
    Any,
    Set,
    overload,
    cast,
)
from typing_extensions import TypedDict, Literal

# -- template http.py.jinja --
from ._async_http import (
    HTTP as HTTP,
    Response as Response,
    client as client,
)