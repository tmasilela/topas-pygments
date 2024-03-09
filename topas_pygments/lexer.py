from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ['TopasLexer', 'TextLexer']


class TopasLexer(RegexLexer):

    name = 'TOPAS'
    aliases = ['topas']
    filenames = ['*.txt']

    tokens = {
        'root': [
            (r'#.*$', Comment),
            (r'(?i)(includefile|inheritedvalue)', Keyword.Namespace),
            (r'^([bidus]v?c?)(:)', bygroups(Keyword.Type, Name)),
            (r'(?i)(ma|el|is|ge|gr|ph|so|sc|tf|ts|vr|rt)([/\w]*/)([\w]+)',
                bygroups(Name.Class, Name.Class, Name.Attribute)),
            (r'(?i)"(true|false|t|f|1|0)"', Keyword.Constant),
            (r'(?<!^b)"', String, 'string'),
            (r'(?<!\w)[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', Number),
            (r'[=+*-]', Operator),
            (r'.', Name),
        ],
        'string': [
            ('[^"]+', String),
            ('"', String, '#pop'),
        ]
    }


class PlainLexer(RegexLexer):

    name = 'Plain'
    aliases = ['plain']

    tokens = {
        'root': [
            (r'.', Name),
        ],
    }
