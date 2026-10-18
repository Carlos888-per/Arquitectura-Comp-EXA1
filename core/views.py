from django.shortcuts import render

from .forms import NumberForm, TextForm


def home(request):
    number_form = NumberForm(request.POST or None, prefix="number")
    text_form = TextForm(request.POST or None, prefix="text")
    number_result = None
    text_result = None

    if request.method == "POST":
        if "number-submit" in request.POST and number_form.is_valid():
            value = number_form.cleaned_data["number"]
            bits = value.bit_length()
            byte_count = max(1, (bits + 7) // 8)
            number_result = {
                "decimal": str(value),
                "binary": format(value, f"0{byte_count * 8}b"),
                "octal": format(value, "o"),
                "hexadecimal": format(value, "X"),
                "bits": bits,
                "bytes": byte_count,
            }
        elif "text-submit" in request.POST and text_form.is_valid():
            text_result = [
                {
                    "character": character,
                    "decimal": ord(character),
                    "codepoint": f"U+{ord(character):04X}",
                    "hexadecimal": f"{ord(character):X}",
                    "utf8": " ".join(f"{byte:02X}" for byte in character.encode("utf-8")),
                }
                for character in text_form.cleaned_data["text"]
            ]

    return render(request, "core/home.html", {
        "number_form": number_form,
        "text_form": text_form,
        "number_result": number_result,
        "text_result": text_result,
    })
