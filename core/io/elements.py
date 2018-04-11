# -*- coding: utf-8 -*-

"""Simple class expression of Pyslvs."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from math import sqrt, degrees, atan2
from core.graphics import colorQt
from typing import Tuple

class VPoint:
    
    """Joints type."""
    
    __slots__ = (
        '__links',
        '__type',
        '__angle',
        '__color',
        '__x',
        '__y',
        '__c'
    )
    Jtype = ('R', 'P', 'RP')
    
    def __init__(self,
        links: str ='',
        type: int =0,
        angle: float =0.,
        color: str ='Red',
        x: float =0.,
        y: float =0.
    ):
        self.__set(links, type, angle, color, x, y)
        if (self.type == 1) or (self.type == 2):
            self.__c = tuple((self.x, self.y) for i in range(len(self.links)))
        else:
            self.__c = ((self.x, self.y),)
    
    @property
    def links(self):
        return self.__links
    
    def setLinks(self, links: str):
        self.__links = tuple(filter(lambda a: a!='', links.split(',')))
    
    @property
    def type(self) -> int:
        return self.__type
    
    @property
    def typeSTR(self) -> str:
        return self.Jtype[self.type]
    
    def setType(self, type: int):
        self.__type = type
    
    @property
    def angle(self) -> float:
        return self.__angle
    
    def setAngle(self, angle: float):
        self.__angle = angle
    
    @property
    def color(self) -> 'QColor':
        return colorQt(self.__color)
    
    @property
    def colorSTR(self) -> str:
        return self.__color
    
    def setColor(self, color: str):
        self.__color = color
    
    @property
    def x(self) -> float:
        return self.__x
    
    @property
    def y(self) -> float:
        return self.__y
    
    def setCoordinate(self, x: float, y: float):
        self.__x = x
        self.__y = y
    
    @property
    def cx(self) -> float:
        return self.__c[0][0]
    
    @property
    def cy(self) -> float:
        return self.__c[0][1]
    
    @property
    def c(self) -> Tuple[Tuple[float, float], ...]:
        """Get the coordinates of all pin."""
        return self.__c
    
    def __set(self, links, type, angle, color, x, y):
        self.__links = tuple(filter(lambda a: a!='', links.split(',')))
        self.__type = type
        self.__angle = angle
        self.__color = color
        self.__x = x
        self.__y = y
    
    def move(self, *coordinates):
        self.__c = tuple(coordinates)
    
    def distance(self, p):
        x = self.x - p.x
        y = self.y - p.y
        return round(sqrt(x*x + y*y), 4)
    
    def slopeAngle(self, p):
        return round(degrees(atan2(p.y-self.y, p.x-self.x)), 4)
    
    @property
    def expr(self):
        return "J[{}, color[{}], P[{}], L[{}]]".format(
            "{}, A[{}]".format(self.typeSTR, self.angle)
            if self.typeSTR!='R' else 'R',
            self.colorSTR,
            "{}, {}".format(self.x, self.y),
            ", ".join(l for l in self.links)
        )
    
    def __repr__(self):
        return "VPoint({p.links}, {p.type}, {p.angle}, {p.c})".format(p=self)

class VLink:
    
    """Linkages type."""
    
    __slots__ = ('__name', '__color', '__points')
    
    def __init__(self, name: str, color: str, points: Tuple[int, ...]):
        self.__set(name, color, points)
    
    @property
    def name(self) -> str:
        return self.__name
    
    def setName(self, name: str):
        self.__name = name
    
    @property
    def color(self) -> 'QColor':
        return colorQt(self.__color)
    
    @property
    def colorSTR(self) -> str:
        return self.__color
    
    def setColor(self, color: str):
        self.__color = color
    
    @property
    def points(self) -> Tuple[int, ...]:
        return self.__points
    
    def setPoints(self, points: Tuple[int, ...]):
        self.__points = points
    
    def __set(self, name, color, points):
        self.__name = name
        self.__color = color
        self.__points = points
    
    def __contains__(self, point):
        return point in self.points
    
    def __repr__(self):
        return "VLink('{l.name}', {l.points})".format(l=self)
