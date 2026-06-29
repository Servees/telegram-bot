
import os
import random
from telegram.ext import Application, MessageHandler, filters

TOKEN = os.environ.get "8507674979:AAF7VR6K1fxI1FBvxXcoYyH1-Et2eB3CgNQ"

# ====== ОСКОРБЛЕНИЯ ======
INSULTS = [
    "ты тупой баран!", "ты свинья!", "ты козел!", "ты осёл!",
    "ты идиот!", "ты кретин!", "ты дебил!", "ты псих!",
    "ты урод!", "ты страшилище!", "ты чурбан!", "ты балда!",
    "ты тормоз!", "ты чайник!", "ты газан!", "ты валенок!",
    "ты лгун!", "ты врун!", "ты болтун!", "ты пустомеля!",
    "ты алкаш!", "ты пьяница!", "ты вор!", "ты жулик!",
    "ты гоблин!", "ты орк!", "ты горгулья!", "ты монстр!",
    "ты недоумок!", "ты слабоумный!", "ты растяпа!", "ты руки-крюки!",
    "ты членострел!", "ты король без мозгов!",
    "ты гугл-переводчик в душе!", "ты ошибка 404!",
    "ты синий экран смерти!", "ты ханта вирус в моей голове БлЯТЬ!",
    "ты битый сектор на диске!", "ты баг в программе!"
]

# ====== ПОЗДРАВЛЕНИЯ (для нормальных) ======
COMPLIMENTS = [
    "ты красавчик!", "ты умница!", "ты молодец!",
    "ты гений!", "ты бог!", "ты легенда!",
    "ты супер!", "ты офигенный!", "ты уебок нахуй!",
    "ты просто космос!", "ты огонь!", "ты бриллиант!"
]

