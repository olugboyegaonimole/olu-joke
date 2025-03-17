from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend (change to ["http://localhost"] for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# List of clean jokes
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "What did the fish say when it hit the wall? Dam!",
    "Why don’t eggs tell jokes? They might crack up!",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
    "Why do cows have hooves instead of feet? Because they lactose!",
    "Why did the golfer bring an extra pair of pants? In case he got a hole in one!",
    "Why are frogs so happy? They eat whatever bugs them!",
    "Why can’t your nose be 12 inches long? Because then it would be a foot!",
    "What do you call cheese that isn’t yours? Nacho cheese!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don’t oysters donate to charity? Because they are shellfish!",
    "Why was the math book sad? It had too many problems!",
    "How do you organize a space party? You planet!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What kind of shoes do ninjas wear? Sneakers!",
    "How do you catch a squirrel? Climb a tree and act like a nut!",
    "Why couldn’t the leopard hide? Because he was always spotted!",
    "What do you call fake spaghetti? An impasta!",
    "What do you call a can opener that doesn’t work? A can’t opener!",
    "Why did the chicken go to the séance? To get to the other side!",
    "What did one plate say to the other? Tonight, dinner’s on me!",
    "What did the janitor say when he jumped out of the closet? Supplies!",
    "What do you call a factory that makes good products? A satisfactory!",
    "Why did the football team go to the bank? To get their quarterback!",
    "How does a penguin build its house? Igloos it together!",
    "Why don’t mountains ever get tired? Because they peak all the time!",
    "What kind of key opens a banana? A monkey!",
    "Why did the orange stop? Because it ran out of juice!",
    "What kind of music do mummies listen to? Wrap music!",
    "Why was the belt arrested? For holding up pants!",
    "What did one snowman say to the other? Do you smell carrots?",
    "How do you make holy water? You boil the hell out of it!",
    "Why did the teddy bear say no to dessert? Because he was stuffed!",
    "Why couldn’t the pony sing? He was a little hoarse!",
    "Why did the baker go to therapy? He kneaded it!",
    "Why did the banana go to the doctor? It wasn’t peeling well!",
    "What do you call a sleeping bull? A bulldozer!",
    "Why don’t skeletons go trick-or-treating? They have no body to go with!",
    "What do you call a cow in an earthquake? A milkshake!",
    "Why did the coffee file a police report? It got mugged!",
    "What do you call a fish with no eyes? Fsh!",
    "Why don’t seagulls fly over the bay? Because then they’d be bagels!",
    "Why did the clock get kicked out of class? It tocked too much!",
    "How do trees access the internet? They log in!",
    "Why don’t ants get sick? They have tiny ant-bodies!",
    "Why was the calendar so good at his job? He had a lot of dates!",
    "What do you get when you cross a snowman and a vampire? Frostbite!",
    "Why did the man put his money in the blender? He wanted liquid assets!",
    "Why do birds fly south for the winter? Because it’s too far to walk!",
    "What did the grape do when it got stepped on? Nothing, it just let out a little wine!",
    "Why do skeletons stay so calm? Because nothing gets under their skin!",
    "What do you call an alligator in a vest? An investigator!",
    "Why was the broom late? It swept in!",
    "What do you call a pig that does karate? A pork chop!",
    "Why did the musician get arrested? He got caught with a high note!",
    "Why don’t bakers play hide and seek? Because they always get found!",
    "What do you call an elephant that doesn’t matter? An irrelephant!",
    "What kind of vegetable is cool but not that cool? Rad-ish!",
    "What did one ocean say to the other ocean? Nothing, they just waved!",
    "Why do ducks make great detectives? They always quack the case!",
    "What do you call a snowman in summer? A puddle!",
    "What do you call a sleeping dinosaur? A dino-snore!",
    "Why was the cat sitting on the computer? To keep an eye on the mouse!",
    "What do you call a nervous javelin thrower? Shakespeare!",
    "Why couldn’t the angle get a loan? Because he was too obtuse!",
    "Why did the barber win the race? He knew all the short cuts!",
    "How do cows stay up to date? They read the moos-paper!",
    "Why do vampires always seem sick? They’re always coffin!",
    "What’s orange and sounds like a parrot? A carrot!",
    "Why was Cinderella so bad at soccer? She kept running away from the ball!",
    "Why don’t spiders go to school? Because they learn on the web!",
    "How do you fix a broken tomato? Tomato paste!",
    "Why did the banana break up with the orange? It found them un-peeling!",
    "What kind of jokes do elevators tell? Uplifting ones!",
    "Why do melons get married? Because they cantaloupe!",
    "What do you call a deer with no eyes? No-eye-deer!",
    "What do you call a belt made out of watches? A waist of time!",
    "Why did the skeleton start a band? He had great bones!",
    "Why do cows go to space? To see the moooon!",
    "What’s brown and sticky? A stick!",
    "Why don’t basketball players go on vacation? They might get called for traveling!",
    "What does a cloud wear under its pants? Thunderwear!",
    "Why did the tomato sit down? It was feeling saucy!",
    "What do you call a lazy kangaroo? A pouch potato!",
    "What did the big flower say to the little flower? Hi, bud!",
    "What do you call an avocado that went to church? Holy guacamole!",
    "Why did the ghost go to school? To improve his boo-k smarts!",
    "Why did the elephant bring a suitcase? Because he wanted to pack his trunk!",
    "Why do skeletons never lie? They always tell the bare bones truth!",
    "Why do fish live in saltwater? Because pepper makes them sneeze!",
    "How do you make a lemon laugh? Tell it a citrus joke!",
    "Why did the cow cross the road? To get to the udder side!",
    "Why did the baker break up with the dough? It was too kneady!",
    "Why don’t eggs play soccer? They’re afraid of getting scrambled!",
    "What do you get when you cross a dog and a calculator? A friend you can count on!",
    "Why did the chicken go to the library? To check out a book-bawk-bawk!"

]

# Root Endpoint for API Status Check
@app.get("/", include_in_schema=False)
@app.head("/")
def root():
    return {"message": "Welcome to the Joke API!"}

@app.get("/joke")
def get_joke():
    return {"joke": random.choice(jokes)}

