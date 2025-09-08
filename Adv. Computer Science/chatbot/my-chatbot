import random

PRESENT_VERBS = [
    "accept",
    "is",
    "allow",
    "ask",
    "believe",
    "bring",
    "buy",
    "call",
    "carry",
    "change",
    "choose",
    "clean",
    "close",
    "come",
    "consider",
    "continue",
    "cut",
    "decide",
    "develop",
    "do",
    "draw",
    "drive",
    "eat",
    "explain",
    "fall",
    "feel",
    "find",
    "fly",
    "forget",
    "get",
    "give",
    "go",
    "grow",
    "happen",
    "have",
    "hear",
    "help",
    "hold",
    "hope",
    "keep",
    "know",
    "learn",
    "leave",
    "let",
    "like",
    "listen",
    "live",
    "look",
    "lose",
    "love",
    "make",
    "mean",
    "meet",
    "move",
    "need",
    "open",
    "pay",
    "play",
    "put",
    "read",
    "run",
    "say",
    "see",
    "seem",
    "sell",
    "send",
    "set",
    "show",
    "sit",
    "sleep",
    "speak",
    "spend",
    "stand",
    "start",
    "stay",
    "stop",
    "study",
    "take",
    "talk",
    "teach",
    "tell",
    "think",
    "travel",
    "try",
    "turn",
    "understand",
    "use",
    "wait",
    "walk",
    "want",
    "watch",
    "win",
    "work",
    "order, " "write",
    "add",
    "agree",
    "answer",
    "begin",
    "belong",
    "break",
    "build",
    "carry",
    "catch",
    "climb",
    "compare",
    "complete",
    "count",
    "decide",
    "deliver",
    "describe",
    "design",
    "enjoy",
    "enter",
    "explain",
    "follow",
    "forget",
    "happen",
    "improve",
    "increase",
    "join",
    "jump",
    "lead",
    "listen",
    "look",
    "move",
    "offer",
    "plan",
    "produce",
    "protect",
    "reach",
    "receive",
    "remember",
    "return",
    "save",
    "send",
    "serve",
    "show",
    "sing",
    "sit",
    "spend",
    "stand",
    "stop",
    "support",
    "take",
    "talk",
    "teach",
    "think",
    "touch",
    "travel",
    "try",
    "understand",
    "use",
    "visit",
    "wait",
    "walk",
    "watch",
    "wish",
    "work",
    "write",
]

PAST_VERBS = ["went", "ate", "liked", "ordered", "saw"]

NOUNS = [
    "name",
    "time",
    "year",
    "people",
    "way",
    "day",
    "man",
    "woman",
    "child",
    "world",
    "school",
    "state",
    "family",
    "student",
    "group",
    "country",
    "problem",
    "hand",
    "part",
    "place",
    "case",
    "week",
    "company",
    "system",
    "program",
    "question",
    "work",
    "night",
    "point",
    "home",
    "water",
    "room",
    "mother",
    "sandwich",
    "taco",
    "bread",
    "fruit",
    "boba",
    "burger",
    "area",
    "money",
    "story",
    "fact",
    "month",
    "lot",
    "right",
    "study",
    "book",
    "eye",
    "job",
    "word",
    "business",
    "issue",
    "side",
    "kind",
    "head",
    "house",
    "service",
    "friend",
    "father",
    "power",
    "hour",
    "game",
    "line",
    "end",
    "member",
    "law",
    "car",
    "city",
    "community",
    "name",
    "president",
    "team",
    "minute",
    "idea",
    "kid",
    "body",
    "information",
    "back",
    "parent",
    "face",
    "level",
    "office",
    "door",
    "health",
    "person",
    "art",
    "war",
    "history",
    "party",
    "rsesult",
    "change",
    "morning",
    "reason",
    "research",
    "girl",
    "guy",
    "moment",
    "air",
    "teacher",
    "force",
    "education",
    "foot",
    "boy",
    "age",
    "policy",
    "music",
    "market",
    "sense",
    "nation",
    "plan",
    "college",
    "effect",
    "control",
    "field",
    "care",
    "road",
    "science",
    "truth",
    "food",
    "movie",
    "dog",
    "cat",
    "tree",
    "river",
    "mountain",
    "sea",
    "ocean",
    "computer",
    "phone",
    "internet",
    "paper",
    "pen",
    "letter",
    "song",
    "language",
    "country",
    "city",
    "village",
    "farm",
    "garden",
    "building",
    "bridge",
    "church",
    "hospital",
    "store",
    "restaurant",
    "hotel",
    "bank",
    "library",
    "park",
    "airport",
    "station",
    "train",
    "bus",
    "plane",
    "ship",
    "road",
    "street",
    "room",
    "kitchen",
    "bathroom",
    "bed",
    "chair",
    "table",
    "cup",
    "plate",
    "spoon",
    "fork",
    "knife",
    "bottle",
    "glass",
    "bag",
    "box",
    "key",
    "lock",
    "door",
    "window",
    "wall",
    "floor",
    "ceiling",
    "roof",
    "light",
    "lamp",
    "candle",
    "sun",
    "moon",
    "star",
    "sky",
    "cloud",
    "rain",
    "snow",
    "wind",
    "fire",
    "earth",
    "air",
    "water",
    "stone",
    "metal",
    "wood",
    "sand",
    "soil",
    "flower",
    "leaf",
    "grass",
    "fruit",
    "apple",
    "banana",
    "orange",
    "grape",
    "pear",
    "peach",
    "cherry",
    "melon",
    "berry",
    "vegetable",
    "potato",
    "tomato",
    "onion",
    "carrot",
    "cabbage",
    "corn",
    "rice",
    "bread",
    "meat",
    "fish",
    "egg",
    "milk",
    "cheese",
    "butter",
    "salt",
    "sugar",
    "oil",
    "coffee",
    "tea",
    "friendship",
    "love",
    "peace",
    "hope",
    "dream",
    "fear",
    "anger",
    "happiness",
    "sadness",
    "strength",
    "freedom",
    "justice",
    "truth",
    "faith",
    "trust",
    "honor",
    "courage",
    "memory",
    "thought",
    "idea",
    "problem",
    "solution",
    "pizza",
    "question",
    "answer",
    "plan",
    "goal",
    "project",
    "success",
    "failure",
    "lesson",
]

