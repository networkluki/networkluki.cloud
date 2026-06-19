import tempfile
import unittest
from pathlib import Path

import build


class RenderTemplateTests(unittest.TestCase):
    def test_render_template_replaces_and_escapes_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            template = Path(directory) / "page.html"
            template.write_text("<h1>{title}</h1>", encoding="utf-8")

            result = build.render_template(template, {"title": "A & <B>"})

        self.assertEqual(result, "<h1>A &amp; &lt;B&gt;</h1>")

    def test_render_template_reports_missing_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            template = Path(directory) / "page.html"
            template.write_text("<h1>{title}</h1>", encoding="utf-8")

            with self.assertRaises(SystemExit) as error:
                build.render_template(template, {})

        self.assertIn("Missing template value 'title'", str(error.exception))


if __name__ == "__main__":
    unittest.main()
