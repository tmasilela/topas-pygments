from pygments.style import Style
from pygments.token import *


class TopasStyle(Style):

    default_style = "#f8f8f2"
    background_color = "#272822"
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Text:                      "nobold #f8f8f2", # class:  ''
        Whitespace:                "",        # class: 'w'
        Error:                     "nobold #960050 bg:#1e0010", # class: 'err'
        Other:                     "",        # class 'x'

        Comment:                   "nobold #75715e", # class: 'c'
        Comment.Multiline:         "",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   "nobold #66d9ef", # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         "nobold #f92672", # class: 'kn'
        Keyword.Pseudo:            "",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              "nobold",  # class: 'kt'

        Operator:                  "nobold #f92672", # class: 'o'
        Operator.Word:             "",        # class: 'ow' - like keywords

        Punctuation:               "nobold #f8f8f2", # class: 'p'

        Name:                      "nobold #f8f8f2", # class: 'n'
        Name.Attribute:            "nobold #a6e22e", # class: 'na' - to be revised
        Name.Builtin:              "",        # class: 'nb'
        Name.Builtin.Pseudo:       "",        # class: 'bp'
        Name.Class:                "nobold #fd971f", # class: 'nc' - to be revised
        Name.Constant:             "nobold #66d9ef", # class: 'no' - to be revised
        Name.Decorator:            "nobold #a6e22e", # class: 'nd' - to be revised
        Name.Entity:               "",        # class: 'ni'
        Name.Exception:            "nobold #a6e22e", # class: 'ne'
        Name.Function:             "nobold #a6e22e", # class: 'nf'
        Name.Property:             "",        # class: 'py'
        Name.Label:                "",        # class: 'nl'
        Name.Namespace:            "",        # class: 'nn' - to be revised
        Name.Other:                "nobold #a6e22e", # class: 'nx'
        Name.Tag:                  "nobold #f92672", # class: 'nt' - like a keyword
        Name.Variable:             "",        # class: 'nv' - to be revised
        Name.Variable.Class:       "",        # class: 'vc' - to be revised
        Name.Variable.Global:      "",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "",        # class: 'vi' - to be revised

        Number:                    "nobold #ae81ff", # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   "#nobold ae81ff", # class: 'l'
        Literal.Date:              "#nobold e6db74", # class: 'ld'

        String:                    "#nobold e6db74", # class: 's'
        String.Backtick:           "",        # class: 'sb'
        String.Char:               "",        # class: 'sc'
        String.Doc:                "",        # class: 'sd' - like a comment
        String.Double:             "",        # class: 's2'
        String.Escape:             "#nobold ae81ff", # class: 'se'
        String.Heredoc:            "",        # class: 'sh'
        String.Interpol:           "",        # class: 'si'
        String.Other:              "",        # class: 'sx'
        String.Regex:              "",        # class: 'sr'
        String.Single:             "",        # class: 's1'
        String.Symbol:             "",        # class: 'ss'

        Generic:                   "",        # class: 'g'
        Generic.Deleted:           "#nobold f92672", # class: 'gd',
        Generic.Emph:              "nobold",  # class: 'ge'
        Generic.Error:             "",        # class: 'gr'
        Generic.Heading:           "",        # class: 'gh'
        Generic.Inserted:          "nobold #a6e22e", # class: 'gi'
        Generic.Output:            "",        # class: 'go'
        Generic.Prompt:            "",        # class: 'gp'
        Generic.Strong:            "nobold",  # class: 'gs'
        Generic.Subheading:        "nobold #75715e", # class: 'gu'
        Generic.Traceback:         "",        # class: 'gt'
    }
