from sphinx.builders.html import StandaloneHTMLBuilder


class DontBuildAdditionalPages(StandaloneHTMLBuilder):
    """Skip all the stuff around building additional pages, etc."""

    def finish(self) -> None:
        """Override StandaloneHTMLBuilder.finish."""

        self.finish_tasks.add_task(self.copy_image_files)
        self.finish_tasks.add_task(self.copy_download_files)
        self.finish_tasks.add_task(self.copy_static_files)
        self.finish_tasks.add_task(self.copy_extra_files)
        self.finish_tasks.add_task(self.write_buildinfo)
