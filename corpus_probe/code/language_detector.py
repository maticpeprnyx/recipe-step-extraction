from lingua import Language, LanguageDetectorBuilder
from open_file import open_bare
import sys

filepath = sys.argv[1]
text = open_bare(filepath)

languages = [Language.SLOVAK, Language.CZECH]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
language = detector.detect_language_of(text)
print(language)
