"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# Ten pieces I wrote myself. Criterion 1 uses all ten; criteria 2 and 5 reuse
# them as their human samples (1-5 for criterion 2, 6-10 for criterion 5).
MY_WRITING = [
    "Sociologically, this is kind of bizarre to me. I don't know many people who read short stories "
    "outside of school, or listen to them as audiobooks, and short stories don't seem to have the "
    "audience size of novels, podcasts, or other long-form content.\n\n"
    "But our attention spans seem to be shrinking, and we seem to be preferring shorter and shorter "
    "content. And everyone I know complains that they don't have enough time to read anymore. I "
    "honestly love short stories because I can enjoy a plot and feel accomplished within whatever odd "
    "pocket of time I have; there isn't the commitment of a novel or, even worse, a series. And free "
    "short story podcasts mean I can listen to a short story during any odd drive to a nearby town.\n\n"
    "I'm curious to hear other people's thought on the matter! It just puzzles me that the shortening "
    "of other medias isn't happening to fiction writing as much.",

    "Josh Silver's new book Fruit Fly has an inciting incident where the main character Googles \"how "
    "to write a best selling novel.\" She lands on a Reddit thread that instructs her to \"go gay, go "
    "dark, and make people cry.\" Being that we are all currently on Reddit, I think it's our "
    "responsibility to make sure anyone who tries to mimic this Google search can find a Reddit "
    "thread with similarly genius tips to write a bestseller. So let's use this thread to share all "
    "our great advice with the good people from Google.",

    "I had something interesting happen to me last night, and I'm curious to see if the same has "
    "happened to any of you as well at one point or another. Overhearing a random comment while doing"
    " something else entirely, my brain went into \"Remember that time when...?\" mode and it found me "
    "looking at an old screenplay I had started many years back now, but never got around to "
    "finishing. As I was reading it, I got to the part where a certain character was introduced and "
    "my eyes near jumped out of my face. On the page is a character I wrote in 2023. Who just so "
    "happens to be pretty much the same character I just finished writing in 2026 for a novel. But, a"
    " character I totally forgot I created.",

    "In my writing journey I realized that a lot of my stuff uses a lot of big words, and I only used"
    " because I didn't see them any different than \"small words\", but recently in my writing class, "
    "when my story was getting reviewed, they said I sounded pretentious. And then I could only "
    "wonder, for all that I've written, why so? I just like really abstract things, but it prevents "
    "me from having writing partners or connecting well with others in the class. I could not say "
    "anything to these people, but I left the class so confused, because, I just assumed since they "
    "were in college level they'd know them, aside from the words that were made up from my enjoyment"
    " of experimenting. But yeah, I'm just trying to not seem arrogant, and once I dumbed down the "
    "words in my next story, they liked it... and I was even more confused.",

    "I’ve been writing on and off for almost six years now. I genuinely enjoy it, and I feel like "
    "it’s something I find myself in. I’ve tried writing dozens of stories, but I’ve never managed to"
    " finish one. I can’t quite figure out what the problem is. All I know is that lately, I’ve been "
    "experiencing what people call writer’s block most of the time (I don’t really believe in it, but"
    " whatever the hell this is, it’s got me pretty badly stuck) I keep planning endlessly instead of"
    " just letting the story flow. But when I do let it flow, it somehow loses its meaning. On the "
    "other hand, I find it hard to let go of an idea, as if it deserves to be there simply because it"
    " came to mind in the first place. I also think I might struggle with the actual act of creating "
    "something from scratch. If you’ve ever finished a story, or gone through something similar, I’d "
    "really appreciate it if you shared your experience.",

    "So some time back I finished the first draft of my novel, and decided to take a break for a "
    "while. I planned on start working on marketing the novel after that through instagram, since I "
    "do have a lot of writer friends there. The problem was that I would have to have that and my "
    "personal stuff, since I don't want to bother switching between two accounts, and like I said, I "
    "have a lot of writer friends there and a bit of 'starter support'. This wouldn't be a problem in"
    " itself but I also have a few family members who follow me on instagram and I haven't told them "
    "about me wanting to be a writer and stuff and I'm scared of telling them that and if I post "
    "anything related to writing, they would be able to see that. Does anyone have any advice for "
    "this?",

    "Here's an interesting discussion I've been wondering about for a while: what sort of level of "
    "vocabulary do y'all think is appropriate? I'm a writer myself, and I'd say I have a decently "
    "average/slightly above-average vocabulary. But I've been reading a book recently where, "
    "legitimately, I was looking up a word on my phone every 2 minutes or so. My question is: what "
    "are people's thoughts on using super advanced vocabulary? On the one hand, sure, it's a good "
    "flex that you have a good vocabulary and kinda gives your writing professionalism. But on the "
    "other...I feel like it's just...unecessary? Like, obviously you want at least a semi-advanced "
    "vocab for your writing, but it's the structure and the formation of your writing that makes it "
    "good, not fancy words. I feel like using super advanced vocabulary, words that even decently "
    "intelligent people aren't going to have a clue what they mean, is just, like...showing off? And "
    "it makes it a little frustrating for readers when they CONSTANTLY have to look up what the hell "
    "you're talking about?",

    "Use the words that are naturally part of your vocabulary. If you have an advanced vocabulary, "
    "use an advanced vocabulary unless you're specifically writing something that's inappropriate. If"
    " you don't have an advanced vocabulary, trying to use one will likely come off as artificial and"
    " false. I know everybody has a dictionary in their pocket now, but a lot of us grew up where, "
    "look, sometimes you read a word that you didn't know the meaning of, and you didn't really have "
    "a choice but to figure out what you could from context and plow ahead. We managed just fine. One"
    " of my favorite books answers the final dramatic question of the story with two words that are "
    "in a foreign language that I don't speak. (At the time, I wasn't sure if it was French or Latin,"
    " and this was before online translation.) It worked.",

    "Right now, I'm loosely plotting what will either be Book 11 or Book 12. Without giving a lot "
    "away, a lot of it will be set in my hometown, which is a small town in NEPA, while some scenes "
    "will be based at/around Syracuse U. (I'm geographically between them) Most times, I set my "
    "scenes/books in bigger/Metro areas, like Tampa, Vegas, LA-centric, NYC, etc. I really want to "
    "set this book in a small town, because there are so many 'culture clashes' and comparative "
    "dynamics I can explore... But I don't want to really paint the town in a negative light. (They "
    "do enough of this on their own. *smirk*) How would you handle this? Would you make up a name of "
    "the town to avoid possible defamation?\nor would you use the actual town and hope for the best "
    "from the residents?",

    "I'm a college student in a workshop class with a very accredited author as my professor. Not too"
    " big, but he's accomplished. He says a lot of weird stuff, but something kind of bugged me about"
    " him. He has this weird gripe with the word \"as,\" and thinks it shouldn't be used often. Like: "
    "\"She approached me as I got up.\" He gave a reason I can't fully remember (he rambles a lot, this"
    " was one of his many asides), but it was something to do with flow and that it should rarely be "
    "used. Obviously, you shouldn't use something too much, but with the way he said it was like you "
    "should never use it. Which is weird, because... I don't see anything wrong or confusing about "
    "it? I tried looking this up for other people's opinions, but there aren't many results. Note, I "
    "don't have this professor anymore and it was about two months ago, but it stuck with me. I "
    "noticed it a lot in my writing and a lot of books I've read and trimmed down on it, but I still "
    "think it's useful. Am I crazy?",
]

