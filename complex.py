
import math


class Complex:

    def __init__(self, real, img):
        """ constructor of a complex number.
        real is the real part
        img is the imaginary part
        """
        self.real = real
        self.img = img

    def module(self):
        """ return the module of the complex number
        """
        return math.sqrt(self.real*self.real + self.img*self.img)

    def phase(self):
        """ return the phase of the complex number
        """
        m = self.module()
        xcos = self.real/m
        phas = math.acos(xcos)
        return phas

    def __add__(self, x):
        """ return a complex number that is this complex + x
        """
        real = self.real+x.real
        img = self.img+x.img
        return Complex(real, img)

    def __sub__(self, x):
        """ return a complex number that is this complex - x
        """
        real = self.real - x.real
        img = self.img - x.img
        return Complex(real, img)

    def __mul__(self, x):
        """ return a complex number that is this complex * x
        """
        real = self.real*x.real - self.img*x.img
        img = self.real*x.img + self.img*x.real
        return Complex(real, img)

    def __str__(self):
        """ convert this complex into a string
        """
        if (self.img >= 0):
            s = str(self.real) + '+' + str(self.img) + 'j'
        else:
            s = str(self.real) + str(self.img) + 'j'
        return s

    def __repr__(self):
        return str(self)
