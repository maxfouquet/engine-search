#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')