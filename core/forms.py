from django import forms


class NumberForm(forms.Form):
    BASES = (("2", "Binario (base 2)"), ("8", "Octal (base 8)"), ("10", "Decimal (base 10)"), ("16", "Hexadecimal (base 16)"))

    number = forms.CharField(label="Número", max_length=64, strip=True, error_messages={"required": "Ingresa un número."}, widget=forms.TextInput(attrs={"placeholder": "Ej. 101101", "autocomplete": "off"}))
    base = forms.ChoiceField(label="Base de origen", choices=BASES)

    def clean_number(self):
        value = self.cleaned_data["number"]
        if not value:
            raise forms.ValidationError("Ingresa un número.")
        if value.startswith("-"):
            raise forms.ValidationError("No se permiten valores negativos.")
        try:
            base = int(self.data.get("base", "10"))
        except (TypeError, ValueError):
            raise forms.ValidationError("Selecciona una base válida: 2, 8, 10 o 16.")
        if base not in (2, 8, 10, 16):
            raise forms.ValidationError("Selecciona una base válida: 2, 8, 10 o 16.")
        try:
            parsed = int(value, base)
        except ValueError:
            labels = {2: "0 y 1", 8: "0 a 7", 10: "0 a 9", 16: "0 a 9 y A a F"}
            raise forms.ValidationError(f"Dígitos inválidos para base {base}; usa {labels[base]}.")
        if parsed > 65535:
            raise forms.ValidationError("El valor debe estar entre 0 y 65 535.")
        return parsed


class TextForm(forms.Form):
    text = forms.CharField(label="Texto", max_length=20, strip=False, required=True, error_messages={"required": "Ingresa un texto."}, widget=forms.TextInput(attrs={"placeholder": "Ej. España", "maxlength": 20}))

    def clean_text(self):
        value = self.cleaned_data["text"]
        if not value:
            raise forms.ValidationError("Ingresa un texto.")
        return value
