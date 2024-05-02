import re
class TokenClassifier:
    def __init__(self, user_input):
        self.user_input = user_input
        self.variable_pattern = re.compile(r'\b(?!abracadabra|vanish|wish|whisper|sparkle|prison|numpot|dotpot|alphapot|magif|magelse|wishweaver|illusioncycle|genie|lamp|in|is|limit|lightout|fadeaway|self|init|die|or|and|not)(?:(?<![\'\"])[a-zA-Z_][a-zA-Z_0-9]*)(?![\'\"])')
        self.dotpot_pattern=re.compile(r"[-+]?[0-9]*\.[0-9]+")
        self.numpot_pattern=re.compile(r'(?<![a-zA-Z_0-9.])(?:[-+]?\b[0-9]+\b)(?![0-9]*\.[0-9]+)')
        self.alphapot_pattern = re.compile(r'\'[a-zA-Z\,\.\:\s]+\'|\"[a-zA-Z\,\.\s\:]+\"')
        self.special_characters_pattern = re.compile(r"[(){}\[\]?^$#!&:_,](?=(?:[^']*'[^']*')*[^']*$)(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)")
        self.operators_pattern = re.compile(r"([+\-/*%><=]+|\*\*|==|!=|>=|<=|\+=|\-=|and|or|not)")
        self.keywords_pattern = re.compile(r'\b(?!["\'])(?:abracadabra|vanish|wish|whisper|sparkle|prison|numpot|dotpot|alphapot|magif|magelse|wishweaver|illusioncycle|genie|lamp|in|is|limit|lightout|fadeaway|self|init|die)(?!["\'])\b')
    def find_matches(self, pattern):
        return re.findall(pattern, self.user_input)

    def classify_and_print(self, matches, class_part):
        if matches:
            print("====================\n")
            print(f"MATCH {class_part.upper()} ARE:")
            for match in matches:
                print(f"TOKEN: {match}\tCLASS-PART: {class_part}")
            print(f"TOTAL {class_part.upper()} ARE: {len(matches)}")
        else:
            print("===============================")
            print(f"No {class_part.lower()} found")

    def classify_and_print_all(self):
        variable_matches = self.find_matches(self.variable_pattern)
        self.classify_and_print(variable_matches, "ID")
        
        dotpot_matches = self.find_matches(self.dotpot_pattern)
        self.classify_and_print(dotpot_matches, "DOTPOT")
        
        numpot_matches = self.find_matches(self.numpot_pattern)
        self.classify_and_print(numpot_matches, "NUMPOT")
        
        alphapot_matches = self.find_matches(self.alphapot_pattern)
        self.classify_and_print(alphapot_matches, "ALPHAPOT")
        
        special_characters_matches = self.find_matches(self.special_characters_pattern)
        self.classify_and_print(special_characters_matches, "SPECIAL CHARACTERS")

        operators_matches = self.find_matches(self.operators_pattern)
        self.classify_and_print(operators_matches, "OPERATORS")

        keywords_matches = self.find_matches(self.keywords_pattern)
        self.classify_and_print(keywords_matches, "KEYWORDS")


user_input = input("Enter a Code: ")
token_classifier = TokenClassifier(user_input)
token_classifier.classify_and_print_all()