from __future__ import annotations

from copy import copy

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin

from .config import FootnotesConfig


class FootnotesPlugin(BasePlugin[FootnotesConfig]):
    """Inject localized footnote backlink text."""

    def on_config(self, config: MkDocsConfig):
        if not self.config.enabled:
            return

        text = self.config.backlink_title
        if text is None:
            env = config.theme.get_env()
            template = env.get_template(
                "partials/language.html", globals={"config": config}
            )
            text = template.module.t("footnote.backlink")

        config.markdown_extensions = copy(config.markdown_extensions)
        config.mdx_configs = copy(config.mdx_configs)

        config.mdx_configs["footnotes"] = {
            **config.mdx_configs.get("footnotes", {}),
            "BACKLINK_TITLE": text,
        }

        if (
            "footnotes" not in config.markdown_extensions
            and "markdown.extensions.footnotes" not in config.markdown_extensions
        ):
            config.markdown_extensions.append("footnotes")
