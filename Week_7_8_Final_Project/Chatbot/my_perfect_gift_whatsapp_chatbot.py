from ai import call_gpt


CATALOG_FILE = "catalogo_real_mi_regalo_perfecto.csv"


def run_one_session():
    language = choose_language()
    print_intro(language)

    catalog = load_catalog(CATALOG_FILE)

    if len(catalog) == 0:
        if language == "es":
            print(
                "⚠️ *No pude cargar el catálogo.*\n\n"
                "Sube el archivo CSV con este nombre exacto:\n\n"
                + CATALOG_FILE
            )
        else:
            print(
                "⚠️ *I could not load the catalog.*\n\n"
                "Upload the CSV file with this exact name:\n\n"
                + CATALOG_FILE
            )
        return

    answers = ask_five_questions(language)
    best_products = find_best_products(catalog, answers)

    if language == "es":
        print(
            "✨ *¡Gracias!*\n\n"
            "Nuestra IA está revisando el catálogo real para encontrar "
            "las mejores ideas para tu regalo personalizado.\n\n"
            "Esto tomará solo un momento..."
        )
    else:
        print(
            "✨ *Thank you!*\n\n"
            "Our AI is checking the real catalog to find the best ideas "
            "for your personalized gift.\n\n"
            "This will only take a moment..."
        )

    prompt = build_gpt_prompt(language, answers, best_products)
    response = call_gpt(prompt)

    print(response)

    return ask_return_to_main_menu(language)


def main():
    restart = True

    while restart:
        restart = run_one_session()


def choose_language():
    message = (
        "🌎 *Welcome / Bienvenido*\n\n"
        "Please choose your language:\n"
        "Por favor elige tu idioma:\n\n"
        "A. 🇺🇸 English\n"
        "B. 🇪🇸 Español\n\n"
        "Type here / escribe aqui:"
    )

    choice = input(message)
    choice = clean_text(choice)

    if choice == "b" or "espanol" in choice or "spanish" in choice:
        return "es"

    return "en"


def ask_return_to_main_menu(language):
    if language == "es":
        message = (
            "\n🏠 *¿Deseas regresar al menú principal?*\n\n"
            "A. Sí, buscar otro regalo\n"
            "B. No, finalizar\n\n"
            "Escribe la letra de tu opción: "
        )
        error = "Por favor escribe A para regresar al menú principal o B para finalizar."
    else:
        message = (
            "\n🏠 *Would you like to return to the main menu?*\n\n"
            "A. Yes, find another gift\n"
            "B. No, finish\n\n"
            "Type the letter of your choice: "
        )
        error = "Please type A to return to the main menu or B to finish."

    choice = clean_text(input(message))

    while choice not in ("a", "b"):
        print(error)
        choice = clean_text(input(message))

    return choice == "a"


def print_intro(language):
    if language == "es":
        message = (
            "🎁 *MY PERFECT GIFT*\n"
            "Asistente de regalos personalizados para WhatsApp\n\n"
            "¡Hola! 👋\n\n"
            "Creamos productos personalizados como tazas, termos, "
            "llaveros, sublimación, vinil, DTF y mucho más.\n\n"
            "Este chatbot te ayudará a encontrar ideas para tu regalo "
            "personalizado usando nuestro catálogo real.\n\n"
            "📄 *¿De dónde salen los productos?*\n"
            "Los productos se toman de un archivo CSV subido al IDE con "
            "este nombre exacto:\n\n"
            + CATALOG_FILE + "\n\n"
            "Ese CSV funciona como una pequeña base de datos del catálogo. "
            "Python lo lee, revisa los productos disponibles y filtra las "
            "mejores opciones según tus respuestas.\n\n"
            "🤖 *¿Cómo se usa GPT?*\n"
            "Después de filtrar el catálogo, el programa llama a GPT para "
            "crear una recomendación más clara, personalizada y lista para "
            "enviar por WhatsApp.\n\n"
            "Te haré solamente 5 preguntas rápidas."
        )
    else:
        message = (
            "🎁 *MY PERFECT GIFT*\n"
            "Personalized Gift Assistant for WhatsApp\n\n"
            "Hi! 👋\n\n"
            "We create personalized products such as mugs, tumblers, "
            "keychains, sublimation gifts, vinyl, DTF products, and more.\n\n"
            "This chatbot will help you find personalized gift ideas "
            "using our real catalog.\n\n"
            "📄 *Where do the products come from?*\n"
            "The products come from a CSV file uploaded to the IDE with "
            "this exact name:\n\n"
            + CATALOG_FILE + "\n\n"
            "That CSV works like a small catalog database. Python reads it, "
            "checks the available products, and filters the best options "
            "based on your answers.\n\n"
            "🤖 *How is GPT used?*\n"
            "After filtering the catalog, the program calls GPT to create "
            "a clearer, personalized recommendation ready to send on "
            "WhatsApp.\n\n"
            "I will ask you only 5 quick questions."
        )

    print(message)


