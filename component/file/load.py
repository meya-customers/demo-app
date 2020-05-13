from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from meya.util.template import from_template
from meya.util.template import to_template
from typing import List


@dataclass
class FileLoadComponent(Component):
    """
    file_path: relative file path from the app root including filename
    render: if True, renders using Meya's jinja2 templating
    context: dict used for jinja2 templating, if None defaults to app render context
    """

    file_path: str = element_field()
    template: bool = element_field(default=False)
    context: dict = element_field(default=None)

    @dataclass
    class Response:
        result: str = response_field()

    async def start(self) -> List[Entry]:
        with open(self.file_path, "r") as content_file:
            content = content_file.read()
        if self.template:
            if not self.context:
                self.context = await self.create_render_context()
            content = from_template(self.context, to_template(content))
        return self.respond(data=self.Response(result=content))
