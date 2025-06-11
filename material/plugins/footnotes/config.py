from mkdocs.config.config_options import Optional, Type
from mkdocs.config.base import Config


class FootnotesConfig(Config):
    """Footnotes plugin configuration."""

    enabled = Type(bool, default=True)
    backlink_title = Optional(Type(str))