# Five AI-generated samples (written by Claude for this test).
AI_SAMPLES = [
    "Remote work has fundamentally transformed the modern workplace. By eliminating daily commutes, "
    "employees can reclaim valuable time and achieve a healthier work-life balance. Organizations, in "
    "turn, benefit from access to a broader talent pool and reduced overhead costs. However, remote work "
    "also presents unique challenges, including communication barriers and feelings of isolation. To "
    "address these issues, companies should invest in collaborative tools and foster a strong culture of "
    "connection. Ultimately, a thoughtful approach to remote work can unlock significant benefits for "
    "both employees and employers.",

    "Regular physical activity offers numerous benefits for both physical and mental health. Exercise "
    "strengthens the cardiovascular system, improves muscle tone, and helps maintain a healthy weight. "
    "In addition, physical activity has been shown to reduce symptoms of anxiety and depression by "
    "releasing endorphins. Experts recommend at least 150 minutes of moderate exercise each week. By "
    "incorporating simple activities such as walking, cycling, or swimming into their daily routines, "
    "individuals can significantly improve their overall well-being and quality of life.",

    "Climate change is one of the most pressing challenges facing humanity today. Rising global "
    "temperatures are leading to more frequent extreme weather events, melting ice caps, and rising sea "
    "levels. These changes pose significant risks to ecosystems, agriculture, and human communities. "
    "Addressing climate change requires a coordinated global effort, including the transition to "
    "renewable energy sources, improved energy efficiency, and sustainable land use practices. By "
    "working together, governments, businesses, and individuals can help mitigate its impacts.",

    "Reading is a valuable habit that offers a wide range of benefits. It expands vocabulary, improves "
    "concentration, and enhances critical thinking skills. Furthermore, reading exposes individuals to "
    "diverse perspectives and cultures, fostering empathy and understanding. Whether it is fiction or "
    "nonfiction, regular reading can stimulate the mind and reduce stress. To cultivate a reading habit, "
    "individuals should set aside dedicated time each day and choose books that align with their "
    "interests. Over time, reading can become an enjoyable and enriching part of daily life.",

    "Effective time management is essential for achieving personal and professional goals. By "
    "prioritizing tasks, setting clear objectives, and minimizing distractions, individuals can increase "
    "their productivity and reduce stress. One popular technique is the Pomodoro method, which involves "
    "working in focused intervals followed by short breaks. Additionally, using tools such as calendars "
    "and to-do lists can help individuals stay organized. Ultimately, mastering time management allows "
    "people to make the most of their time and maintain a healthy balance between work and life.",
]

