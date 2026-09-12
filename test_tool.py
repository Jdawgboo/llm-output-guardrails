import unittest
from tool import check_output


class GuardrailTests(unittest.TestCase):
    def test_reports_textual_and_structural_violations(self):
        result = check_output("secret answer", forbidden=["secret"], max_characters=5, require_json=True)
        self.assertEqual(result, ["max_characters", "forbidden:secret", "invalid_json"])


if __name__ == "__main__":
    unittest.main()
