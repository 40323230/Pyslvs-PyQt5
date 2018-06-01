# -*- coding: utf-8 -*-

"""Solvespace format output function."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import List


class SlvsParser:
    
    """Use to read data from solvespace file format."""
    
    def __init__(self, file_name: str):
        """Open the file when initialize."""
        self.groups = []
        self.requests = []
        self.entities = []
        self.constraints = []
        dataset = {
            'AddGroup': self.groups,
            'AddParam': [],
            'AddRequest': self.requests,
            'AddEntity': self.entities,
            'AddConstraint': self.constraints,
        }
        args = {}
        with open(file_name, 'r', encoding="iso-8859-15") as f:
            if f.readline() != "±²³SolveSpaceREVa\n":
                return
            for line in f:
                if line == '\n':
                    args.clear()
                elif '=' in line:
                    attribute, data = line[:-1].split('=')
                    args[attribute] = data
                elif line[:-1] in dataset:
                    dataset[line[:-1]].append(args.copy())
    
    def isValid(self) -> bool:
        """Simple check whether if file is valid."""
        return bool(self.groups)
    
    def getGroups(self) -> List[str]:
        """Read and return group names."""
        groups = []
        for group in self.groups:
            #Number code and group name.
            groups.append((
                group['Group.h.v'],
                "".join(x for x in group['Group.name'] if x.isalnum() or (x in "._- "))
            ))
        return groups[1:]
    
    def parse(self, group: str) -> str:
        """Parse as PMKS expression for specified group.
        
        + Requests: Get all linkages.
            + Independence points will be ignored.
        + Constraint: Adjacency.
            + Collecting linkages for each point.
        + Entities: Get positions.
        """
        
        def int16(num: str) -> int:
            """Generate 16 bit interger."""
            return int(num, 16)
        
        #Requests: Get all linkages.
        requests = []
        for request in self.requests:
            if request['Request.group.v'] == group:
                #0x4 << 16 == 0x40000
                requests.append(int16(request['Request.h.v']) << 16)
        
        vlinks = {link: {link + 1, link + 2} for link in requests}
        vlinks[0] = set()
        
        #Constraint: Adjacency.
        #Grounded. Other linkages at least will greater than 4.
        for constraint in self.constraints:
            if constraint['Constraint.group.v'] != group:
                continue
            if constraint['Constraint.type'] == '20':
                now_replace = int16(constraint['Constraint.ptA.v'])
                for vlink in vlinks.values():
                    num = int16(constraint['Constraint.ptB.v'])
                    if num in vlink:
                        vlink.remove(num)
                        vlink.add(now_replace)
            elif constraint['Constraint.type'] == '31':
                vlinks[0].add(int16(constraint['Constraint.ptA.v']))
        
        pos = {}
        for vlink in vlinks.values():
            for point in vlink:
                if point not in pos:
                    pos[point] = None
        points = sorted(pos)
        
        #Entities: Get positions.
        for entity in self.entities:
            if entity['Entity.type'] == '2001':
                num = int16(entity['Entity.h.v'])
                if num in pos:
                    pos[num] = (
                        entity['Entity.actPoint.x'],
                        entity['Entity.actPoint.y'],
                    )
        
        #Rename link names.
        for i, name in enumerate(sorted(vlinks)):
            if i == 0:
                vlinks['ground'] = vlinks.pop(name)
            else:
                vlinks['link_{}'.format(i - 1)] = vlinks.pop(name)
        
        exprs = []
        for num in points:
            x, y = pos[num]
            links = [name for name, link in vlinks.items() if (num in link)]
            exprs.append("J[R, color[Green], P[{}, {}], L[{}]]".format(
                x, y, ", ".join(links)
            ))
        
        return "M[{}]".format(", ".join(exprs))