# Five borderline samples: AI-generated (by Claude), then written in a looser,
# more personal voice so they sit between the two.
BORDERLINE_SAMPLES = [
    "I started working from home two years ago and honestly it's been mostly good. No commute, which "
    "is huge. I get more done in the mornings. The downside is that some days I don't talk to anyone "
    "until my partner gets home, and that gets old. I've started going to a coffee shop on Thursdays "
    "just to be around people. It helps more than I expected.",

    "My doctor told me to walk more, so I've been doing thirty minutes after dinner most nights. The "
    "first week was rough. Now I kind of look forward to it. I sleep better and I'm less snacky in the "
    "evening, which I didn't see coming. I'm not going to pretend I've become a fitness person, but "
    "it's a habit now and it feels like a good one.",

    "We had a drought last summer and the town put in watering restrictions for the first time anyone "
    "can remember. People were annoyed at first. Then the creek behind the school dried up completely "
    "and nobody complained much after that. It made climate change feel a lot less abstract. I've been "
    "reading more about it since, trying to figure out what actually helps.",

    "I used to read all the time as a kid and then just stopped somewhere in college. This year I set "
    "a goal of one book a month. I'm on track, mostly. Fiction is easier for me to stick with than "
    "nonfiction. The best one so far was a mystery my sister recommended. Reading before bed instead of "
    "scrolling has been a nice change.",

    "I tried the Pomodoro thing for a week. Twenty-five minutes on, five off. It worked better than I "
    "thought it would for boring tasks like email and expense reports. For anything that needs real "
    "focus, the timer just interrupted me right when I got going. So now I use it for the boring stuff "
    "only. Small change, but my afternoons feel less wasted.",
]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },
    {
        "name": "spread ai",
        "criterion": 2,
        # Compared against "spread human": mean AI score minus mean human score.
        "texts": AI_SAMPLES,
    },
    {
        "name": "spread human",
        "criterion": 2,
        "texts": MY_WRITING[:5],
    },
    {
        "name": "bad input",
        "criterion": 3,
        # Raw request bodies, sent exactly as written. Each should get a 400.
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t ", "creator_id": "eval_bad_whitespace"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": ["a", "list"], "creator_id": "eval_bad_list"},
            {"text": "a", "creator_id": "eval_bad_one_char"},
        ],
    },
    # Criterion 4 (appeals) can't be tested with text alone. It needs a
    # submission and then an appeal against the content_id that came back, so
    # it runs separately: python run_appeals.py --label before
    {
        "name": "label coverage",
        "criterion": 5,
        # 15 inputs across the score range: 5 AI, 5 borderline, 5 human.
        "texts": AI_SAMPLES + BORDERLINE_SAMPLES + MY_WRITING[5:],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