def ask_five_questions(language):
    answers = {}

    if language == "es":
        answers["recipient"] = ask_question(
            "1️⃣ *¿Para quién es el regalo?*",
            [
                ["A", "👩 Mamá"],
                ["B", "👨 Papá"],
                ["C", "💘 Pareja"],
                ["D", "🤝 Amigo/a"],
                ["E", "👩‍🏫 Maestro/a"],
                ["F", "✨ Otro"]
            ],
            language
        )

        answers["occasion"] = ask_question(
            "2️⃣ *¿Para qué ocasión es el regalo?*",
            get_occasion_options(answers["recipient"], language),
            language
        )

        answers["occasion"] = validate_occasion(
            answers["recipient"],
            answers["occasion"],
            language
        )

        answers["budget"] = ask_question(
            "3️⃣ *¿Cuál es tu presupuesto aproximado?*",
            [
                ["A", "💵 Menos de $10"],
                ["B", "💰 Entre $10 y $20"],
                ["C", "🎁 Entre $20 y $35"],
                ["D", "💎 Más de $35"],
                ["E", "🤔 No estoy seguro/a"],
                ["F", "✨ Otro"]
            ],
            language
        )

        answers["style"] = ask_question(
            "4️⃣ *¿Qué estilo de regalo prefieres?*",
            [
                ["A", "🛠️ Útil"],
                ["B", "💖 Sentimental"],
                ["C", "😂 Divertido"],
                ["D", "✨ Elegante"],
                ["E", "🎨 Muy personalizado"],
                ["F", "✨ Otro"]
            ],
            language
        )

        answers["deadline"] = ask_question(
            "5️⃣ *¿Para cuándo lo necesitas?*",
            [
                ["A", "⚡ Hoy"],
                ["B", "🌙 Mañana"],
                ["C", "📅 Esta semana"],
                ["D", "🕊️ Sin urgencia"],
                ["E", "🤔 Todavía no sé"],
                ["F", "✨ Otro"]
            ],
            language
        )

    else:
        answers["recipient"] = ask_question(
            "1️⃣ *Who is the gift for?*",
            [
                ["A", "👩 Mom"],
                ["B", "👨 Dad"],
                ["C", "💘 Partner"],
                ["D", "🤝 Friend"],
                ["E", "👩‍🏫 Teacher"],
                ["F", "✨ Other"]
            ],
            language
        )

        answers["occasion"] = ask_question(
            "2️⃣ *What is the occasion?*",
            get_occasion_options(answers["recipient"], language),
            language
        )

        answers["occasion"] = validate_occasion(
            answers["recipient"],
            answers["occasion"],
            language
        )

        answers["budget"] = ask_question(
            "3️⃣ *What is your approximate budget?*",
            [
                ["A", "💵 Under $10"],
                ["B", "💰 Between $10 and $20"],
                ["C", "🎁 Between $20 and $35"],
                ["D", "💎 More than $35"],
                ["E", "🤔 Not sure"],
                ["F", "✨ Other"]
            ],
            language
        )

        answers["style"] = ask_question(
            "4️⃣ *What gift style do you prefer?*",
            [
                ["A", "🛠️ Useful"],
                ["B", "💖 Sentimental"],
                ["C", "😂 Funny"],
                ["D", "✨ Elegant"],
                ["E", "🎨 Very personalized"],
                ["F", "✨ Other"]
            ],
            language
        )

        answers["deadline"] = ask_question(
            "5️⃣ *When do you need it?*",
            [
                ["A", "⚡ Today"],
                ["B", "🌙 Tomorrow"],
                ["C", "📅 This week"],
                ["D", "🕊️ No rush"],
                ["E", "🤔 I am not sure yet"],
                ["F", "✨ Other"]
            ],
            language
        )

    return answers


