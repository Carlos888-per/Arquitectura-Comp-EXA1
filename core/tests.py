from django.test import TestCase

from .forms import NumberForm, TextForm


class NumberFormTests(TestCase):
    def test_binary_value_is_parsed(self):
        form = NumberForm({"number": "101101", "base": "2"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["number"], 45)

    def test_octal_value_is_parsed(self):
        form = NumberForm({"number": "17", "base": "8"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["number"], 15)

    def test_hex_value_is_parsed_case_insensitively(self):
        form = NumberForm({"number": "ff", "base": "16"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["number"], 255)

    def test_digit_invalid_for_selected_base(self):
        form = NumberForm({"number": "102", "base": "2"})
        self.assertFalse(form.is_valid())
        self.assertIn("Dígitos inválidos", str(form.errors))

    def test_value_above_uint16_is_rejected(self):
        form = NumberForm({"number": "65536", "base": "10"})
        self.assertFalse(form.is_valid())
        self.assertIn("65 535", str(form.errors))

    def test_negative_value_is_rejected(self):
        form = NumberForm({"number": "-1", "base": "10"})
        self.assertFalse(form.is_valid())
        self.assertIn("negativos", str(form.errors))

    def test_empty_number_has_clear_error(self):
        form = NumberForm({"number": "", "base": "10"})
        self.assertFalse(form.is_valid())
        self.assertIn("Ingresa un número", str(form.errors))


class TextFormTests(TestCase):
    def test_text_is_limited_to_twenty_characters(self):
        form = TextForm({"text": "a" * 21})
        self.assertFalse(form.is_valid())

    def test_empty_text_has_clear_error(self):
        form = TextForm({"text": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("Ingresa un texto", str(form.errors))


class AnalyzerViewTests(TestCase):
    def test_conversion_page_pads_binary_to_whole_byte(self):
        response = self.client.post("/", {"number-number": "1", "number-base": "10", "number-submit": "1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "00000001")
        self.assertContains(response, "1 bits")

    def test_zero_uses_no_significant_bits_but_one_storage_byte(self):
        response = self.client.post("/", {"number-number": "0", "number-base": "10", "number-submit": "1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "0 bits")
        self.assertContains(response, "00000000")

    def test_text_page_shows_utf8_bytes_for_enye(self):
        response = self.client.post("/", {"text-text": "ñ", "text-submit": "1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "U+00F1")
        self.assertContains(response, "C3 B1")
