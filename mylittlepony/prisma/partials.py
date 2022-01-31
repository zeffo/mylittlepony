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

# -- template partials.py.jinja --
from pydantic import BaseModel, Field, validator
from . import types, models, fields, enums



# users can modify relational types which are then namespaced to partials.
# so we have to import ourselves in order to resolve forward references
from . import partials


# fmt: on