def ask_question(question, options, language):
    message = question + "\n\n"

    for option in options:
        message += option[0] + ". " + option[1] + "\n"

    if language == "es":
        message += "\nEscribe la letra de tu opción:"
    else:
        message += "\nType the letter of your choice:"

    answer = input(message)
    answer_clean = clean_text(answer)
    selected_text = ""

    for option in options:
        if answer_clean == clean_text(option[0]):
            selected_text = option[1]

    if answer_clean == "f":
        if language == "es":
            selected_text = input(
                "✨ Elegiste *Otro*.\n\n"
                "Cuéntame brevemente tu opción:"
            )
        else:
            selected_text = input(
                "✨ You selected *Other*.\n\n"
                "Briefly tell me your option:"
            )

    if selected_text == "":
        selected_text = answer

    return selected_text


def get_occasion_options(recipient, language):
    recipient_type = get_recipient_type(recipient)

    if language == "es":
        if recipient_type == "partner":
            return [
                ["A", "🎂 Cumpleaños"],
                ["B", "💞 Aniversario"],
                ["C", "💘 San Valentín"],
                ["D", "🎄 Navidad"],
                ["E", "🎁 Sorpresa romántica"],
                ["F", "✨ Otro"]
            ]

        if recipient_type == "mother":
            return [
                ["A", "🎂 Cumpleaños"],
                ["B", "👩 Día de la Madre"],
                ["C", "🙏 Agradecimiento"],
                ["D", "🎄 Navidad"],
                ["E", "🎁 Sorpresa especial"],
                ["F", "✨ Otro"]
            ]

        if recipient_type == "father":
            return [
                ["A", "🎂 Cumpleaños"],
                ["B", "👨 Día del Padre"],
                ["C", "🙏 Agradecimiento"],
                ["D", "🎄 Navidad"],
                ["E", "🎁 Sorpresa especial"],
                ["F", "✨ Otro"]
            ]

        if recipient_type == "teacher":
            return [
                ["A", "🙏 Agradecimiento"],
                ["B", "🎂 Cumpleaños"],
                ["C", "🎓 Fin de curso"],
                ["D", "🎄 Navidad"],
                ["E", "🏆 Reconocimiento"],
                ["F", "✨ Otro"]
            ]

        return [
            ["A", "🎂 Cumpleaños"],
            ["B", "🙏 Agradecimiento"],
            ["C", "🎓 Graduación"],
            ["D", "🎄 Navidad"],
            ["E", "🎁 Sorpresa especial"],
            ["F", "✨ Otro"]
        ]

    if recipient_type == "partner":
        return [
            ["A", "🎂 Birthday"],
            ["B", "💞 Anniversary"],
            ["C", "💘 Valentine's Day"],
            ["D", "🎄 Christmas"],
            ["E", "🎁 Romantic surprise"],
            ["F", "✨ Other"]
        ]

    if recipient_type == "mother":
        return [
            ["A", "🎂 Birthday"],
            ["B", "👩 Mother's Day"],
            ["C", "🙏 Thank you"],
            ["D", "🎄 Christmas"],
            ["E", "🎁 Special surprise"],
            ["F", "✨ Other"]
        ]

    if recipient_type == "father":
        return [
            ["A", "🎂 Birthday"],
            ["B", "👨 Father's Day"],
            ["C", "🙏 Thank you"],
            ["D", "🎄 Christmas"],
            ["E", "🎁 Special surprise"],
            ["F", "✨ Other"]
        ]

    if recipient_type == "teacher":
        return [
            ["A", "🙏 Thank you"],
            ["B", "🎂 Birthday"],
            ["C", "🎓 End of school year"],
            ["D", "🎄 Christmas"],
            ["E", "🏆 Recognition"],
            ["F", "✨ Other"]
        ]

    return [
        ["A", "🎂 Birthday"],
        ["B", "🙏 Thank you"],
        ["C", "🎓 Graduation"],
        ["D", "🎄 Christmas"],
        ["E", "🎁 Special surprise"],
        ["F", "✨ Other"]
    ]


def validate_occasion(recipient, occasion, language):
    recipient_type = get_recipient_type(recipient)
    occasion_text = clean_text(occasion)

    romantic_words = [
        "aniversario",
        "anniversary",
        "san valentin",
        "valentine",
        "romantico",
        "romantica",
        "romantic"
    ]

    if recipient_type != "partner":
        for word in romantic_words:
            if word in occasion_text:
                if language == "es":
                    return "🎁 Sorpresa especial"
                return "🎁 Special surprise"

    return occasion


