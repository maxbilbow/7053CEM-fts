import random


def make_sentence(length: int):
    string: str = ""
    for i in range(length):
        if i > 0:
            string += " "
        string += random.choice(RANDOM_WORDS)
    return string


SKILLS = ["C++",
          "JavaScript",
          "Python",
          "Cheese Roll",
          "cheese_rolling",
          "wrestling",
          "photography",
          "ukulele",
          "chess",
          "guitar",
          "databases",
          "sql",
          "gaming",
          "Spring Boot",
          "homebrew"]

RANDOM_WORDS = ["forgotten", "private", "element", "day", "sheep", "pleasant", "hot", "see", "exciting", "yard", "star",
                "month", "cap", "warn", "development", "sentence", "sort", "trade", "meant", "its", "book", "lovely",
                "path", "garage", "any", "chemical", "leather", "two", "daily", "put", "forty", "naturally", "result",
                "morning", "wrote", "bear", "shop", "military", "they", "strength", "bad", "arrangement", "acres",
                "place", "herd", "quietly", "hunt", "during", "combine", "younger", "mental", "piano", "simple", "sick",
                "hall", "force", "action", "poetry", "exchange", "western", "hat", "actual", "graph", "ship",
                "frequently", "fact", "constantly", "wood", "certain", "elephant", "failed", "occasionally", "known",
                "free", "parts", "film", "would", "ride", "west", "almost", "task", "service", "ground", "swung",
                "mill", "instant", "exist", "twice", "stronger", "sugar", "gun", "wolf", "period", "palace", "port",
                "gold", "valuable", "onto", "plate", "knew", "power", "negative", "mud", "floor", "history", "look",
                "effort", "death", "modern", "tears", "ball", "saved", "quick", "lost", "clothing", "paint", "likely",
                "she", "we", "layers", "struggle", "chapter", "poet", "either", "eye", "breathe", "bark", "silent",
                "uncle", "thrown", "may", "exercise", "duck", "act", "useful", "transportation", "still", "ancient",
                "plan", "pale", "might", "card", "today", "softly", "rich", "telephone", "rapidly", "safety", "drawn",
                "design", "ate", "southern", "breakfast", "belong", "silence", "bound", "take", "familiar", "difficult",
                "prove", "below", "atmosphere", "eager", "positive", "warm", "late", "memory", "bend", "planet",
                "vessels", "avoid", "properly", "atom", "rhythm", "anybody", "blanket", "shot", "examine",
                "mathematics", "suggest", "bet", "rope", "huge", "public", "start", "together", "grain", "step",
                "along", "land", "plastic", "own", "increase", "themselves", "paid", "bring", "breath", "halfway",
                "explanation", "show", "milk", "news", "exclaimed", "sunlight", "shirt", "primitive", "finest",
                "manner", "capital", "pound", "long", "oil", "himself", "our", "aside", "week", "buffalo", "wall",
                "strike", "immediately", "ought", "do", "egg", "shake", "coming", "easier", "product", "down", "each",
                "nor", "cost", "rocket", "deeply", "curve", "without", "stove", "everywhere", "brick", "light",
                "rising", "century", "board", "corn", "list", "author", "excited", "brave", "lower", "most", "leaving",
                "income", "coach", "six", "respect", "condition", "riding", "best", "expect", "new", "active", "box",
                "though", "can", "suit", "judge", "to", "something", "recall", "pencil", "curious", "every", "coal",
                "page", "thought", "garden", "tomorrow", "bar", "soil", "brought", "car", "heat", "sky", "flight",
                "creature", "term", "build", "good", "market", "gave", "notice", "seen", "baby", "meat", "won",
                "ability", "horn", "disease", "tape", "shadow", "people", "snake", "sleep", "rock", "one", "breathing",
                "continued", "knife", "above", "throat", "push", "storm", "worker", "previous", "science", "original",
                "stop", "ran", "personal", "television", "border", "shall", "remove", "congress", "fairly", "oxygen",
                "steady", "my", "protection", "learn", "alive", "fun", "block", "nearest", "flag", "not", "title",
                "willing", "enjoy", "fort", "little", "course", "life", "slipped", "know", "depend", "situation",
                "sister", "jump", "develop", "track", "stage", "shinning", "before", "union", "never", "meet", "pick",
                "ordinary", "choice", "discussion", "separate", "leg", "leaf", "character", "post", "sound", "feature",
                "hair", "dug", "stretch", "order", "happy", "stepped", "cell", "begun", "copy", "stems", "president",
                "massage", "scale", "soft", "careful", "composed", "victory", "letter", "lot", "lady", "organization",
                "cloud", "high", "will", "beat", "search", "voyage", "brief", "greater", "loose", "truth", "born",
                "had", "command", "nervous", "said", "if", "dear", "fur", "especially", "floating", "suppose", "making",
                "stick", "string", "why", "substance", "right", "sometime", "outside", "biggest", "listen", "many",
                "unit", "moon", "balloon", "captain", "weigh", "form", "hole", "doll", "tie", "root", "four", "pie",
                "balance", "spell", "silk", "afternoon", "fast", "grandmother", "guide", "wash", "train", "hurry",
                "talk", "earn", "plural", "beside", "moving", "similar", "quickly", "faster", "thee", "statement",
                "indeed", "machinery", "lead", "equator", "close", "tide", "those", "cook", "express", "brush",
                "describe", "doing", "fix", "nice", "catch", "fifty", "class", "held", "entirely", "cookies", "other",
                "tongue", "printed", "army", "smaller", "favorite", "climb", "consider", "where", "smallest", "mouse",
                "very", "all", "finger", "flew", "furniture", "coat", "length", "magic", "planning", "usual", "lucky",
                "stuck", "wonder", "slip", "distance", "bee", "around", "are", "mind", "swim", "cross", "want",
                "yesterday", "declared", "citizen", "present", "hope", "motion", "tune", "process", "needed", "worth",
                "cloth", "jack", "solution", "mostly", "mean", "according", "store", "industry", "typical", "sun",
                "tribe", "me", "loss", "ants", "hardly", "whistle", "bowl", "word", "farm", "dozen", "trip", "mile",
                "five", "matter", "basis", "pond", "ago", "once", "corner", "frame", "beginning", "unhappy", "note",
                "farmer", "harder", "mysterious", "cannot", "pipe", "pleasure", "else", "mood", "pig", "attention",
                "opposite", "cup", "red", "carry", "mass", "race", "tree", "song", "dropped", "struck", "percent",
                "hide", "on", "muscle", "small", "bone", "diameter", "offer", "children", "heading", "roof", "nuts",
                "inside", "pretty", "handsome", "circle", "use", "teacher", "central", "interior", "exactly",
                "attached", "complex", "country", "slight", "anywhere", "least", "think", "throw", "wheat", "ring",
                "claws", "practical", "wife", "scientist", "field", "sitting", "swing", "monkey", "ourselves",
                "company", "hit", "coffee", "equal", "load", "world", "forget", "tried", "official", "gather",
                "audience", "parent", "visit", "universe", "now", "cheese", "arrange", "visitor", "river", "affect",
                "until", "earth", "electricity", "wealth", "ready", "ruler", "sang", "putting", "satisfied", "could",
                "organized", "name", "blow", "eleven", "whale", "pressure", "wire", "feathers", "tip", "law", "lion",
                "off", "love", "pour", "escape", "quarter", "lips", "plates", "proud", "save", "way", "wheel", "source",
                "slow", "pride", "seat", "doubt", "cream", "foreign", "add", "flat", "sea", "cake", "rhyme", "am",
                "desk", "till", "touch", "thumb", "send", "electric", "screen", "pictured", "noise", "molecular",
                "gift", "pot", "taste", "instance", "seeing", "agree", "particles", "purple", "tight", "win",
                "shoulder", "birth", "sense", "noon", "within", "shoot", "front", "writer", "taught", "neighborhood",
                "method", "watch", "peace", "underline", "kind", "lying", "dark", "clothes", "ten", "home", "remember",
                "father", "correctly", "old", "tent", "sweet", "boy", "bicycle", "total", "early", "hunter", "drove",
                "extra", "living", "cage", "essential", "beauty", "concerned", "flies", "feet", "up", "completely",
                "height", "write", "climate", "short", "how", "settlers", "hold", "aid", "join", "location", "refer",
                "imagine", "even", "roll", "practice", "he", "clearly", "bite", "unknown", "limited", "your", "skin",
                "row", "done", "help", "frighten", "glass", "whenever", "closely", "cattle", "must", "about", "rather",
                "receive", "smell", "hung", "found", "black", "flow", "shaking", "wise", "tube", "characteristic",
                "question", "soon", "remarkable", "function", "material", "driven", "fully", "manufacturing", "shape",
                "terrible", "native", "bus", "top", "taken", "paragraph", "season", "pen", "hard", "control"
                                                                                                   "replace", "got",
                "air", "drop", "wind", "meant", "steady", "out", "buffalo", "pile", "running", "date", "pond",
                "daughter", "against", "tune", "small", "food", "wet", "leave", "behind", "chest", "lamp", "average",
                "basis", "parallel", "there", "ability", "tea", "chart", "fruit", "stop", "luck", "station", "struck",
                "pencil", "shorter", "lake", "under", "almost", "ability", "progress", "memory", "able", "needed",
                "include", "select", "taste", "show", "necessary", "crop", "stand", "blank", "spring", "herd", "lack",
                "nest", "take", "perhaps", "blanket", "flame", "shout", "wind", "dead", "fight", "already", "slave",
                "indeed", "finally", "layers", "dawn", "key", "exclaimed", "mental", "gas", "anyone", "arrow", "famous",
                "lose", "century", "classroom", "taken", "fence", "solid", "next", "pressure", "monkey", "perhaps",
                "until", "empty", "fair", "freedom", "straight", "slide", "we", "properly", "adventure", "ever",
                "spite", "firm", "move", "return", "opportunity", "money", "hung", "apart", "said", "moon", "go",
                "tone", "steep", "tried", "position", "bad", "repeat", "shinning", "means", "expect", "expression",
                "whether", "newspaper", "warn", "eight", "dried", "particularly", "dish", "determine", "balloon",
                "block", "identity", "wore", "wing", "angry", "personal", "fear", "silent", "start", "captain",
                "having", "draw", "force", "blow", "drew", "furniture", "remember", "grass", "research", "mouth",
                "doll", "military", "warm", "box", "won", "bound", "swimming", "successful", "longer", "freedom",
                "path", "been", "flight", "for", "running", "thing", "cat", "studying", "drawn", "kind", "guess",
                "cave", "hundred", "detail", "exist", "someone", "stream", "combination", "pride", "pull", "instant",
                "rice", "nor", "race", "country", "for", "article", "slave", "final", "unhappy", "energy", "journey",
                "let", "tie", "wind", "below", "safety", "easier", "important", "worth", "except", "sky", "ever",
                "very", "money", "mistake", "away", "shoot", "poem", "paragraph", "military", "principal", "trunk",
                "interest", "steep", "lying", "picture", "block", "pride", "title", "strength", "electric", "feet",
                "gave", "sail", "visitor", "pot", "wood", "thick", "evidence", "lamp", "thank", "trap", "carbon",
                "pond", "shut", "leader", "die", "review", "nation", "neck", "plastic", "lying", "specific", "score",
                "heard", "mark", "lack", "disappear", "rhyme", "club", "upward", "hat", "matter", "too", "arrive",
                "spread", "main", "avoid", "partly", "from", "stared", "good", "various", "science", "equator", "keep",
                "shot", "sharp", "empty", "welcome", "different", "palace", "attempt", "mill", "excited", "nose", "at",
                "cloud", "higher", "writing", "worse", "height", "primitive", "rubber", "feature", "element", "applied",
                "let", "conversation", "present", "ring", "lion", "unknown", "congress", "weather", "sure", "parent",
                "rope", "bring", "friendly", "young", "exclaimed", "prepare", "offer", "brown", "happy", "independent",
                "strange", "dawn", "silly", "smell", "thrown", "bottom", "apart", "married", "score", "service",
                "those", "expect", "evidence", "dream", "probably", "vowel", "one", "direction", "brick", "feed",
                "allow", "iron", "better", "produce", "coat", "earlier", "article", "electricity", "familiar",
                "vessels", "stop", "say", "beneath", "breakfast", "longer", "his", "bush", "motion", "worth",
                "fastened", "with", "active", "control", "whose", "game", "detail", "religious", "occasionally",
                "exercise", "eat", "frequently", "level", "electricity", "born", "poor", "crack", "bill", "classroom",
                "together", "cotton", "finally", "value", "skin", "snow", "electric", "useful", "done", "pressure",
                "surface", "brass", "separate", "length", "on", "or", "pound", "is", "finish", "felt", "bigger", "do",
                "bite", "attention", "century", "raise", "thou", "nearer", "library", "meet", "charge", "break", "ball",
                "whose", "mark", "expression", "support", "breeze", "missing", "porch", "differ", "wear", "pull",
                "since", "policeman", "opinion", "take", "subject", "smile", "tool", "behind", "tone", "both", "wash",
                "court", "speed", "silence", "strike", "bright", "excited", "rock", "occur", "his", "including",
                "exactly", "torn", "settle", "would", "spend", "railroad", "applied", "blank", "attention", "seven",
                "enjoy", "straw", "almost", "feature", "life", "tried", "great", "planned", "pictured", "locate",
                "curve", "rain", "decide", "color", "donkey", "carry", "glad", "think", "yet", "many", "average",
                "court", "heading", "reader", "road", "wife", "origin", "activity", "amount", "leave", "laugh", "farm",
                "person", "if", "needed", "rabbit", "thick", "division", "pet", "organization", "wall", "farmer",
                "electric", "mental", "score", "visitor", "gave", "dirt", "prevent", "ran", "throughout", "basis",
                "partly", "why", "however", "avoid", "proper", "simplest", "ship", "machinery", "small", "pictured",
                "why", "creature", "last", "land", "aid", "felt", "truth", "upward", "fellow", "told", "although",
                "original", "ants", "addition", "valley", "figure", "low", "grandfather", "zoo", "cat", "shop", "bill",
                "machinery", "weather", "alike", "soldier", "buy", "melted", "you", "liquid", "engine", "solar",
                "chain", "given", "planning", "hole", "gently", "entirely", "present", "greatest", "occur", "simplest",
                "high", "circus", "tube", "trail", "pink", "amount", "this", "size", "dollar", "dinner", "gray", "rope",
                "member", "ill", "donkey", "tired", "rest", "citizen", "jungle", "talk", "figure", "tube", "press",
                "wrote", "send", "constantly", "chair", "feathers", "muscle", "laid", "worried", "larger", "usually",
                "proud", "character", "kitchen", "kind", "settlers", "took", "barn", "zoo", "square", "honor", "shoe",
                "muscle", "element", "compare", "stomach", "built", "chicken", "was", "was", "indeed", "sun", "weight",
                "human", "weight", "report", "determine", "wagon", "recently", "use", "final", "hill", "tea", "map",
                "below", "why", "useful", "written", "dear", "hope", "slipped", "help", "neck", "bark", "above", "sale",
                "few", "leave", "between", "liquid", "smell", "no", "size", "difference", "sick", "expect", "greatest",
                "highest", "experiment", "function", "right", "various", "terrible", "aid", "browserling", "sitting",
                "develop", "stay", "lunch", "sold", "ear", "arrangement", "twelve", "relationship", "vapor", "such",
                "smooth", "modern", "sum", "aboard", "street", "cent", "largest", "compound", "hearing", "pocket",
                "thread", "composed", "character", "large", "basket", "am", "composed", "directly", "fastened",
                "ability", "suggest", "gasoline", "herd", "build", "tropical", "angle", "shallow", "compass", "fat",
                "tin", "past", "nothing", "west", "needs", "range", "about", "happy", "instant", "basis", "cage",
                "thirty", "castle", "buried", "series", "be", "sets", "finger", "addition", "whistle", "age", "include",
                "concerned", "bicycle", "story", "clothing", "they", "pure", "warn", "already", "serve", "forty",
                "sweet", "then", "whistle", "close", "usual", "softly", "beyond", "medicine", "chain", "tonight", "up",
                "tune", "due", "clay", "gone", "political", "information", "whistle", "automobile", "depend", "noise",
                "strike", "trade", "stronger", "camp", "name", "secret", "factor", "known", "pie", "having", "birth",
                "room", "price", "board", "blanket", "test", "college", "dig", "asleep", "learn", "pilot", "five",
                "get", "forgotten", "corn", "managed", "trap", "pass", "proper", "cave", "voyage", "shown", "describe",
                "compare", "dark", "remarkable", "dirty", "quiet", "beat", "discussion", "hearing", "world", "car",
                "silent", "similar", "treated", "deal", "bill", "happened", "smell", "known", "quiet", "while",
                "getting", "stage", "strip", "scientific", "once", "success", "likely", "was", "essential", "motion",
                "rate", "hurried"]
