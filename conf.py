project = "Requirements"
author = "Your Team"
copyright = "2026, Your Team"

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
    {
        "directive": "spec",
        "title": "Specification",
        "prefix": "SPEC_",
        "color": "#FEDCD2",
        "style": "node",
    },
    {
        "directive": "test",
        "title": "Test",
        "prefix": "TEST_",
        "color": "#DF744A",
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
