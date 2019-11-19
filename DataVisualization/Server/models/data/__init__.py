# -*- coding: utf-8 -*-
from .base import getObj, getItem, getItems, radius, load
# 下面调用数据处理类，会自动执行对象注册
from . import business

__all__ = ['getObj', 'getItem', 'getItems', 'radius', 'load']
