import math

# Basic Operations
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b 

# Advanced Operations

def power(a, b):
    return math.pow(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("Error: Cannot take square root of negative number")
    return math.sqrt(a)

# Trigonometric Functions
def sine(angle):
    return math.sin(math.radians(angle))

def arcsine(angle):
    return math.asin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def arccosine(angle):
    return math.acos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

def arctangent(angle):
    return math.atan(math.radians(angle))
