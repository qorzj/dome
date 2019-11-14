"""
Dom Element
"""
SCRIPT_MODE = 1
# __pragma__ ('skip')
SCRIPT_MODE = 1 - SCRIPT_MODE
# __pragma__ ('noskip')


if not SCRIPT_MODE:
    window = Zepto = ...
    import json


def tofixed(num, *, precision) -> str:
    if not SCRIPT_MODE:
        fmt = f'%.{precision}f'
        return fmt % num
    else:
        return num.toFixed(precision)


def switch_underscore(text: str):
    return text.rstrip('_').replace('_', '-')


class div:
    JSVOID = 'javascript:void(0)'

    def __init__(self, *children, tag: str = 'div', **attrs):
        self.children = children
        self.attrs = dict(attrs)
        self.tag = tag

    def _dump_head(self):
        sb = [self.tag]
        for key, value in self.attrs.items():
            if value is True:
                sb.append(' {}'.format(switch_underscore(key)))
            elif value is not None and value is not False:
                sb.append(' {}={}'.format(switch_underscore(key), repr(value)))
        return ''.join(sb)

    def __str__(self):
        sb = []
        if self.tag.lower() == 'html':
            sb.append('<!DOCTYPE html>\n')
        if len(self.children):
            sb.append('<{}>'.format(self._dump_head()))
            for child in self.children:
                if isinstance(child, str):
                    sb.append(child)
                else:
                    sb.append(str(child))
            sb.append('</{}>'.format(self.tag))
            return ''.join(sb)
        else:
            return '<{}/>'.format(self._dump_head())


def module(from_:str, import_:str, as_:str, path='/static/js'):
    """
    example: module(from_='home', import_='Action()', as_='home_action')
    """
    return div(
        f"import * as {from_} from '{path}/{from_}.js'; window.{as_} = {from_}.{import_};",
        tag='script', type='module'
    )


# Transcrypt only
class Kit:
    @staticmethod
    def ajax(method, url, data=None, headers=None, contentType=None, onsuccess=None, onerror=None, **kw):
        """
        :param onsuccess: function(data, status, xhr): when request succeeds
        :param onerror: function(xhr, errorType, error): timeout, parse error, or status code not in HTTP 2xx
        """
        if method: kw['type'] = method
        if url: kw['url'] = url
        if data is not None: kw['data'] = data
        if headers is not None: kw['headers'] = headers
        if contentType is not None: kw['contentType'] = contentType
        if onsuccess is not None: kw['success'] = onsuccess
        if onerror is not None: kw['error'] = onerror
        Zepto.ajax(kw)

    @staticmethod
    def request(*, method, url, data=None, json=None, headers=None, onsuccess=None, onerror=None):
        contentType = False
        if json is not None:
            data = Kit.stringify_json(json)
            contentType = 'application/json'
        elif isinstance(data, dict):
            data = Kit.param(data)
        Kit.ajax(method=method, url=url, data=data, headers=headers,
                 contentType=contentType, processData=False, onsuccess=onsuccess, onerror=onerror)

    @staticmethod
    def select(selector):
        return Zepto(selector)

    @staticmethod
    def onload(handler):
        return Zepto(handler)

    @staticmethod
    def param(data):
        if data is None:
            return None
        tmp = {}
        for k, v in data.items():
            if v is not None:
                tmp[k] = v
        return Zepto.param(tmp)

    @staticmethod
    def parse_json(text):
        if not SCRIPT_MODE:
            return json.loads(text)
        else:
            return Zepto.parseJSON(text)

    @staticmethod
    def stringify_json(data):
        if not SCRIPT_MODE:
            return json.dumps(data)
        else:
            return window.JSON.stringify(data)

    @staticmethod
    def print(obj):
        window.console.log(obj)

    @staticmethod
    def reload():
        window.location.reload()

    @staticmethod
    def goto(url):
        window.location.assign(url)

    @staticmethod
    def form_data(*selectors):
        """
        form = Kit.form_data('#ia', '#ib')
        form.append('key', value)
        """
        formData = eval('new FormData()')
        for selector in selectors:
            div = Kit.select(selector)
            if div.attr('type') == 'file':
                formData.append(div.attr('name'), div[0].files[0])
            else:
                formData.append(div.attr('name'), div.val())
        return formData
