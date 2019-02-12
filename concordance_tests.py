import unittest
import mock
from concordance import *


class ConcordanceTests(unittest.TestCase):

    sent1 = "Hello world!  Hello I love you won't you tell me your name?  Here's a sentence with just a period " \
            "at the end.  Here is one with e.g. in the middle.  Here is one with etc. in the middle.  " \
            "Here is one with i.e. in the middle."

    sent2 = "Given an arbitrary text document written in English, write a program that will generate a concordance, " \
            "i.e. an alphabetical list of all word occurrences, labeled with word frequencies.  Bonus: label each " \
            "word with the sentence numbers in which each occurrence appeared."

    sent3 = ""

    def test_sentences(self):
        self.assertEqual(len(CreateConcordance.split_sentences(ConcordanceTests.sent1)), 6)
        self.assertEqual(len(CreateConcordance.split_sentences(ConcordanceTests.sent2)), 2)

    def test_for_exception_if_sentence_is_empty(self):
        with self.assertRaises(Exception):
            CreateConcordance.split_sentences("")

    def test_for_exception_if_file_does_not_exist(self):
        with self.assertRaises(Exception):
            CreateConcordance.concordance("bad.file.name")

    def test_for_exception_if_file_is_empty(self):
        with self.assertRaises(SystemExit) as exit_code:
            CreateConcordance.concordance("empty.file.lines.txt")
        self.assertEqual(exit_code.exception.code, 99)

    def test_for_exception_if_file_has_empty_lines(self):
        with self.assertRaises(SystemExit) as exit_code:
            CreateConcordance.concordance("empty.file.txt")
        self.assertEqual(exit_code.exception.code, 99)

    def test_count_words(self):
        sentences = CreateConcordance.split_sentences(ConcordanceTests.sent2)
        self.assertEqual(len(sentences), 2)
        concordance = CreateConcordance.count_words(sentences)
        self.assertTrue(len(concordance.keys()), 34)

        self.assertTrue('alphabetical' in concordance)
        val = concordance['alphabetical']
        total = val[0]
        lines = val[1:len(val)]
        self.assertTrue(total, 1)
        self.assertTrue(lines, [1])

        self.assertTrue('an' in concordance)
        val = concordance['an']
        total = val[0]
        lines = val[1:len(val)]
        self.assertTrue(total, 1)
        self.assertTrue(lines, [1, 1])

        self.assertTrue('frequencies' in concordance)
        val = concordance['frequencies']
        total = val[0]
        lines = val[1:len(val)]
        self.assertTrue(total, 1)
        self.assertTrue(lines, [1])
