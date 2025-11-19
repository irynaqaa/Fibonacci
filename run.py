#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This script runs the Flask application
from app import app

if __name__ == '__main__':
    app.run(debug=True)