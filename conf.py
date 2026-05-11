project = "Engineering Requirements Handbook"
author = "Abel RADENAC"
copyright = "2026, Abel RADENAC"

extensions = [
    "myst_parser",
    "sphinx_needs",
]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

master_doc = "index"
html_theme = "furo"

myst_enable_extensions = [
    "colon_fence",
]

needs_id_required = True
needs_id_regex = "^[A-Z]+_[0-9]{3}$"
needs_title_optional = False
needs_types = [
    {
        "directive": "req",
        "title": "Requirement",
        "prefix": "REQ_",
        "color": "#BFD8D2",
        "style": "node",
    },
]

needs_links = {
    "covers": {
        "incoming": "covered by",
        "outgoing": "covers",
        "schema": {
            "type": "array",
            "items": {"type": "string"},
        },
        "default": [],
    },
}