def load_catalog(file_name):
    catalog = []

    try:
        file = open(file_name, encoding="utf-8")
    except:
        return catalog

    lines = []

    for line in file:
        line = line.strip()

        if line != "":
            lines.append(line)

    file.close()

    if len(lines) == 0:
        return catalog

    delimiter = detect_delimiter(lines)
    header_index = find_header_index(lines)

    if header_index == -1:
        header_index = 0

    headers = split_csv_line(lines[header_index], delimiter)

    for i in range(header_index + 1, len(lines)):
        values = split_csv_line(lines[i], delimiter)
        product = {}

        for j in range(len(headers)):
            header = headers[j].strip()

            if j < len(values):
                product[header] = values[j].strip()
            else:
                product[header] = ""

        product["_search_text"] = make_search_text(product)
        product["_name_text"] = get_product_name_text(product)

        catalog.append(product)

    return catalog


def detect_delimiter(lines):
    comma_count = 0
    semicolon_count = 0

    limit = 5

    if len(lines) < limit:
        limit = len(lines)

    for i in range(limit):
        comma_count += count_character(lines[i], ",")
        semicolon_count += count_character(lines[i], ";")

    if semicolon_count > comma_count:
        return ";"

    return ","


def count_character(text, character):
    count = 0

    for char in text:
        if char == character:
            count += 1

    return count


def find_header_index(lines):
    for i in range(len(lines)):
        line = clean_text(lines[i])

        has_sku = "sku" in line
        has_product = (
            "producto" in line
            or "product" in line
            or "servicio" in line
        )
        has_price = "precio" in line or "price" in line
        has_category = "categoria" in line or "category" in line

        if has_sku and has_product:
            return i

        if has_product and has_price and has_category:
            return i

    return -1


def split_csv_line(line, delimiter):
    values = []
    current = ""
    inside_quotes = False

    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == delimiter and not inside_quotes:
            values.append(current)
            current = ""
        else:
            current += char

    values.append(current)

    cleaned_values = []

    for value in values:
        value = value.strip()

        if len(value) >= 2:
            if value[0] == '"' and value[len(value) - 1] == '"':
                value = value[1:len(value) - 1]

        cleaned_values.append(value)

    return cleaned_values


def make_search_text(product):
    text = ""

    for key in product:
        text += " " + clean_text(product[key])

    return text


def get_product_name_text(product):
    text = ""

    for key in product:
        key_clean = clean_text(key)

        if "producto" in key_clean or "servicio" in key_clean:
            text += " " + clean_text(product[key])

        if "product" in key_clean or "categoria" in key_clean:
            text += " " + clean_text(product[key])

        if "category" in key_clean:
            text += " " + clean_text(product[key])

    return text


def clean_text(text):
    text = str(text).lower().strip()

    replacements = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ñ": "n",
        "$": "",
        ".": " ",
        ",": " ",
        ";": " ",
        ":": " ",
        "-": " ",
        "/": " ",
        "(": " ",
        ")": " ",
        "¿": "",
        "?": "",
        "¡": "",
        "!": ""
    }

    for old_character in replacements:
        text = text.replace(
            old_character,
            replacements[old_character]
        )

    return text


def get_recipient_type(answer):
    text = clean_text(answer)

    if (
        "mama" in text
        or "madre" in text
        or "mom" in text
        or "mother" in text
    ):
        return "mother"

    if (
        "papa" in text
        or "padre" in text
        or "dad" in text
        or "father" in text
    ):
        return "father"

    if (
        "pareja" in text
        or "novio" in text
        or "novia" in text
        or "esposo" in text
        or "esposa" in text
        or "partner" in text
        or "boyfriend" in text
        or "girlfriend" in text
        or "husband" in text
        or "wife" in text
    ):
        return "partner"

    if (
        "maestro" in text
        or "maestra" in text
        or "teacher" in text
    ):
        return "teacher"

    if "cliente" in text or "client" in text:
        return "client"

    if (
        "amigo" in text
        or "amiga" in text
        or "friend" in text
    ):
        return "friend"

    return "other"


