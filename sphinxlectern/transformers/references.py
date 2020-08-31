from urllib.parse import urlparse
from docutils import nodes
from sphinx.application import Sphinx


def apply_target_to_ext(app: Sphinx, doctree: nodes.document) -> None:
    for ref in doctree.traverse(nodes.reference):
        if "refuri" in ref:
            urlparts = urlparse(ref["refuri"])
            if urlparts.hostname and urlparts.hostname != app.config.hb_hostname:
                ref["target"] = "_blank"


def setup(app: Sphinx) -> None:
    app.add_config_value("hb_hostname", "", "html")
    app.connect("doctree-read", apply_target_to_ext)
