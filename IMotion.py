#!/usr/bin/env python3
# coding: utf-8


class IMotion:

    def move(self, distance):
        raise NotImplementedError("Should have implemented this")

    def rotate(self, angle):
        raise NotImplementedError("Should have implemented this")