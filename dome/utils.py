import importlib
import html
import os
from types import ModuleType


def escape(s, quote=None):
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true (the default), the quotation mark
    characters, both double quote (") and single quote (') characters are also
    translated.
    """
    return html.escape(s, quote)


def rreload(module):
    """Recursively reload modules."""
    importlib.reload(module)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is ModuleType:
            rreload(attribute)


def buildjs(srcpath, distpath='static/js'):
    """
    example:
        buildjs('pages')
    """
    os.system(f'mkdir -p {distpath}')
    pagenames = [fname.rsplit('.')[0] for fname in os.listdir(srcpath) if fname.endswith('.py')]
    for pagename in pagenames:
        pyname = f'{srcpath}/{pagename}.py'
        jsname = f'{distpath}/{pagename}.js'
        if not os.path.isfile(jsname) or os.path.getmtime(jsname) < os.path.getmtime(pyname):
            cmd = f'transcrypt -b -k -n {srcpath}/{pagename} && mv {srcpath}/__target__/*.js {distpath}'
            os.system(cmd)