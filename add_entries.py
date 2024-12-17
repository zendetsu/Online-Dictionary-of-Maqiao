from app import db, DictionaryEntry
from app import app

    # Example entries
entries = [
        DictionaryEntry(
            word="River",
            page_number=1,
            definition="江,Vast bodies of water, but to all waterways, including small ditches and streams.",
            example="""Although Magiao people later on became more specific about size, they
still didn’t seem to attach much importance to it, only differentiating it
slightly by tone. Gang pronounced in a high, level tone refers to a large
river, and ina rising tone toa rivulet or stream; it takes some time for outsiders
to attune their ears to avoid misunderstandings. As a newcomer to
Maagiao,I ran into such difficulties myself when I went off in excited
search ofa river, following directions from locals. My destination turned
out to be a gurgling brook so narrow I could reach the other side in one
flying leap. Some dark waterweed lay within and watersnakes would flash
by unannounced, but for washing or swimming it was of no use.
Rising-tone gang is very different from high-tone gang. Following this
rising-tone gang for a stretch, I wandered alternately between torrents
and calm, and then back to torrents. I felt myself scattering in pieces
then coming together again, as if repeatedly lost, then found.""",
            related="Luo River"
        ),
        DictionaryEntry(
            word="Luo River",
            page_number=2,
            definition="The river into which Maqiao's water flowed.",
            example="""There was a little rowboat for crossing, and
if the boatman wasn’t there then people wanting to cross simply rowed
themselves over. If the boatman was there, it cost five cents per person.(...)In fact, the river in summer was much wider, and the water
much more turbulent. If it happened to be the flood season, the bottomless
brown soup overflowed unstoppably, obscuring all reflections,
expelling layer upon layer of mire onto the banks, along with soursmelling
piles of foam which the slow lapping of the water marooned on
the shallow bends. But the worse the conditions became, the more people
gathered on the riverbanks, patiently waiting for dead ducks, dead
pigs, broken tables or old wooden pots, along with bamboo canes split
off from bundles, to come bobbing along: fishing them out and taking
them off home was called “making a flood fortune.""",
            related="Savages (Savages of the Luo Clan)"
        ),

	DictionaryEntry(
	    word="Maqiao Bow",
	    page_number=10,
	    definition="The full name for Maqiao. Bow means village, including the land covered by a village: it's obviously a traditional unit of area, one \"bow\" representing the stretch of land covered by the trajectory of an arrow.",
	    example="""It’s said that Magiao (literally “Horsebridge”) Bow was originally
spelled differently, with the characters meaning “Motherbridge” Bow,
but the only evidence is an old title deed. Maybe this is just a spelling
mistake left over from the past. Thanks to the establishment of a fairly
clear system of record-taking in the modern era, the changes to its name
can be roughly summarized as follows:
— before 1956, called Maqiao Village, part of Tianzi Township;
— from 1956 to 1958, called Magiao Group, part of Dongfeng
Cooperative;
— in 1958, called 22nd production team, part of Changle People’s
Commune (Large Commune);
— from 1959 to 1979, called Maqiao Production Team, part of
Tianzi People’s Commune (Small Commune);
— since 1979, when the People’s Communes were disbanded, up to
the present day, Maqiao Village, along with a section of Tianzi
Township, has become part of Shuanglong Township.""",
	    related="Old Chum"
	),

	DictionaryEntry(
            word="Sweet",
            page_number=17,
            definition="Anything tastes good. The word “sweet” exposes a Magqiao blind spot with respect to food and drink, demarcating the boundaries of their knowledge in this area.",
            example="""Sugar is “sweet,” fish and meat are also “sweet,” boiled rice, chilli
pepper, bitter gourds are all “sweet.”(...)Similarly, there is only one name for all sweet foods: “candy.” Candied
fruits are “candy,” biscuits are “candy, sponge cake, shortcake, bread,
cream, absolutely everything is “candy.” The first time they saw popsickles
in Changle, they called them “candy” too. There are, of course, exceptions:
the specialities of the region each have their own name, for example
“glutinous rice cake” and “rice cake.”""",
            related="Tincture of Iodine"
        ),

	DictionaryEntry(
            word="Tincture of Iodine",
            page_number=20,
            definition="The scientific term that everyone in Maqiao used.",
            example="""Even old grannies
with clouded vision and foggy hearing talked in a more scholarly tone
than I did. When they pronounced “tincture of iodine” in their Maqiao
accent, it was as if they'd unconsciously uttered a secret code, a code that
normally remained buried out of sight, only spoken in times of dire
necessity, to make contact with the remoteness of modern science.(...)I finally discovered that this term was linked to one mysterious
person.
Uncle Luo, the old village leader of the lower village, told me as he
sucked on his bamboo pipe that a person called Long Stick Xi was the
first person to use the phrase “tincture of iodine” here.""",
            related="Rough"
        ),

	 DictionaryEntry(
            word="Little Big Brother",
            page_number=31,
            definition="""Big sister. Clearly, by the same token, “little little brother” means little sister,
“Jittle paternal uncle” means an aunt on the father’s side; “little maternal
uncle” means an aunt on the mother’s side, and so on. (...) Language, it seems, is never absolutely objective or neutral. A linguistic
space will always be distorted under the influence of a particular set
of beliefs. Bearing in mind the namelessness of females, it’s easy to draw
further conclusions about their social status around here; it’s easy to
understand why they always bound their chests flat, crossed their legs
tightly, and lowered their eyes timidly onto steps or short grass, harboring
a deep-felt fear and shame that sprang from their status as females.""",
            example="""English has never
been masculinized to the same degree as Maqiao dialect, where female
terms were completely deleted. I’ve had great difficulty in working out
whether this linguistic misrepresentation had any influence on the sexual
psychology or even sexual biology of Maqiao women—whether it
had to any degree altered reality. From the looks of things, the women all
seemed to use coarse, vulgar language, had even learned how to fight and
curse. Once they gained the upper hand in relation to a man, they often
became complacent. Their hands and faces were hardly ever clean,
hardly ever fresh and bright, and their bodies were always hidden in
masculine clothing that covered their female figures with loose, straight
pants or stiff, rough-padded jackets. They were also embarrassed to talk
about menstruation, and referred to it as “that thing.” “That thing,”
again, is no kind of name. When I was laboring in the paddy fields, I
hardly ever saw a woman ask to rest because of her period.""",
            related="Placing the Pot"
        ),

	 DictionaryEntry(
            word="Science",
            page_number=42,
            definition="Being lazy. The implications of the word \"Scientific\", once projected onto Ma Ming, were far from positive. To put it another way, science became an extension of the general mockery of the Daoist Immortals.",
            example="""“Tt’s not that we won't carry it, we just want to carry it a bit more scientifically.”
“What d’you mean scientific? You mean lazy! Those city automobiles,
railroads, flying machines of yours—name me one that hasn’t been
thought up by a lazybones! Who else but lazybones would’ve thought up
such a devilish set of names?”
This outburst quite took my breath away.
He went on: “With all these scientific comings and goings, we'll all be
like Ma Ming before you know it.” (...) He was referring to the owner of the House of Immortals. Ma Ming,
its resident-in-chief, had never come out to work, didn’t even want to see
to his own needs. Sometimes he would bring back a bit of gourd, but he
was too lazy to light a fire, so he would eat it raw. He’d got used to eating
things raw like this, and so when he’d scavenged out some uncooked
rice, he’d put it straight into his mouth and crunch away on the grains
until the corners of his mouth were a mass of powdery rice starch. People
would laugh at him, but still he came up with justification after justification,
saying that cooked things lacked nutritional value; that tigers
and panthers in the mountains had always eaten their food raw, and see
how much stronger they were than humans, how much less prone to illness—
so*what could be wrong with it?""",
            related="House of Immortals (and Lazybones)"
        ),
	 DictionaryEntry(
            word="Awakened",
            page_number=45,
            definition="Stupid. Someone awakened is a stupid fool. Maqiao people have long used this word, spat out with a disdainful wrinkling of the nose and thinning of the lips, to refer to all kinds of idiotic behavior. This use of the word “awakened” to mean “ignorant” or “stupid” is a fossil seam running through the unique history and beliefs of the Luo people.",
            example="""In c.278 b.c., Qu Yuan the Awakened, Qu Yuan the self-proclaimed
member of the Awakened, unable to tolerate the drunken disorder prevailing throughout the world, resolved to make a martyr of himself, and
to oppose evil through death. He threw himself into the Miluo River (the
lower reaches of the Luo River) and drowned—in the area nowadays
called Chutang township, where he went after having been condemned
to exile. (...) His eventual death
at the side of the Miluo river, leaving behind a vast, empty riverbank,
meant that he must have received some fundamental shock which
induced in him a feeling of terror towards the yet vaster life that existed
beyond life, a feeling of unassailable confusion at the yet vaster history
that existed beyond history. The only thing he could do was to take a
step into the unknown.
Where else could he have experienced such a dazzlingly rude—awakening?
Where else could he have come to understand better his long-prized
sense of —awakening?(...)Qu Yuan never saw this glory, and in any case, not just any aspiring
Qu Yuan could win this glory. Looking at things from the opposite angle,
the way in which Magiao people understood and used the word “awakened”
concealed another viewpoint, concealed the dislike of their forefathers
for the politics and foreign culture of a powerful state, concealed
the necessary ambiguity between different historical positions.""",
            related="Asleep"
        ),

	 DictionaryEntry(
            word="Asleep",
            page_number=49,
            definition="Clever. The character pronounced jue in Mandarin is pronounced go in the Magqiao accent, with a rising tone, and its meaning is the opposite of the Maqiao meaning of \"awakened\"",
            example="""“Awakened” and “asleep” are antonyms. Directly opposed to normal
understanding in standardized Chinese thinking, this pair of antonyms
exchanged places when their meanings were extended in Magiao: as
Madgiao people see it, regaining consciousness is stupid, while sleeping is
in fact clever. This inversion always sounded rather odd to outsiders who
were new to the village.
We have to allow that different people will judge cleverness and stupidity
from different angles and using different yardsticks. We must, it
seems, also permit that Maqiao people are perfectly entitled to draw
from their own experience original metaphors from “awakened” and
“asleep.” Take Ma Ming: people can sigh about what a down-and-out he
was, and laugh at how he was smelly and stubborn and crazy and stupid
and how he lived, quite frankly, like a dog. But if we look at things from a different angle? From Ma Ming’s angle? Far from lacking happiness or
unfettered freedom, his existence could often be compared even with
that of the immortals. And if we consider how act upon act of bitter farce
have played themselves out: the Great Leap Forward, the Anti-Rightist
Movement, the Cultural Revolution . . . far too much human brilliance
dissipated into absurdity, far too much diligence turned into mistakes,
far too much enthusiasm diverted into wrongdoing; at least Ma Ming,
this distant onlooker, remained pure and unblemished, with no trace of
blood on his hands. Even with all the natural hardships he endured, he
lived to be healthier than most. Now, does that make him stupid or clever?
Was he “awakened” or “asleep”?""",
            related="Awakened"
        ),

	DictionaryEntry(
            word="Jackal-Fiend",
            page_number=195,
            definition="A jackal-fiend was a jackal fish, another name for which was jackal mute. Maqiao people said this fish didn’t eat plants but other fish; it was the fiercest of all fish, but could also at times be the most stoic: people could tread over it for months on end without it moving.",
            example="""Once, my traveling
companion asked me if I'd noticed anything different last time I
crossed the stream. I paused to think, then said I hadn't. Think again,
he said. I thought again, and still said I hadn’t. D’you remember a big,
long rock in the water? he asked. I couldn’t remember, and only his
repeated promptings brought back a vague recollection. The last time
Id crossed the stream, there seemed to have been a long rock, probably
near a clump of water willow in the middle of the current, that Pd
stepped on, even squatted down on to drink a couple of mouthfuls of
water. Maybe.
My companion smiled. That wasn’t a rock, he said. Oh no. The last
time the river was up, a few young oxherders on the mountain had spotted
that long rock suddenly stand erect, stir up a murky whirlpool in the
stream, then travel downstream with the floodwater—turned out it'd
been alive: a jackal-fiend.""",
            related=""
        ),

	DictionaryEntry(
            word="Precious",
            page_number=196,
            definition="“Precious” meant stupid; “preciousness” meant stupidity.",
            example="""Zhihuang’s preciousness was renowned throughout all Maqiao. For example, he didn’t understand you had to give up your seat to cadres, he didn’t
understand how to fake when tamping down earth, it took him a very
long time to figure out that women have periods every month. That he
used to beat his wife so violently showed how precious he was. His wife
later divorced him and went back to her family home in Pingjiang, but
from time to time he’d send the dream-woman food and clothing—this
showed he was even more precious.""",
            related="Lion Dance, Three-Hairs"
        ),

	DictionaryEntry(
            word="Born-to-the-Pen",
            page_number=213,
            definition="Oxen that had been brought up like family, oxen that ox-rustlers found hard to steal away.",
            example="""Although Three-Hairs
had something of a foul temper, it was still an ox born-to-the-pen.
Two months before it died, nothing had been seen of it for two days,
the team leader had sent people searching everywhere with no result,
and everyone thought it’d never be found again, that it’d already been
slaughtered or sold by ox-rustlers. But on the evening of the third day,
while I was playing chess at Zhihuang’s, Zhihuang unexpectedly turned
back from relieving himself and said his ox whip was twitching on the
wall, there was definitely something up, definitely. Maybe Three-Hairs
had come back. (...) After escaping from the ox-rustlers it must have meandered
all over the mountains on its long, long tramp home.""",
            related="Three-Hairs"
        ),

	DictionaryEntry(
            word="Three-Hairs",
            page_number=207,
            definition="A fearsome ox over whom, in all Maqiao, only \"Precious\" Zhihuang had any jurisdiction.",
            example="""When most people wanted to catch oxen, they all went
“chuh—chuh—chuh”; only Zhihuang used “slippy—slip slip” to catch
Three-Hairs. “(...)The problem was that sometimes Zhihuang had to go to the
quarry—particularly after autumn, when things got pretty busy there.
After he’d left, no one dared use Three-Hairs. One time, though, I
decided to try my luck at copying Zhihuang’s way of “slipping” it.(...)Three-Hairs seized this opportunity to have some fun with me. The
farther away we were from the live electric wires, the more the animal
tripped and gamboled, the more unresponsive and unstoppable it
became, however hard I pulled.(...)The plough handle flew out of my hands, the pointed ploughshare
swung forward and, like the merciless falling of an axe, stuck itself
straight into one of Three-Hairs’ back legs.(...)Three-Hairs wasn’t sold, but died at the hands of Zhihuang, in a finale
that no one would have predicted. He staked his own honor on Three-
Hairs: if this beast injured anyone again, he declared, he’d take the axe to
it himself. He couldn't go back on what he’d said. One spring day, when
everything in the world was sprouting back to life, sounds and colors
shifting under the warm sunlight, a secret disquiet pervaded the air. Just
as Zhihuang was driving Three-Hairs down the field, suddenly the animal’s
whole body shuddered, its eyes fixed straight ahead, and with a
yank of the ploughshare it charged forward insanely, tramping the mud,
smack-smack-splatter, into a rising and falling curtain of water.
Caught unawares, Zhihuang eventually identified Three-Hairs’ target:
a red dot at the side of the road. It was only afterwards that he found
out it’d been a woman passing by from a neighboring village wearing a
jacket with red flowers on it.(...)Three-Hairs was still shedding tears.
Zhihuang, his face totally expressionless, finally picked up the axe
and walked over— A dull thump.
The ox’s head split into a rivulet of blood, followed by a second, a
third. ... Even when the fountain of blood had spurted a foot high, the
ox still put up no resistance, didn’t even call out, still kept its kneeling
position. Finally, it swayed briefly, leaned to one side, then collapsed
heavily, like a mud wall splaying over the ground.""",
            related="Born-to-the-Pen"
        ),

	DictionaryEntry(
            word="Rude",
            page_number=215,
            definition="Pretty. “Rude” in Magiao language was also widely used to mean excellence, to tower above others, to stand out from your peers, surpass the norm, and so on.",
            example="""The first time I heard this word was when crossing the Luo
River in flood season, when the river was a few times wider than usual.
On the same boat were two unfamiliar women, probably from distant
regions, who covered their faces with bamboo hats once they’d boarded
the boat, exposing no more than a pair of eyes. The boatman sized them
up briefly, then waved at them to get off. The two women had no choice
but to get off and smear their faces with mud till they looked like painted
actors; doubling up with laughter at the sight of each other, they finally
got back on the boat, still convulsed with giggles.(...)A very
particular rule held on this crossing: in times of high winds or turbulent
waters, women who weren't ugly weren't allowed to cross. Legend had it
that a very long time ago an ugly woman from around here who could
never get married had ended up throwing herself to her death off this
pier into the river. The ugly woman’s soul didn’t then scatter: she only
had to spot an attractive woman on a boat to whip the wind into jealous
waves, causing endless accidents in which boats were destroyed and lives
lost.(...)It’s this word “rude”
that I’m interested in. It conceals within an assumption that provokes an
involuntary shiver: beauty is a form of evil, good is a form of danger,beautiful and good things will always bring disunity, instability, dissatisfaction,
disputes, and animosity—rudeness.""",
            related="Spirit"
        ),

	DictionaryEntry(
            word="Spirit",
            page_number=217,
            definition="""Maqiao people used the word “spirit” to describe any kind of unconventional behavior. People from around here were anxious above all else to affirm
human ordinariness, to affirm that humans were conventional beings.
Any unconventional behavior was, essentially, inhuman behavior,
derived from the mysterious shadows of the netherworld, from superhuman
forces of heaven or destiny. If the problem wasn’t a spiritual
(i.e., mental) matter, then it had to be a matter of spirits (i.e., ghosts or
divinities). Maqiao people used the word “spirit” for both these two
meanings, probably considering the difference between the two to be of
little importance. Any story about spirits began with fantasies of a spiritually
abnormal nature.(...)A whole bundle of expressions—“spirit-fast,”
“spirit-brave,’ “spirit-good,” “spirit-weird, “spirit-pretty,’ “spiritsmooth”—
referred to achievements that temporarily transgressed ordinary
human limits, often witnessed in people close to the obsessive
derangement of spiritual disorder, close to the spirits, and who were
putting their mental state to positive use, either subconsciously or
unconsciously.""",
            example="""Benyi and Tiexiang went to the government office to register [their marriage]. The government
office said she was too young, she should come back in two
years. When it became clear that nothing she said was having any effect,
her apricot eyes hardened and she told the secretary who handled official
seals: “If you don’t register us, I won’t go, I’ll have the kid at your
place and say it’s yours. How’d you like that?” The secretary jumped in
terror and scrambled to sort everything out, the sweat running down his
face. He watched their back-views—hers and her bridegroom’s—recede
far off into the distance, his mind still unhinged with fear: that spirit
woman, he said, d’you think she’ll stay like that?(...)A spirit like Tiexiang’s, everyone said, just had to be possessed by evil forces.""",
            related="Rude"
        ),

	DictionaryEntry(
            word="Official's Road",
            page_number=383,
            definition="""Narrow roadway paved with stone, twisting and turning as it stretched over the mountains to Maqiao. it wasn’t just any old pathway that got to be called an “officials’
road.” I'd guess its history went something like this: way back in the past,
someone from the village who'd left to take up an official post elsewhere
had needed to ride back home to visit his elders; a good road being thus
essential, his first act as an official was to build a road to his home village,
an officials’ road.""",
            example="""Officials’ roads were usually built by convicts. The
official would allocate punishment through differing lengths of construction
work, according to the respective gravity or levity of a crime:
one hundred or two hundred feet, and so on. The construction of roads
was not only a testament to wealth and honor: their growth rested on the
crimes of bygone days.
Neither the officials nor criminals of Maqiao’s past left their names to
posterity.
As time went by, it fell into disrepair: some of the stone slabs shattered,
or simply disappeared entirely. The fragments remaining sank
into the surrounding topsoil, with only the part not yet grown over still
poking out, trampled to a slippery gleam by passing bare feet, like a row
of human spines lubricated with oil and sweat, eternally subjugated
below our feet.""",
            related=""
        ),

	DictionaryEntry(
            word="Democracy Cell(as Used by Convicts)",
            page_number=333,
            definition="""To convicts, the democracy cell was the most terrifying thing of all,
when a prison king hadn’t yet emerged, or when victory and defeat
between two or three prison kings remained undecided—that was no
life at all. One stray comment and there’d be shouting and fighting;
you'd be doing pretty well to keep your eyes, nose, hands and feet on
after a few months in a democracy ....""",
            example="""[Kuiyuan said,] “I was unlucky, this time I got into a democracy cell...”
I didn’t understand.
“I only survived by the skin of my teeth.”
“What d’you mean, democracy cell?”“Don’t you know what a democracy cell is?”
“T’ve never committed a crime.”
“It’s just ... it’s just ... everyone’s democratic, right.”
“What’s that mean?”
“Democracy means lice, bedbugs, fights, blood, lots of them.”
I still didn’t understand.(...)A newcomer had no choice but to fall into line. If you weren't prepared
to follow the fiat of the prison king, the Daoist Immortals or those
convicts in waiting for promotion as Daoist Immortals would soon beat
you half to death. This was called “softening you up.” Or they’d stick you
in the frame, show the guards in charge of discipline a nail or razor blade
to prove you'd broken prison rules, and you'd end up in chains or with a
yoke round your feet. He said although a prison king was pretty vicious,
in a prison king's cell, people were usually quite law-abiding, generally
there was al eader in everything, there were no group fights, things were
kept fairly clean and hygienic, the towels hung up neatly, the quilts
folded one on top of another, which kept the disciplinary cadres happy.""",
            related="Bubbleskin (etc.), Kuiyuan"
        ),

	DictionaryEntry(
            word="Brutal",
            page_number=341,
            definition="Capable, Skillful, a high level of technical know-how. The problem is, brutal at the same time implies ruthless, vicious, malicious.",
            example="""Being able to write nicely was brutal, knowing a lot of characters was
brutal, helping the team leader fix the grain threshing machine was brutal,
being able to dive down and fill in the leaks in the pond was brutal,even factories from barbarian parts that manufactured appliances, diesel
oil, chemical fertilizers, and sheet plastic (and therefore, of course, the
workers) were clever, were brutal. When Magiao people talked like this,
maybe they were unaware that they were implicitly relegating knowledge
and skill to the category of moral corruption, of savagery.
I suspect that, according to their past experience, people with a grasp
of some particular knowledge or skill possessed a natural tendency
toward violence and terror. The first time they saw a piece of rumbling
machinery, it dropped Japanese bombs on them from the sky; the first
time they saw a radio amplifier, it cut off their “capitalist tails” by confiscating
their own private land. What was there to reassure them that clever
people they later encountered wouldn't do them similar sorts of harm?""",
            related="Strange Talent"
        ),

	DictionaryEntry(
            word="Strange Talent",
            page_number=343,
            definition="""Maqiao dialect has another term for people who
demonstrate great ability: “strange talent.” The Origins of Words (Commercial
Book Center, 1988) gives three definitions for guai, the word for
“strange” in Mandarin: the first is bizarre or unique; the second is particularly,
extremely, very—presumably the gradual evolution of the first
meaning into a function word; the third is censure, blame. From the
looks of it, in Chinese bizarre things are forever linked with censure and
blame, are perilously out of the ordinary.""",
            example="""Magiao’s “strangest talent” was Yanwu.(...)When I next saw him, a while on, he’d changed to studying Chinese
medicine: quite the expert he looked, treating people with acupuncture
and taking their pulse. Afterwards, he studied portrait painting and
carving as well—it was said he sold paintings and calligraphy in
Changle and in the county, as well as carved Chairman Mao’s poems in
plain and cursive calligraphy on customers’ fountain pens, while-youwait
and at a fair price. In short, there was nothing much he couldn't
turn his hand to, nothing that could prevent him from showing off the
superlative strangeness of his talent. The fame of his strange talent
spread far and wide until everyone, both old and young, knew of him.
Even though he was a “traitor to the Chinese” (see the entry “Traitor to
the Chinese”), Maqiao people never bore any ill feeling toward him and
were always very tolerant of his frequent mysterious journeying outside
the village.
Quite the contrary: he was the pride of Maqiao, the communal pride
of all the villages and stockades massed around the environs of Maqiao
Bow. """,
            related="Brutal"
        ),

	DictionaryEntry(
            word="Kuiyuan(spelled with lack or loss)",
            page_number=354,
            definition="Kuiyuan's name, but with the character meaning \"lack\" or \"loss\" instead of the character meaning \"chief\", or \"great\".This “loss” kui was deeply inauspicious and dripped with animosity— even though it was probably only a result of momentary carelessness and laziness on the part of the invitation writer. “I'll give his mother a good sticking!”",
            example="""He was going to call Yanwu’s family to account, he
told his family. In fact, after he went out he first of all went and sat in
Zhihuang’s house for a while, than went to the vegetable garden at
Fucha’s house to nibble on a cucumber, then ended up going to the front
of Tiananmen, where he watched some young men play ping-pong, then
watched some more young men play a table of mahjong—he didn’t dare
go looking for Yanwu. He was even afraid of Yanwu learning he’d come
to make trouble.(...)Kuiyuan stuffed the electric drill up his shirt, scooped up
two socket boards while he was at it and slipped out of the main gate(...)Kuiyuan felt another sharp pain in his behind.
He led the three men to the sweet potato patch, scratched away at the
topsoil with his hands, took out the electric drill and the socket board(...)“Hey, Wang, go fetch your fucking ear—”
This piercing, booze-soaked scream was Kuiyuan’s.
“You bastard Wang, that’s what happens if you don’t listen to your
betters, your ear ends up going to the dogs—”
It was obvious that Kuiyuan’s knife had cut up the wrong person.
“Kui you bastard, youre going to get it now, you got the wrong person!”
someone shouted out nearby.""",
            related="Stick(y) (Nia)"
        ),
]


    # Commit changes to the database
with app.app_context():
    db.session.add_all(entries)  # Add all entries at once
    db.session.commit()
    print("Entries successfully added!")
