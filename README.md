# Dome
Python DOM Element template

## Get dome
```bash
pip3 install dome
```

## Usage & Example
```
>>> import dome as D

>>> node = D.Html(
...             D.Head(
...                 D.Meta(Charset="utf-8"),
...                 D.Meta(HttpEquiv='X-UA-Compatible', Content='IE=edge,chrome=1'),
...                 D.Node('title')('This is Title')
...             ),
...             D.Body(
...                 D.Div(
...                     'div #1',
...                     Id='1st', Class='cs1',
...                 ), "\n",
...                 D.Div(
...                     'div #2',
...                     Id='2nd', Style="display: none",
...                 )
...             )
...         )

>>> print(node.dumps())
<html><head><meta charset="utf-8"/><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/><title>This is Title</title></head><body><div id="1st" class="cs1">div #1</div>
<div id="2nd" style="display: none">div #2</div></body></html>

>>> print(node.tag)
html
>>> print(node.attrs)
{}
>>> print(node)
[[[], [], ['This is Title']], [['div #1'], '\n', ['div #2']]]
>>> print(node.dumps())
<html><head><meta charset="utf-8"/><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/><title>This is Title</title></head><body><div id="1st" class="cs1">div #1</div>
<div id="2nd" style="display: none">div #2</div></body></html>

>>> print(node[0][1].tag)
meta
>>> print(node[0][1].attrs)
{'HttpEquiv': 'X-UA-Compatible', 'Content': 'IE=edge,chrome=1'}
>>> print(node[0][1])
[]
>>> print(node[0][1].dumps())
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>

>>> print(node[1][0].tag)
div
>>> print(node[1][0].attrs)
{'Id': '1st', 'Class': 'cs1'}
>>> print(node[1][0])
['div #1']
>>> print(node[1][0].dumps())
<div id="1st" class="cs1">div #1</div>
```
