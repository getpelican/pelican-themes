#!/usr/bin/env python
import inflect

def ordinal(self):
    o = inflect.engine()
    return o.ordinal(self)  # 1 -> '1st'

