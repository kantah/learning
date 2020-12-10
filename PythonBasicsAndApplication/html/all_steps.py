import requests

res = requests.get("https://docs.python.org/3.5/")  # функция get реализует http get запрос
print(res.status_code)
print(res.headers['Content-Type'])  # проверяем тип содержимого
# 200
# text/html
print(res.content)  # b'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n
#  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n<html xmlns="http://www.w3.org/1999/xhtml">\n
#  <head>\n    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />\n    <meta http-equiv="Content-Type"
#  content="text/html; charset=utf-8" /><title>3.5.10 Documentation</title>\n    <link rel="stylesheet"
#  href="_static/pydoctheme.css" type="text/css" />\n    <link rel="stylesheet" href="_static/pygments.css"
#  type="text/css" />\n    \n    <script type="text/javascript" id="documentation_options" data-url_root="./"
#  src="_static/documentation_options.js"></script>\n    <script type="text/javascript"
#  src="_static/jquery.js"></script>\n    <script type="text/javascript" src="_static/underscore.js"></script>\n
#  <script type="text/javascript" src="_static/doctools.js"></script>\n    <script async="async" type="text/javascript"
#  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>\n    \n
#  <script type="text/javascript" src="_static/sidebar.js"></script>\n    \n
#  <link rel="search" type="application/opensearchdescription+xml"\n
#  title="Search within Python 3.5.10 documentation"\n          href="_static/opensearch.xml"/>\n
#  <link rel="author" title="About these documents" href="about.html" />\n
#  <link rel="index" title="Index" href="genindex.html" />\n
#  <link rel="search" title="Search" href="search.html" />\n
#  <link rel="copyright" title="Copyright" href="copyright.html" />\n
#  <link rel="shortcut icon" type="image/png" href="_static/py.png" />\n
#  <link rel="canonical" href="https://docs.python.org/3/index.html" />\n    \n
#  <script type="text/javascript" src="_static/copybutton.js"></script>\n    \n    \n    \n \n\n  </head><body>\n  \n
#  <div class="related" role="navigation" aria-label="related navigation">\n      <h3>Navigation</h3>\n      <ul>\n
#  <li class="right" style="margin-right: 10px">\n          <a href="genindex.html" title="General Index"\n
#  accesskey="I">index</a></li>\n        <li class="right" >\n
#  <a href="py-modindex.html" title="Python Module Index"\n             >modules</a> |</li>\n
#  <li><img src="_static/py.png" alt=""\n                 style="vertical-align: middle; margin-top: -1px"/></li>\n
#  <li><a href="https://www.python.org/">Python</a> &#187;</li>\n        <li>\n
#  <a href="#">3.5.10 Documentation</a> &#187;\n        </li>\n\n    <li class="right">\n        \n\n
#  <div class="inline-search" style="display: none" role="search">\n
#  <form class="inline-search" action="search.html" method="get">\n
#  <input placeholder="Quick search" type="text" name="q" />\n          <input type="submit" value="Go" />\n
#  <input type="hidden" name="check_keywords" value="yes" />\n
#  <input type="hidden" name="area" value="default" />\n        </form>\n    </div>\n
#  <script type="text/javascript">$(\'.inline-search\').show(0);</script>\n         |\n    </li>\n\n      </ul>\n
#  </div>    \n\n    <div class="document">\n      <div class="documentwrapper">\n        <div class="bodywrapper">\n
#  <div class="body" role="main">\n            \n  <h1>Python 3.5.10 documentation</h1>\n  <p>\n
#  Welcome! This is the documentation for Python 3.5.10.\n  </p>\n
#  <p><strong>Parts of the documentation:</strong></p>\n  <table class="contentstable" align="center"><tr>\n
#  <td width="50%">\n
#  <p class="biglink"><a class="biglink" href="whatsnew/3.5.html">What\'s new in Python 3.5?</a><br/>\n
#  <span class="linkdescr"> or <a href="whatsnew/index.html">all "What\'s new" documents</a> since 2.0</span></p>\n
#  <p class="biglink"><a class="biglink" href="tutorial/index.html">Tutorial</a><br/>\n
#  <span class="linkdescr">start here</span></p>\n
#  <p class="biglink"><a class="biglink" href="library/index.html">Library Reference</a><br/>\n
#  <span class="linkdescr">keep this under your pillow</span></p>\n
#  <p class="biglink"><a class="biglink" href="reference/index.html">Language Reference</a><br/>\n
#  <span class="linkdescr">describes syntax and language elements</span></p>\n
#  <p class="biglink"><a class="biglink" href="using/index.html">Python Setup and Usage</a><br/>\n
#  <span class="linkdescr">how to use Python on different platforms</span></p>\n
#  <p class="biglink"><a class="biglink" href="howto/index.html">Python HOWTOs</a><br/>\n
#  <span class="linkdescr">in-depth documents on specific topics</span></p>\n    </td><td width="50%">\n
#  <p class="biglink"><a class="biglink" href="installing/index.html">Installing Python Modules</a><br/>\n
#  <span class="linkdescr">installing from the Python Package Index &amp; other sources</span></p>\n
#  <p class="biglink"><a class="biglink" href="distributing/index.html">Distributing Python Modules</a><br/>\n
#  <span class="linkdescr">publishing modules for installation by others</span></p>\n
#  <p class="biglink"><a class="biglink" href="extending/index.html">Extending and Embedding</a><br/>\n
#  <span class="linkdescr">tutorial for C/C++ programmers</span></p>\n
#  <p class="biglink"><a class="biglink" href="c-api/index.html">Python/C API</a><br/>\n
#  <span class="linkdescr">reference for C/C++ programmers</span></p>\n
#  <p class="biglink"><a class="biglink" href="faq/index.html">FAQs</a><br/>\n
#  <span class="linkdescr">frequently asked questions (with answers!)</span></p>\n    </td></tr>\n  </table>\n\n
#  <p><strong>Indices and tables:</strong></p>\n  <table class="contentstable" align="center"><tr>\n
#  <td width="50%">\n      <p class="biglink"><a class="biglink" href="py-modindex.html">Global Module Index</a><br/>\n
#  <span class="linkdescr">quick access to all modules</span></p>\n
#  <p class="biglink"><a class="biglink" href="genindex.html">General Index</a><br/>\n
#  <span class="linkdescr">all functions, classes, terms</span></p>\n
#  <p class="biglink"><a class="biglink" href="glossary.html">Glossary</a><br/>\n
#  <span class="linkdescr">the most important terms explained</span></p>\n    </td><td width="50%">\n
#  <p class="biglink"><a class="biglink" href="search.html">Search page</a><br/>\n
#  <span class="linkdescr">search this documentation</span></p>\n
#  <p class="biglink"><a class="biglink" href="contents.html">Complete Table of Contents</a><br/>\n
#  <span class="linkdescr">lists all sections and subsections</span></p>\n    </td></tr>\n  </table>\n\n
#  <p><strong>Meta information:</strong></p>\n  <table class="contentstable" align="center"><tr>\n    <td width="50%">\n
#  <p class="biglink"><a class="biglink" href="bugs.html">Reporting bugs</a></p>\n
#  <p class="biglink"><a class="biglink" href="about.html">About the documentation</a></p>\n    </td><td width="50%">\n
#  <p class="biglink"><a class="biglink" href="license.html">History and License of Python</a></p>\n
#  <p class="biglink"><a class="biglink" href="copyright.html">Copyright</a></p>\n    </td></tr>\n  </table>\n\n
#  </div>\n        </div>\n      </div>\n      <div class="sphinxsidebar"
#  role="navigation" aria-label="main navigation">\n
#  <div class="sphinxsidebarwrapper"><h3>Download</h3>\n<p><a href="download.html">Download these
#  documents</a></p>\n<h3>Docs for other versions</h3>\n<ul>\n
#  <li><a href="https://docs.python.org/3.8/">Python 3.8 (in development)</a></li>\n
#  <li><a href="https://docs.python.org/3.7/">Python 3.7 (stable)</a></li>\n
#  <li><a href="https://docs.python.org/3.6/">Python 3.6 (stable)</a></li>\n
#  <li><a href="https://docs.python.org/2.7/">Python 2.7 (stable)</a></li>\n
#  <li><a href="https://www.python.org/doc/versions/">Old versions</a></li>\n</ul>\n\n<h3>Other resources</h3>\n<ul>\n
#  \n  <li><a href="https://www.python.org/dev/peps/">PEP Index</a></li>\n
#  <li><a href="https://wiki.python.org/moin/BeginnersGuide">Beginner\'s Guide</a></li>\n
#  <li><a href="https://wiki.python.org/moin/PythonBooks">Book List</a></li>\n
#  <li><a href="https://www.python.org/doc/av/">Audio/Visual Talks</a></li>\n</ul>\n        </div>\n      </div>\n
#  <div class="clearer"></div>\n    </div>  \n    <div class="related" role="navigation"
#  aria-label="related navigation">\n      <h3>Navigation</h3>\n      <ul>\n
#  <li class="right" style="margin-right: 10px">\n          <a href="genindex.html" title="General Index"\n
#  >index</a></li>\n        <li class="right" >\n          <a href="py-modindex.html" title="Python Module Index"\n
#  >modules</a> |</li>\n        <li><img src="_static/py.png" alt=""\n
#  style="vertical-align: middle; margin-top: -1px"/></li>\n
#  <li><a href="https://www.python.org/">Python</a> &#187;</li>\n        <li>\n
#  <a href="#">3.5.10 Documentation</a> &#187;\n        </li>\n\n    <li class="right">\n        \n\n
#  <div class="inline-search" style="display: none" role="search">\n        <form class="inline-search"
#  action="search.html" method="get">\n          <input placeholder="Quick search" type="text" name="q" />\n
#  <input type="submit" value="Go" />\n          <input type="hidden" name="check_keywords" value="yes" />\n
#  <input type="hidden" name="area" value="default" />\n        </form>\n    </div>\n
#  <script type="text/javascript">$(\'.inline-search\').show(0);</script>\n         |\n    </li>\n\n      </ul>\n
#  </div>  \n    <div class="footer">\n    &copy; <a href="copyright.html">Copyright</a> 2001-2020,
#  Python Software Foundation.\n    <br />\n    The Python Software Foundation is a non-profit corporation.\n
#  <a href="https://www.python.org/psf/donations/">Please donate.</a>\n    <br />\n    Last updated on Sep 05, 2020.\n
#  <a href="bugs.html">Found a bug</a>?\n    <br />\n    Created using <a href="http://sphinx.pocoo.org/">Sphinx</a>
#  1.8.0.\n    </div>\n\n  </body>\n</html>'

