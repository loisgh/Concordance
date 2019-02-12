import re


class CreateConcordance:

    @staticmethod
    def split_sentences(document):
        """
        This method returns a list of sentences.  A sentence is defined as
        a phrase which ends with a period, exclamation point or question mark
        or any of those wrapped in a quote.

        Please note that I am only removing the most common abbreviations.
        If I were truly implementing a full concordance, I would include a
        more exhaustive list of abbreviations.
        """
        if not len(document):
            raise Exception("The document length cannot be zero.")

        document_without_abbreviations = document.replace('i.e.', 'ie').\
            replace('e.g.', 'eg').\
            replace('etc.', 'etc')

        sentences = re.split(r' *[.?!][\'"\)\]]* *', document_without_abbreviations)
        if not len(sentences[-1]):
            sentences.pop()
        return sentences

    @staticmethod
    def count_words(sentences):

        concordance = dict()
        line = 1
        for sentence in sentences:
            if sentence.strip() not in ('', '  '):
                sent_list = sentence.lower().split(" ")
                for word in sent_list:
                    if word in concordance:
                        value = concordance[word]
                        value[0] += 1
                        value.append(line)
                    else:
                        value = [1, line]
                    concordance[word] = value
                line += 1

        return concordance

    @staticmethod
    def print_concordance(concordance):
        lines = 1
        for word, values in sorted(concordance.items()):
            num_occurances = values[1:len(values)]
            sent_nums = "{}:{}".format(values[0], ','.join(str(num) for num in num_occurances))
            sent_nums_display = '{' + sent_nums + '}'
            lines_str = "{}.".format(str(lines))
            print('{:<4s}{:<30s}{:<15s}'.format(lines_str, word, sent_nums_display))
            lines += 1

    @staticmethod
    def read_the_sentence(in_file_name):
        file_with_sentence = None
        try:
            file_with_sentence = open(in_file_name, "r")
            sentence = file_with_sentence.read()
            if not sentence.strip():
                exit(99)
            else:
                return sentence
        except FileNotFoundError:
            print("{} does not exist".format(in_file_name))
        finally:
            file_with_sentence.close()

    @staticmethod
    def concordance(in_file_name):
            sentence = CreateConcordance.read_the_sentence(in_file_name)
            sentences = CreateConcordance.split_sentences(sentence)
            concordance = CreateConcordance.count_words(sentences)
            CreateConcordance.print_concordance(concordance)