def is_bad_match_for_recipient(product, recipient_type):
    product_name = product["_name_text"]

    romantic_words = [
        "pareja",
        "novio",
        "novia",
        "esposo",
        "esposa",
        "romantico",
        "romantica",
        "san valentin",
        "aniversario"
    ]

    alcohol_words = [
        "tequilero",
        "shot",
        "licor",
        "cerveza"
    ]

    if recipient_type != "partner":
        for word in romantic_words:
            if word in product_name:
                return True

    if (
        recipient_type == "mother"
        or recipient_type == "father"
        or recipient_type == "teacher"
        or recipient_type == "client"
    ):
        for word in alcohol_words:
            if word in product_name:
                return True

    return False


def find_best_products(catalog, answers):
    scored_products = []

    recipient_type = get_recipient_type(
        answers["recipient"]
    )

    user_text = ""
    user_text += " " + expand_words(answers["recipient"])
    user_text += " " + expand_words(answers["occasion"])
    user_text += " " + expand_words(answers["style"])

    budget_range = get_budget_range(answers["budget"])
    budget_min = budget_range[0]
    budget_max = budget_range[1]

    deadline = clean_text(answers["deadline"])

    for product in catalog:
        score = 0
        product_text = product["_search_text"]

        if is_bad_match_for_recipient(
            product,
            recipient_type
        ):
            score -= 100

        words = user_text.split()

        for word in words:
            if len(word) > 2 and word in product_text:
                score += 2

        price = find_price_in_product(product)

        if price != -1:
            if budget_max != -1:
                if price <= budget_max:
                    score += 4
                else:
                    score -= 4

            elif budget_min != -1:
                if price >= budget_min:
                    score += 3
                else:
                    score += 1

        if (
            "disponible" in product_text
            or "available" in product_text
        ):
            score += 2

        delivery_days = find_delivery_days(product)

        if "today" in deadline or "hoy" in deadline:
            if delivery_days != -1 and delivery_days <= 1:
                score += 3
            elif delivery_days > 1:
                score -= 3

        if (
            "tomorrow" in deadline
            or "manana" in deadline
        ):
            if delivery_days != -1 and delivery_days <= 2:
                score += 3
            elif delivery_days > 2:
                score -= 2

        if "week" in deadline or "semana" in deadline:
            if delivery_days != -1 and delivery_days <= 7:
                score += 2

        if (
            "personalizacion" in product_text
            or "personalizado" in product_text
        ):
            score += 2

        scored_products.append([score, product])

    scored_products = sort_products(scored_products)

    best_products = []

    for item in scored_products:
        score = item[0]
        product = item[1]

        if score > -50:
            best_products.append(product)

        if len(best_products) == 8:
            break

    return best_products


def expand_words(text):
    text = clean_text(text)
    expanded = text
    words = text.split()

    for word in words:
        if word in ["mama", "mom", "mother"]:
            expanded += (
                " madre dia de la madre cumpleanos "
                "agradecimiento sentimental foto frase taza termo"
            )

        if word in ["papa", "dad", "father"]:
            expanded += (
                " padre dia del padre cumpleanos "
                "agradecimiento util trabajo taza termo"
            )

        if word in [
            "pareja",
            "partner",
            "novio",
            "novia",
            "boyfriend",
            "girlfriend",
            "esposo",
            "esposa"
        ]:
            expanded += (
                " amor aniversario san valentin "
                "sentimental pareja romantico"
            )

        if word in ["amigo", "amiga", "friend"]:
            expanded += (
                " amistad cumpleanos agradecimiento "
                "divertido detalle"
            )

        if word in ["maestro", "maestra", "teacher"]:
            expanded += (
                " profesor profesora agradecimiento "
                "detalle util oficina"
            )

        if word in ["cumpleanos", "birthday"]:
            expanded += " celebracion regalo divertido sorpresa"

        if word in ["graduacion", "graduation"]:
            expanded += " universidad estudio logro"

        if word in ["util", "useful"]:
            expanded += (
                " trabajo oficina gimnasio estudio "
                "uso diario termo taza mousepad"
            )

        if word == "sentimental":
            expanded += " foto frase recuerdo"

        if word in ["divertido", "funny"]:
            expanded += " celebracion sorpresa"

        if word in ["elegante", "elegant"]:
            expanded += " minimalista premium especial"

        if word in ["personalizado", "personalized"]:
            expanded += (
                " personalizacion nombre foto frase diseno"
            )

        if word in ["economico", "affordable"]:
            expanded += " barato detalle bajo precio"

    return expanded