# По умолчанию контент является бинарными данными, но если мы уверены, что данные, которые мы запрашиваем текстовые,
# можем использовать атрибут text
print(res.text)

#Если ресурсом является картинка:
res = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res.status_code)
print(res.headers['Content-Type'])  # проверяем тип содержимого
# 200
# image/png
print(res.content)  # получим бинарное представление кода:
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\
# x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x00\tpHYs\x00\x00\
# x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07tIME\x07\xd8\x04\x1b\x118!\x063\'^\x00\x00\x027IDAT8\xcbe\
# x93OHUA\x14\x87\xbf{\xdf\xb3w{"\x94\x10\xa5\xd1&hS\x8b6\xadZ\xb4\x10\x1emB*xP\xdb\xc0MQ\xae\xdd\x04A\x8b "\xda)mZH\
# x1b\x17\x91 F\x11EF\x98\x96\xb6\xb5\x88\xcc2\x15\xd4\xfc\xf3\xee\x9dy3g\xe6\xb6\xf0\xde\xbc\xea\x81\xc3\xc0\xcc\
# xf7;\xe77\xcc\x9c\x80]\xd1\xfd\xe0\xed3i\x9as\xde\x99v\xb1M\xc4\x18\xa4\xa9\xb4U\xfa\xf1\xc7\xfe\xeb}\x80\x06\\\xce\
# x87\xbb\x0bx\'\x17G\xfaj\xedN,\xceZ\xbcX\xbcwQ\x1a\xf8\x9b\xc01 *\xf2{\n8k9\x7fg\x18\'v;\xad\xcd\x8f;\x80j\x91/\
# x03t?|\x7f\xdb[{\\\xac\n\x8cN\x06\x8dj\x94E\xc7%g\x0c\xe1\xbeJ=M}\xceW\x80\xd2\x8e\x02\x97\x1f}x\xed\xc4v\xa5^\
# xc0{\x02\xa0Tn\x81J\x15\x82\x12N\xec\x0e\x87\xe9\\}\xc1\xdbX\x8bn\xdc\xaf\x9czw/\xf4\xdeumY5;mg\x99\x87\xa8\xcdQ\
# xc0"\t\xa1SQ\x19}\x03\xe8,\xe7\xa0/\x88|\xe1\xdei\xea\xb5\xd3\xf1\x9b\xa9\'}\x03\xcbS\xb5\x1a\xa2@\x12B\xaf\xda\
# x81\x8e\xf2\x0e\xb1\xb5\xe8\xc6\xda\xe8\xfc\xf8\xf0\xd3\xf9\xe9Wk\x80\x00)`\xe6\xc6j\'\x0f\xb6J/N\x81K@\x12\x80\
# xfde1M\xed\xc5FN,j}yhb\xa0wp\xe3\xe7\xad+\xad\xd1\x89K\xa1S\xd1\x7fXb\xf2\xee\x88\xc2\x8b\xd6@\x10:\x91\xd9\xdc\
# xfa\x9f\xc9\x97\xcf\xe3_\xbd=mU\x7f5\xf4EqR\x10\'\xe04I\x92N\x02&t:\xee\x17c\xb4\x13\xcb\xef\xa9\x91\xb5j\xe4.l\
# x0b\n\xa2\x82\x18`zF\xbf\x006\x83\xecgu\x00G\x81f\xbapm"\x87\x97\x16\xff\x0e\x95\xbcJ\xb7\x9c(p\n\x80o\xb3\xe6\
# xcb\xd9\x9e\xd5q\xe0G\x190\xc0"\xb0\x01\xa4\xc5n\x87\x0f\xb8:"\xe0,\x88%8\xb3\xd8\x054\x00\x95\xf1+!\xe0\xb3\x8d\
# x15`\xd5\xdbDoY-\xe4\xe9\xaf\xf84\xd5\xd9\x8b,\x00\xdf\xb35\xd93\x0b\x8d\x8d\xf5\xba\xd5\xf1gob\x9d;\xb1\xe3\x9d3c\
# x9f\xd4]\xc0\x02I\xd6\xd0\x02i\xc0\xde\x88\x80C\xc0\x11\xa0\rh\xc9\\nf]\x97\xb2\x91\x06\xe0\x1f\x01\xbf\xaf\xff\xfc\
# x8c\x00\x9a\x00\x00\x00\x00IEND\xaeB`\x82'

with open("python.png", "wb") as f:
    f.write(res.content)  # создаем файл, открываем его на запись в бианрном формате и записываем в него содержимое
# response content. При открытии файла увидим картинку

# Если мы знаем, какие имена принимает опрашиваемый ресурс, можно указать эти параметры в запросе
res = requests.get("https://yandex.ru/search/", params={"text": "stepik"})
print(res.status_code)
print(res.headers["Content-type"])
print(res.url)
# 200
# text/html; charset=utf-8
# https://yandex.ru/search/?text=stepik

res = requests.get("https://yandex.ru/search/", params={
                                                    "text": "stepik",
                                                    "test": "test1",
                                                    "name": "Name with spaces",
                                                    "list": ["test1", "test2"]})
print(res.status_code)
print(res.headers["Content-type"])
print(res.url)  # https://yandex.ru/search/?text=stepik&test=test1&name=Name+with+spaces&list=test1&list=test2
#  параметры передаются по следующим правилам: вначале стоит знак вопроса, пары ключ-значение передаются через =, между
# парами стоит амперсанд(&, бинарное "и"), вместо пробелов используется знак "+".