PREPS = [
    "to",
    "in",
    "on",
    "at",
    "by",
    "for",
    "from",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "over",
    "under",
    "within",
    "without",
    "across",
    "behind",
    "beyond",
    "near",
    "since",
    "until",
    "upon",
    "around",
    "among",
    "along",
    "off",
    "outside",
    "inside",
    "onto",
    "past",
    "per",
    "via",
]

DETERMINERS = [
    "the",
    "a",
    "an",
    "my",
    "your",
    "his",
    "her",
    "our",
    "their",
    "this",
    "that",
    "these",
    "those",
]

PRONOUNS = [
    "i",
    "you",
    "he",
    "she",
    "it",
    "we",
    "they",
    "me",
    "him",
    "her",
    "us",
    "them",
    "my",
    "your",
    "his",
    "her",
    "our",
    "their",
    "mine",
    "yours",
    "hers",
    "ours",
    "theirs",
]

def stripString(i: str) -> str:
    return i.strip(".,;:!?()\"'").lower()

class Query:
    def __init__(self, text: str):
        self.string = text
        self.is_question = self.string.strip().endswith("?")
        self.words = self.string.split()
        self.clean = [word.strip(".,;:!?()\"'").lower() for word in self.words]
        self.verbs = [
            word for word in self.clean if word in PRESENT_VERBS or word in PAST_VERBS
        ]
        self.nouns = [word for word in self.clean if word in NOUNS] + [
            word for word in self.clean if word != word.lower()
        ]
        self.subject = self.infer_subject()
        self.prepositional_phrases = self.findPrepositionalPhrases()
        self.topic = next(
            (n for n in self.nouns if n not in ["i", "you", "it", "this", "that"]), "it"
        )

    def infer_subject(self) -> str:

        first = self.clean[0]
        if first in PRONOUNS:
            return first

        if (
            first == "there"
            and len(self.clean) > 1
            and self.clean[1] in {"is", "are", "was", "were"}
        ):
            for i in range(2, len(self.words)):
                w_norm = stripString(self.words[i])
                w_orig = self.words[i]
                if w_norm in NOUNS or (w_orig and w_orig[0].isupper()):
                    return w_norm if w_norm else w_orig.lower()
            return "it"

        first_verb_idx = None
        for i, w in enumerate(self.clean):
            if w in PRESENT_VERBS or w in PAST_VERBS:
                first_verb_idx = i
                break

        if first_verb_idx is not None:
            for i in range(first_verb_idx):
                if self.clean[i] in PRONOUNS:
                    return self.clean[i]

            for i in range(first_verb_idx):
                if self.words[i] and self.words[i][0].isupper():
                    return self.clean[i]

            for i in range(first_verb_idx):
                if self.clean[i] in NOUNS:
                    return self.clean[i]

        if first in PRESENT_VERBS or first in PAST_VERBS:
            return "you"

        for i in range(len(self.words)):
            if self.words[i] and self.words[i][0].isupper():
                return self.clean[i]
        for i in range(len(self.clean)):
            if self.clean[i] in NOUNS:
                return self.clean[i]

        return "it"

    def findPrepositionalPhrases(self):
        phrases = []

        for i in range(len(self.words)):
            head_prep = stripString(self.words[i])

            if head_prep not in PREPS:
                continue

            j = i + 1

            while j < len(self.words) and stripString(self.words[j]) in DETERMINERS:
                j += 1

            seen_noun = False
            seen_pronoun = False
            seen_proper = False

            while j < len(self.words):
                w_norm = stripString(self.words[j])
                w_orig = self.words[j]

                if w_norm or w_norm[:-1] in NOUNS:
                    seen_noun = True

                if w_norm in PRONOUNS:
                    seen_pronoun = True

                if w_orig and w_orig[0].isupper():
                    seen_proper = True

                next_is_prep = (
                    j + 1 < len(self.words) and stripString(self.words[j + 1]) in PREPS
                )
                punct_end = w_orig.endswith((",", ";", ".", "?", "!", ":"))

                j += 1
                if punct_end or next_is_prep:
                    break

            if seen_noun or (
                head_prep in {"at", "with"} and (seen_pronoun or seen_proper)
            ):
                phrases.append(" ".join(self.clean[i:j]))

        return phrases