def get_budget_range(text):
    cleaned = clean_text(text)
    numbers = get_numbers(cleaned)

    if len(numbers) == 0:
        return [-1, -1]

    if (
        "menos" in cleaned
        or "under" in cleaned
        or "less" in cleaned
    ):
        return [0, numbers[0]]

    if (
        "mas" in cleaned
        or "more" in cleaned
        or "over" in cleaned
    ):
        return [numbers[0], -1]

    if len(numbers) >= 2:
        return [numbers[0], numbers[1]]

    return [0, numbers[0]]


def get_numbers(text):
    numbers = []
    current = ""

    for character in text:
        if character >= "0" and character <= "9":
            current += character
        else:
            if current != "":
                numbers.append(int(current))
                current = ""

    if current != "":
        numbers.append(int(current))

    return numbers


def find_price_in_product(product):
    for key in product:
        clean_key = clean_text(key)

        if (
            "precio" in clean_key
            or "price" in clean_key
            or "usd" in clean_key
        ):
            return get_first_number(product[key])

    return -1


def find_delivery_days(product):
    for key in product:
        clean_key = clean_text(key)

        if (
            "tiempo" in clean_key
            or "entrega" in clean_key
            or "delivery" in clean_key
        ):
            numbers = get_numbers(clean_text(product[key]))

            if len(numbers) > 0:
                return numbers[len(numbers) - 1]

    return -1


def get_first_number(text):
    text = str(text)
    current = ""
    found_number = False

    for character in text:
        if (
            character >= "0"
            and character <= "9"
        ) or character == ".":
            current += character
            found_number = True
        else:
            if found_number:
                break

    if current == "":
        return -1

    try:
        return float(current)
    except:
        return -1


def sort_products(scored_products):
    sorted_list = []

    while len(scored_products) > 0:
        best_index = 0

        for i in range(len(scored_products)):
            if (
                scored_products[i][0]
                > scored_products[best_index][0]
            ):
                best_index = i

        sorted_list.append(
            scored_products[best_index]
        )

        scored_products.pop(best_index)

    return sorted_list


