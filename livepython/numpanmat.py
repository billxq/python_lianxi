#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/3 下午7:22
# @author: Bill
# @file: numpanmat.py

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(20,5))
df.to_csv('test.csv')