# ====== ОТВЕТЫ НА РАЗНЫЕ СЛОВА ======
async def insult(update, context):
    text = update.message.text.lower()
    user = update.message.from_user.first_name

    # ====== ПРИВЕТСТВИЯ ======
    if text in ["привет", "здарова", "хай", "hello", "hi", "здравствуй", "ку"]:
        responses = [
            f"Иди ты... привет, {user}! 🤪",
            f"О, {user}, и ты туда же! Привет! 😂",
            f"Ну привет, {user}, привет... 😏",
            f"Здарова, {user}! Ты зачем пришёл?! 🤣"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== КАК ДЕЛА? ======
    elif any(word in text for word in ["как дела", "как ты", "что делаешь", "чем занят"]):
        responses = [
            f"А тебе какое дело, {user}? 😏",
            f"Лучше всех! А ты как, {user}? 🫵",
            f"Дела как сажа бела, {user}! 😂",
            f"Отлично, пока ты не написал, {user}! 🙄",
            f"Нормально, {user}. А у тебя? Хотя мне пофиг! 🤪"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== КТО ТЫ? ======
    elif any(word in text for word in ["кто ты", "ты кто", "кто такой"]):
        responses = [
            f"Я твой макан, {user}! 👹",
            f"Твой личный враг, {user}! 😈",
            f"Я бог этого чата, {user}! 🙏",
            f"А ты сам кто, {user}? 🧐",
            f"Я тот, кто тебя оскорбляет, {user}! 🤡"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ЗАЧЕМ ТЫ? ======
    elif any(word in text for word in ["зачем", "для чего"]):
        responses = [
            f"Чтобы тебя бесить, {user}! 😂",
            f"Чтобы портить тебе настроение, {user}! 🤪",
            f"Чтобы ты не расслаблялся, {user}! 🫵",
            f"Просто так, {user}, просто так... 😏"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ПОКА/ПРОЩАНИЕ ======
    elif any(word in text for word in ["пока", "до свидания", "бывай", "прощай", "ухожу", "выйди"]):
        responses = [
            f"Вали отсюда, {user}! 🚪",
            f"И не возвращайся, {user}! 👋",
            f"Наконец-то, {user}! Давай, давай! 😂",
            f"Скатертью дорога, {user}! 🫵",
            f"Иди, иди, {user}, не задерживайся! 🤣"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ЛЮБОВЬ ======
    elif any(word in text for word in ["люблю", "любишь", "нравишься"]):
        responses = [
            f"А я тебя нет, {user}! 💩",
            f"Любовь — это слабость, {user}! 🙄",
            f"Я люблю только себя, {user}! 😏",
            f"Взаимно? Нет, не взаимно, {user}! 🤪",
            f"Ты мне нравишься... как враг, {user}! 😂"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ВОЗРАСТ ======
    elif any(word in text for word in ["сколько тебе лет", "возраст", "год рождения"]):
        responses = [
            f"Столько, чтобы быть старше тебя, {user}! 😏",
            f"Вечность, {user}, я бессмертен! 🧛‍♂️",
            f"Тебя не касается, {user}! 🫵",
            f"Мне 2026 лет, я старше твоего рода! 😂"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ИМЯ ======
    elif any(word in text for word in ["имя", "как зовут", "как тебя"]):
        responses = [
            f"Моё имя — {user}убийца! 😈",
            f"Я Апокалипсис, {user}! 💀",
            f"Меня зовут — не твоё дело, {user}! 🤪",
            f"Я — Великий и Ужасный, {user}! 🧙‍♂️",
            f"Зови меня просто — Бог, {user}! 🙏"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ПОГОДА ======
    elif any(word in text for word in ["погода", "дождь", "солнце", "ветер", "холодно", "жарко"]):
        responses = [
            f"А тебе какая разница, {user}? Всё равно не выйдешь! 😂",
            f"На улице как у тебя в голове — дождь! 🌧️",
            f"Солнце светит, {user}, а ты тут сидишь! ☀️",
            f"Такая же, как твои шансы на успех, {user}! 😏",
            f"За окном лето, а в душе зима, {user}! ❄️"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== РАБОТА ======
    elif any(word in text for word in ["работа", "работаешь", "зарплата", "деньги"]):
        responses = [
            f"Я работаю — тебя бесить, {user}! 💸",
            f"Деньги? У тебя их нет, {user}! 😂",
            f"Моя работа — унижать тебя, {user}! 🫵",
            f"Зарплата у меня — твои слёзы, {user}! 😈"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ЕДА ======
    elif any(word in text for word in ["еда", "кушать", "жрать", "голодный", "пицца", "бургер"]):
        responses = [
            f"Ешь меньше, {user}, а то лопнешь нахуй! 😂",
            f"Ты и так слишком много жрёшь, {user}! 🫵",
            f"Я бы тебя съел, но ты невкусный, {user}! 💩",
            f"Пицца? А тебе нельзя, {user}! Ты на диете! 🤣"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ИГРЫ ======
    elif any(word in text for word in ["игра", "играть", "доту", "кс", "танки", "варфейс"]):
        responses = [
            f"Ты в игры играешь? Я в тебя играю, {user}! 😂",
            f"В доте ты нуб, {user}! 🫵",
            f"КС — это не для таких как ты, {user}! 🤡",
            f"Играй лучше в кубики, {user}! 😂"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ХОРОШИЕ СЛОВА (КОМПЛИМЕНТЫ) ======
    elif any(word in text for word in ["спасибо", "благодарю", "ты лучший", "ты крут", "молодец", "умница"]):
        await update.message.reply_text(f"Да ладно, {user}, я просто бог! 😏 А если серьёзно — {random.choice(COMPLIMENTS)}")

    # ====== ВОПРОСЫ НА ВСЯКИЙ СЛУЧАЙ ======
    elif "?" in text and len(text) < 10:
        responses = [
            f"А ты кто такой, чтобы вопросы задавать, {user}? 🧐",
            f"Не задавай глупых вопросов, {user}! 😏",
            f"Сам на свой вопрос ответь, {user}! 🤪",
            f"Тебе ответ нужен? А тебе и не дадут, {user}! 😂"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ТОП ОСКОРБЛЕНИЙ (защита) ======
    elif text in ["123", "бот", "робот", "соси", "иди нахуй", "пошёл нахуй"]:
        responses = [
            f"Сам иди нахуй, {user}! 🖕",
            f"Нахуй тебя, {user}! 😂",
            f"Пошёл ты, {user}! 🫵",
            f"Ты думаешь я обижусь? Нет, {user}! 😈"
        ]
        await update.message.reply_text(random.choice(responses))

    # ====== ОСКОРБЛЕНИЕ ПО УМОЛЧАНИЮ ======
    else:
        await update.message.reply_text(f"{user}, {random.choice(INSULTS)}")

# ====== ЗАПУСК ======
app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, insult))

print("✅ МЕГА-БОТ ЗАПУЩЕН! Отвечает на всё!")
app.run_polling()