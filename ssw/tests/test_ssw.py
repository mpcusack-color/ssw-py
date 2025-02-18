# -*- coding: utf-8 -*-
import unittest

try:
    from ssw import (
        SSW,
        force_align,
        format_force_align
    )
except:
    import _setup
    from ssw import (
        SSW,
        force_align,
        format_force_align
    )

class TestSSW(unittest.TestCase):

    def setUp(self):
        self.a = SSW()
        self.a.setRead(b"ACGT")

    def test_exact(self):
        a = self.a
        ref = b"TTTTACGTCCCCC"
        a.setReference(ref)
        res = a.align()
        # a.printResult(res)

    def test_deletion(self):
        a = self.a
        ref = b"TTTTACAGTCCCCC"
        a.setReference(ref)
        res = a.align()
        # a.printResult(res)

    def test_insertion_with_gap_open(self):
        a = self.a
        ref = b"TTTTACTCCCCC"
        a.setReference(ref)
        res = a.align(gap_open=3)
        # a.printResult(res)

    def test_insertion_with_no_gap_open_penalty(self):
        a = self.a
        ref = b"TTTTACTCCCCC"
        a.setReference(ref)
        res = a.align(gap_open=0)
        # a.printResult(res)

    def test_start_idx_test(self):
        a = self.a
        a.setRead("ACTG")
        a.setReference("ACTCACTG")
        res = a.align(start_idx=4)
        # a.printResult(res, start_idx=4)

    def test_forceAlign(self):
        read = b"ACTG"
        ref = b"TTTTCTGCCCCCACG"
        res = force_align(read, ref)
        format_force_align(read, ref, res)
