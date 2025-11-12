import string

def getMatrix(words):
    matrix = []

    def isVowel(c):
        return c.lower() in ['a', 'e', 'i', 'o', 'u']

    def countLetter(word):
        """Counts alphabetic letters."""
        return sum(1 for ch in word if ch.isalpha())

    def vowelRatio(word):
        """Ratio of vowels to total letters (0 if no letters)."""
        letters = [ch for ch in word if ch.isalpha()]
        if not letters:
            return 0
        vowels = sum(1 for ch in letters if isVowel(ch))
        return vowels / len(letters)

    def countDigits(word):
        """Counts the number of digits in the word."""
        return sum(1 for ch in word if ch.isdigit())

    def countUppercase(word):
        """Counts the number of uppercase letters."""
        return sum(1 for ch in word if ch.isupper())

    def countSymbols(word):
        """Counts non-alphanumeric symbols (e.g., !, @, #, .)."""
        return sum(1 for ch in word if ch in string.punctuation)
    
    def hasFilipinoPrefix(word):
        """Checks common Filipino prefixes."""
        prefixes = ['mag', 'ma', 'ka', 'pag', 'nag', 'um', 'ipa']
        lw = word.lower()
        return any(lw.startswith(p) for p in prefixes)
    
    def hasFilipinoSuffix(word):
        """Checks common Filipino suffixes."""
        suffixes = ['in', 'an', 'han', 'hin', 'um', 'ng']
        lw = word.lower()
        return any(lw.endswith(s) for s in suffixes)
    
    def hasEnglishPrefix(word):
        """Checks common English prefixes."""
        prefixes = ['un', 'dis', 're', 'pre']
        lw = word.lower()
        return any(lw.startswith(p) for p in prefixes)

    def hasEnglishSuffix(word):
        """Checks common English suffixes."""
        suffixes = ['ing', 'ed', 'tion', 'ness', 'ly']
        lw = word.lower()
        return any(lw.endswith(s) for s in suffixes)
    

    def isCapitalized(word):
        """Checks if first letter is capitalized (names or OTH)."""
        return len(word) > 0 and word[0].isupper()
    
    def hasEnglishLetterCombination(word):
        """Checks for common English letter combinations."""
        combinations = ['th', 'sh', 'ch', 'ph', 'qu']
        lw = word.lower()
        return any(comb in lw for comb in combinations)
    
    def hasEnglishLetter(word):
        """Checks for letters commonly found in English words."""
        letters = ['c', 'x', 'z', 'q', 'v', 'j']
        lw = word.lower()
        return any(letter in lw for letter in letters)

    for word in words:
        feats = []
        word = str(word)
    
        feats.append(countLetter(word))
        feats.append(vowelRatio(word))
        feats.append(int(hasFilipinoPrefix(word)))
        feats.append(int(hasFilipinoSuffix(word)))
        feats.append(int(hasEnglishPrefix(word)))
        feats.append(int(hasEnglishSuffix(word)))
        feats.append(int(isCapitalized(word)))
        feats.append(countDigits(word))
        feats.append(countUppercase(word))
        feats.append(countSymbols(word))
        feats.append(int(hasEnglishLetter(word)))
        feats.append(int(hasEnglishLetterCombination(word)))
        

        matrix.append(feats)

    return matrix