class Word:
    def __init__(self, text: str):
        self.text = text
        self.is_verb = text in PRESENT_VERBS or text in PAST_VERBS
        self.is_noun = text in NOUNS
        self.is_pronoun = text in PRONOUNS
        self.is_determiner = text in DETERMINERS


class bot:
    def __init__(self, text: str):

        self.query = Query(text)

    def replyToStatement(self):
        if not self.query.verbs and not self.query.nouns:
            print("Tell me more.")
            return

        obj = self.query.topic if self.query.topic else ""
        subj = (
            "I"
            if self.query.subject == "you"
            else "you" if self.query.subject == "i" else self.query.subject
        )
        asdf = " ".join(self.query.prepositional_phrases)

        if self.query.verbs[0] in ["went", "go"]:
            rand = random.randint(0, 2)
            if rand == 0:
                print(f"Why did {subj} go {asdf}?")
                return
            elif rand == 1:
                print(f"How did {subj} like going {asdf}?")
                return
            else:
                print(f"What did you do when {subj} went {asdf}?")
                return
        elif self.query.verbs[0] in ["ate", "eat", "ordered", "order"]:
            print(f"Did {subj} enjoy the {obj}?")
            return
        elif self.query.verbs[0] in ["like", "liked"]:
            print(f"Really! I like {obj} too!")
            return
        elif self.query.verbs[0] in ["love", "loved"]:
            print(f"Really! I love {obj} too!")
            return
        elif self.query.verbs[0] in ["enjoy", "enjoyed"]:
            print(f"Really! I enjoy {obj} too!")
            return
        elif self.query.verbs[0] in ["hate", "hated"]:
            print(f"Really! I hate {obj} too!")
            return
        elif self.query.verbs[0] in ["want", "wanted"]:
            print(f"Wow, you must want it a lot!")
            return


        templates = []
        if self.query.verbs[0]:
            templates.extend([
                lambda: f"What made {subj} {self.query.verbs[0]} {asdf}?".strip(),
                lambda: f"How did {subj} feel about {obj}?",
                lambda: f"Can you share more details about {obj} {asdf}?".strip(),
                lambda: f"What happened after {subj} {self.query.verbs[0]} {asdf}?".strip(),
                lambda: f"Why was {obj} important to {subj}?",
            ])
        else:
            templates.extend([
                lambda: f"What makes {obj} stand out to you?" if subj == "you" else f"What makes {obj} stand out to {subj}?",
                lambda: f"Can you tell me more about {obj} {asdf}?".strip(),
                lambda: "What happened next?",
            ])

        print(random.choice(templates)())

    def replytoQuestion(self):
        rand = random.randint(0, 2)
        if rand == 0:
            print("Go google it.")
        elif rand == 1:
            print("I'm not sure about that.")
        else:
            print("Idk man. I'm not paid enough for this.")

    def reply(self):
        print(
            "------------------------------------------------------------------------------DEBUG------------------------------------------------------------------------------"
        )
        print("Question:", self.query.is_question)
        print("Words:", self.query.words)
        print("Verbs:", self.query.verbs)
        print("Nouns:", self.query.nouns)
        print("Subject:", self.query.subject)
        print("Prepositional Phrases:", self.query.prepositional_phrases)
        print("Topic:", self.query.topic)
        print(
            "-----------------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print("\n")

        if self.query.is_question:
            self.replytoQuestion()
        else:
            self.replyToStatement()


def chat():
    while True:
        try:
            print("")
            text = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        bot(text).reply()


if __name__ == "__main__":
    chat()