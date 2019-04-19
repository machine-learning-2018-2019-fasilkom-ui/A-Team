import re


class TweetCleaner:
    def remove_punctuations_numbers_special_chars(self, str_input):
        return re.sub(r'[^a-zA-Z#]', ' ', str_input)

    def remove_handles(self, str_input):
        return re.sub(r'@[\w]*', ' ', str_input)

    def remove_unsignificant_words(self, str_input):
        return ' '.join(word for word in str_input.split() if len(word) > 3)

    def clean(self, str_input):
        return self.remove_unsignificant_words(
            self.remove_punctuations_numbers_special_chars(self.remove_handles(str_input)))