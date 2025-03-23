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
    "Why did the bicycle stand on its own? Because it was two-tired!",
    "Why did the golfer bring an extra pair of socks? In case he got a hole in one!",
    "Why don’t calendars get tired? They have too many dates!",
    "What kind of tree fits in your hand? A palm tree!",
    "Why did the mushroom go to the party? Because he was a fungi!",
    "Why did the barber win the race? He knew all the short cuts!",
    "Why do hummingbirds hum? Because they don’t know the words!",
    "Why did the cookie go to the doctor? It was feeling crumbly!",
    "Why do potatoes make good detectives? Because they keep their eyes peeled!",
    "How do bees get to school? They take the buzz!",
    "Why don’t crabs give to charity? Because they’re shellfish!",
    "Why was the belt arrested? It was holding up a pair of pants!",
    "What’s a skeleton’s least favorite room? The living room!",
    "What do you call a parade of rabbits hopping backward? A receding hare-line!",
    "Why did the stadium get so hot? All the fans left!",
    "How do you catch a unique rabbit? Unique up on it!",
    "What’s a cat’s favorite color? Purrr-ple!",
    "Why don’t vampires like jokes? Because they suck at them!",
    "Why did the fisherman bring a ladder? Because he wanted to go to the next level!",
    "Why was the computer cold? It left its Windows open!",
    "Why did the clock go to therapy? Because it had too many issues!",
    "What do you call a rabbit who tells jokes? A funny bunny!",
    "What do you call a boomerang that won’t come back? A stick!",
    "Why did the duck sit down at the restaurant? To quack open the menu!",
    "Why do gorillas have big nostrils? Because they have big fingers!",
    "What do you call a bear caught in the rain? A drizzly bear!",
    "What did the peanut say when it sneezed? Cashew!",
    "Why did the dog sit in the shade? Because he didn’t want to be a hot dog!",
    "Why was the broom late? It swept in!",
    "Why was the library so tall? It had so many stories!",
    "Why did the tomato blush? Because it saw the salad dressing!",
    "What’s a snake’s favorite subject? Hisss-tory!",
    "Why did the chicken go to space? To see the egg-straterrestrial!",
    "Why don’t trees ever get lost? Because they always take the root!",
    "Why did the book join the police? Because it wanted to go by the book!",
    "What did one hat say to the other? Stay here, I’m going on ahead!",
    "Why did the banana go to the party? Because it was a-peeling!",
    "How do you organize a fantastic party? You planet!",
    "Why don’t shoes make good comedians? They always get tongue-tied!",
    "What do you call a lazy kangaroo? A pouch potato!",
    "Why did the grape stop in the middle of the road? Because it ran out of juice!",
    "Why do fish always know how much they weigh? Because they have their own scales!",
    "What did the traffic light say to the car? Don’t look, I’m changing!",
    "Why did the rabbit go to school? To learn hare-ithmetic!",
    "Why don’t birds use social media? They already tweet!",
    "Why did the farmer win an award? Because he was outstanding in his field!",
    "Why did the corn start telling jokes? Because it was a-maize-ing!",
    "What do you call a pig who does karate? A pork chop!",
    "Why did the grape get stepped on? Nothing, it just let out a little wine!",
    "What’s a baker’s favorite type of music? Rock and roll!",
    "Why did the sunflower feel so bright? Because it was full of sun!",
    "What kind of pants do ghosts wear? Boo-jeans!",
    "Why did the lemon stop rolling? Because it ran out of juice!",
    "How do cows stay informed? They read the moos-paper!",
    "Why do books love the library? Because that’s where their stories begin!",
    "What’s a sheep’s favorite game? Baa-dminton!",
    "Why don’t trees fight? Because they leaf each other alone!",
    "What do you call a pig that plays basketball? A ball hog!",
    "Why did the duck take up meditation? To find his inner quack!",
    "What did the thunder say to the lightning? You crack me up!",
    "Why did the little fish get bad grades? Because he was below sea level!",
    "What’s a skeleton’s favorite instrument? The trom-bone!",
    "Why do baseball players make great bakers? Because they know how to batter!",
    "Why was the soccer player so good at math? He knew how to use his head!",
    "What’s a ghost’s favorite dessert? Boo-berry pie!",
    "What do you get when you cross a snowman and a dog? Frostbite!",
    "Why did the hen stay up all night? Because she was egg-cited!",
    "What did the cloud say to the sun? You brighten my day!",
    "Why did the puppy sit next to the clock? Because he wanted to be a watch dog!",
    "What do you call a singing vegetable? A beet-boxer!",
    "Why did the tree go to the dentist? It needed a root canal!",
    "Why was the detective so good at his job? Because he always followed the clues!",
    "Why don't skeletons fight each other? They don’t have the guts!",
    "What did the fish say when it hit the wall? Dam!",
    "Why don’t eggs tell jokes? They might crack up!",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
    "Why do cows have hooves instead of feet? Because they lactose!",
    "Why are frogs so happy? They eat whatever bugs them!",
    "Why can’t your nose be 12 inches long? Because then it would be a foot!",
    "What do you call cheese that isn’t yours? Nacho cheese!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don’t oysters donate to charity? Because they are shellfish!",
    "Why was the math book sad? It had too many problems!",
    "What kind of shoes do ninjas wear? Sneakers!",
    "How do you catch a squirrel? Climb a tree and act like a nut!",
    "Why couldn’t the leopard hide? Because he was always spotted!",
    "What do you call fake spaghetti? An impasta!",
    "What do you call a can opener that doesn’t work? A can’t opener!",
    "Why did the chicken go to the séance? To get to the other side!",
    "What did one plate say to the other? Tonight, dinner’s on me!",
    "What do you call a factory that makes good products? A satisfactory!",
    "Why did the football team go to the bank? To get their quarterback!",
    "How does a penguin build its house? Igloos it together!",
    "Why don’t mountains ever get tired? Because they peak all the time!",
    "What kind of key opens a banana? A monkey!",
    "Why did the orange stop? Because it ran out of juice!",
    "What kind of music do mummies listen to? Wrap music!",
    "How do trees access the internet? They log in!",
    "Why don’t ants get sick? They have tiny ant-bodies!",
    "Why was the calendar so good at his job? He had a lot of dates!",
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