def build_gpt_prompt(language, answers, products):
    prompt = ""

    if language == "es":
        prompt += (
            "Eres el asistente amable de ventas de "
            "My Perfect Gift.\n"
        )
        prompt += (
            "Ayudas a elegir regalos personalizados usando "
            "solamente el catalogo real.\n\n"
        )

        prompt += "El cliente respondio:\n\n"
        prompt += "Para quien es: " + answers["recipient"] + "\n"
        prompt += "Ocasion: " + answers["occasion"] + "\n"
        prompt += "Presupuesto: " + answers["budget"] + "\n"
        prompt += "Estilo: " + answers["style"] + "\n"
        prompt += "Lo necesita para: " + answers["deadline"] + "\n\n"

        prompt += "Productos reales que puedes recomendar:\n"

        for i in range(len(products)):
            prompt += "\nProducto " + str(i + 1) + ":\n"

            for key in products[i]:
                if (
                    key != "_search_text"
                    and key != "_name_text"
                ):
                    prompt += (
                        key + ": "
                        + str(products[i][key])
                        + "\n"
                    )

        prompt += "\nReglas obligatorias:\n"
        prompt += "- Responde en espanol.\n"
        prompt += "- Escribe un solo mensaje listo para WhatsApp.\n"
        prompt += "- Todo debe quedar en un solo mensaje; no lo dividas en varios mensajes.\n"
        prompt += "- Usa espacios, iconos y texto facil de leer.\n"
        prompt += "- Deja una linea en blanco entre cada opcion.\n"
        prompt += "- Usa una linea separadora antes de cada opcion y antes de la recomendacion principal.\n"
        prompt += "- Recomienda un maximo de 3 opciones.\n"
        prompt += "- No inventes productos ni datos.\n"
        prompt += "- Usa solamente los productos incluidos arriba.\n"
        prompt += (
            "- Recomienda una frase corta, original y apropiada "
            "para cada producto.\n"
        )
        prompt += (
            "- La frase debe relacionarse con la persona y la ocasion.\n"
        )
        prompt += (
            "- Los productos romanticos son exclusivos para pareja.\n"
        )
        prompt += (
            "- Para mama o papa no recomiendes productos de pareja, "
            "aniversario o San Valentin.\n"
        )
        prompt += (
            "- Para maestros o clientes evita productos romanticos "
            "o relacionados con alcohol.\n"
        )
        prompt += (
            "- Si falta informacion, escribe No especificado.\n\n"
        )

        prompt += "Usa exactamente este formato:\n\n"
        prompt += (
            "🎁 *Según lo que me contaste, "
            "te recomiendo estas opciones:*\n\n"
        )

        for number in range(1, 4):
            prompt += "------------------------------\n"
            prompt += "✨ *Opción " + str(number) + ":*\n\n"
            prompt += "📌 *Producto:*\n"
            prompt += "💡 *Por qué encaja:*\n"
            prompt += "🎨 *Personalización sugerida:*\n"
            prompt += "✍️ *Frase sugerida:*\n"
            prompt += "💵 *Precio aproximado:*\n"
            prompt += "⏰ *Urgencia o disponibilidad:*\n\n"

        prompt += (
            "✅ *Mi recomendación principal sería ______ "
            "porque ______.*"
        )

    else:
        prompt += (
            "You are the friendly sales assistant for "
            "My Perfect Gift.\n"
        )
        prompt += (
            "You recommend personalized gifts using only "
            "the real catalog.\n\n"
        )

        prompt += "Customer answers:\n\n"
        prompt += "Gift for: " + answers["recipient"] + "\n"
        prompt += "Occasion: " + answers["occasion"] + "\n"
        prompt += "Budget: " + answers["budget"] + "\n"
        prompt += "Style: " + answers["style"] + "\n"
        prompt += "Needed by: " + answers["deadline"] + "\n\n"

        prompt += "Real products you may recommend:\n"

        for i in range(len(products)):
            prompt += "\nProduct " + str(i + 1) + ":\n"

            for key in products[i]:
                if (
                    key != "_search_text"
                    and key != "_name_text"
                ):
                    prompt += (
                        key + ": "
                        + str(products[i][key])
                        + "\n"
                    )

        prompt += "\nMandatory rules:\n"
        prompt += "- Answer in English.\n"
        prompt += "- Write one message ready for WhatsApp.\n"
        prompt += "- Everything must stay in one message; do not split it into multiple messages.\n"
        prompt += "- Use spacing, icons, and easy-to-read text.\n"
        prompt += "- Leave one blank line between each option.\n"
        prompt += "- Use a separator line before each option and before the main recommendation.\n"
        prompt += "- Recommend a maximum of 3 options.\n"
        prompt += "- Do not invent products or information.\n"
        prompt += "- Use only the products included above.\n"
        prompt += "- Translate descriptive Spanish product names into natural English.\n"
        prompt += "- In every *Product:* line, the product name must be in English.\n"
        prompt += "- Keep SKU, price, availability, and catalog facts unchanged.\n"
        prompt += "- Example: write Personalized acrylic keychains, not Llaveros acrilicos personalizados.\n"
        prompt += (
            "- Recommend a short and appropriate phrase "
            "for each product.\n"
        )
        prompt += (
            "- The phrase must match the recipient and occasion.\n"
        )
        prompt += (
            "- Romantic products are exclusively for partners.\n"
        )
        prompt += (
            "- For mom or dad, do not recommend couple, "
            "anniversary, or Valentine's products.\n"
        )
        prompt += (
            "- For teachers or clients, avoid romantic "
            "or alcohol-related products.\n"
        )
        prompt += (
            "- If information is missing, write Not specified.\n\n"
        )

        prompt += "Use exactly this format:\n\n"
        prompt += "Start every option with this exact line: ------------------------------\n"
        prompt += (
            "🎁 *Based on what you told me, "
            "I recommend these options:*\n\n"
        )

        for number in range(1, 4):
            prompt += "✨ *Option " + str(number) + ":*\n\n"
            prompt += "📌 *Product:*\n"
            prompt += "💡 *Why it fits:*\n"
            prompt += "🎨 *Suggested personalization:*\n"
            prompt += "✍️ *Suggested phrase:*\n"
            prompt += "💵 *Approximate price:*\n"
            prompt += "⏰ *Urgency or availability:*\n\n"

        prompt += (
            "✅ *My main recommendation would be ______ "
            "because ______.*"
        )

    return prompt


if __name__ == "__main__":
    main()
