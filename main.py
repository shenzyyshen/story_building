from openai import OpenAI
import os
import emoji
import wikipedia
import random
import textwrap
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init
from termcolor import colored


init()
load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"))

superheroes_list = ['Batman', 'Superman', 'Wolverine', 'Deadpool', 'Green Lantern', 'The Flash', 'Raven', 'Storm',
                    'The Punisher', 'Captain Marvel', 'Jessica Jones', 'Daredevil', 'Elektra', 'Iron Fist', 'Star-Lord',
                    'Groot', 'Gamora', 'Drax the Destroyer', 'Batgirl', 'Green Arrow', 'The Atom']

politicians_list =  ['Barack Obama', 'Angela Merkel', 'Nelson Mandela', 'Donald Trump', 'Winston Churchill', 'Abraham Lincoln',
                     'Mahatma Gandhi', 'Franklin D. Roosevelt', 'Theodore Roosevelt', 'Justin Trudeau', 'Boris Johnson',
                     'Luiz Inácio Lula da Silva', 'Emmanuel Macron', 'Jacinda Ardern', 'Hillary Clinton', 'Bernie Sanders',
                     'Recep Tayyip Erdoğan', 'Narendra Modi', 'Pedro Sánchez', 'Yoon Suk-yeol', 'Ursula von der Leyen',
                     'Jair Bolsonaro', 'Volodymyr Zelenskyy', 'Bill Clinton', 'Dick Cheney', 'Gordon Brown', 'Shinzo Abe',
                     'Yulia Tymoshenko', 'Aung San Suu Kyi', 'Sebastián Piñera', 'Michelle Bachelet', 'Andrés Manuel López Obrador',
                     'Enrique Peña Nieto', 'Nicolás Maduro', 'Alan García', 'Cristina Fernández de Kirchner', 'Mauricio Macri',
                     'Felipe Calderón']

cartoons_list = ['SpongeBob SquarePants', 'Homer Simpson', 'Mickey Mouse', 'Scooby-Doo', 'Daffy Duck', 'Shaggy Rogers',
                 'Garfield', 'Velma Dinkley', 'Plankton', 'Brian Griffin', 'Peter Griffin', 'Morty Smith', 'Kyle Broflovski',
                 'Stan Marsh', 'Kenny McCormick', 'Finn the Human', 'Jake the Dog', 'Bender', 'Philip J. Fry', 'Zoidberg',
                 "Dexter (Dexter's Lab)", 'Dee Dee', 'Samurai Jack', 'Courage the Cowardly Dog', 'Ed (Ed, Edd n Eddy)',
                 'Ben Tennyson', 'Jimmy Neutron', 'Cosmo']

actors_list =  ['Leonardo DiCaprio', 'Meryl Streep', 'Angelina Jolie', 'Johnny Depp', 'Keanu Reeves',
                'Emma Stone', 'Anne Hathaway', 'Chris Hemsworth', 'Julia Roberts', 'Daniel Day-Lewis',
                'Joaquin Phoenix', 'Jessica Chastain', 'Nicole Kidman', 'Cate Blanchett', 'Charlize Theron',
                'Jake Gyllenhaal', 'Austin Butler', 'Diego Luna', 'Timothée Chalamet']


def welcome():

    """Welcomes the player and states the rules of the game"""

    book_emoji = emoji.emojize(":open_book:")
    writing_emoji = emoji.emojize(":writing_hand:")
    print()
    print(Style.BRIGHT+ Back.BLACK + Fore.YELLOW+f"---------{book_emoji}Welcome to StoryBuilding!{writing_emoji}---------")
    print()

    print("In this game you will choose a character and build your own story! You will\n"
          "have the option to choose a genre and topics to include in the story. Have fun!\n")



def user_character(selected_list):

    sample_of_characters = random.sample(selected_list,4)
    print()
    print("----Whose destiny would you like to write?----\n")

    for i, character in enumerate(sample_of_characters, 1):
        print(f"{i}. {character}")

    while True:
        try:
            players_character = int(input("Choose your character: "))
            print()
            if  1 <= players_character <= 4:
                print(f"You chose {sample_of_characters[players_character - 1]}")
                return sample_of_characters[players_character - 1]
            else:
                print("Please choose a number between 1 and 4")
        except ValueError:
            print("Invalid input")



def user_genre():
    """pick 1 genre from four pre-defined options (list),
    return the genre selected"""

    predefined_genre = {
    1: "Romance 🌹",  # Rose emoji
    2: "Sci-fi 👽",   # Alien emoji
    3: "Horror ☠️",   # Skull emoji
    4: "Comedy 🤣",   # Laughing emoji
    5: "Fantasy 🔮"   # Crystal emoji
    }

    print()
    print("----Which story genre would you like to use?----\n")

    for key, value in predefined_genre.items():
        print(f"{key}. {value}")

    players_genre = int(input("Your choice: \n"))

    return players_genre


def user_min_number_articles():
    """The user selects how many Wikipedia links to go through and connect
    to each other to further define the story"""

    while True:
        try:
            num_articles = int(input("How many Wikipedia topics would you like to include in your story? (Between 1 and 4):  "))
            if 1 <= num_articles <= 4:
                return num_articles
            else:
                print("Sorry, the number of articles you have entered is not between 1 and 4")
        except ValueError:
            print("Not a valid number, please try again")


def story_build(character, genre, num_articles):
    character_page_text, character_page_links = character_content(character)

    print("Now select a page link\n")

    generate_story_parts(character, genre, character_page_text, character_page_links, num_articles)



################ Helper functions ################
def character_content(character):
    character_page = wikipedia.page(character)  # full page
    character_text = character_page.summary
    character_wiki_links = character_page.links
    return character_text, character_wiki_links


def select_article(page_links):

    while True:
        options = random.sample(page_links, 4)

        link_options = {i+1:link for i, link in enumerate(options)}
        #both link_options = the same

        #link_options = {}
        #for i, link in enumerate(options):
            #link_options[page_links[i+1]] = link
        print("--------Write your next chapter--------\n")

        for key, value in link_options.items():
            print(f"{key}. {value}")

        selected_link = int(input("Choose a topic to add to the story: \n"))

        selected_topic = link_options[selected_link]
        article_page = wikipedia.WikipediaPage(selected_topic)
        page_text = article_page.content
        page_links = article_page.links

        return selected_topic, article_page, page_text, page_links



def generate_story_parts(character, genre, character_intro, character_links, num_articles):
    current_status_story = ""
    current_links = character_links
    current_title = character

    for i in range(num_articles):
        selected_topic, article_page, page_text, new_links = select_article(current_links)

        if i == 0:
            current_status_story = ai_start_story(character, genre, character_intro, page_text)
        else:
            current_status_story = ai_continous_story(current_status_story, genre, page_text)

        print()
        print(Style.BRIGHT+ Back.BLACK + Fore.CYAN +current_status_story)
        print(Fore.YELLOW)

        current_links = new_links
        current_title = selected_topic

    while True:
        user_input = input("Would you like to continue to work on your story or finish it? [C] to continue or [F] to Finish ").lower().strip()
        print()
        if user_input == "c":
            selected_topic, article_page, page_text, page_links = select_article(current_links)
            current_status_story = ai_continous_story(current_status_story, genre, page_text)

            print()
            print(Style.BRIGHT+ Back.BLACK + Fore.CYAN + current_status_story )
            print(Fore.YELLOW)

            current_links = new_links

        elif user_input == "f":
            ai_end_story(current_status_story, genre)
            break
        else:
            print("Please enter 'C' or 'F'")


def ai_start_story(character, genre, character_intro, topic):

    prompt = (
        f"You are a creative storyteller tasked with writing a fictional story in the **{genre}** genre. "
        f"Emphasize the unique traits of this genre while keeping the story internally consistent and stylistically appropriate.\n\n"
        f"Stay as much as possible in the **{genre}** genre. .\n\n"
        f"The story is based on the character **{character}**. It begins with the following two sentences, taken from their Wikipedia page:\n"
        f"**{character_intro}**\n\n"
        f"After these two sentences, start a new paragraph and begin building the story.\n\n"
        f"This will be the **first part** of the story. The story will continue over time as I provide new topics.\n"
        f"For each topic, you'll continue by adding **exactly 3 new sentences**.\n\n"
        f"Each addition must logically build upon the previous content, without rewriting or removing anything already written. "
        f"Use a simple, engaging tone suitable for a wide audience, and be consistent with the genre’s themes and style.\n\n"
        f"The story should feel light, fun, and easy to follow — you can include **familiar clichés** from the genre and make the story a bit silly, exciting, or unusual.\n"
        f"Here is your first topic to expand the story: **{topic}**\n\n"
        f"Start now by generating the **first part** of the story, including the character intro and your continuation. "
        f"Keep the total length under **80 words**."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "user", "content": prompt}
        ]
    )

    print("--------This is how your story begins:--------\n")

    return textwrap.fill(response.choices[0].message.content, width=100)





def ai_continous_story(current_status_story, genre, topic):

    prompt = (
         f"You are a creative storyteller. Your task is to write a fictional story in the **{genre}** genre, "
        f"You can add a twist OR classic genre-style finish — just keep it light, easy to read, and enjoyable.\n\n"
         f"Stay as much as possible in the **{genre}** genre. .\n\n"
        f"The story should begin with the following two sentences taken from the character's Wikipedia page: **{current_status_story}**. "
        f"The story will grow step by step: I will provide three topics in total, each based on a Wikipedia link related to the main character. "
        f"For each topic I provide, you will continue the story by adding **exactly 3 new sentences**. "
        f"Each time you add to the story, always build on the existing text and connect the new content logically — **never rewrite or remove previous parts**. "
        f"The writing style should be simple and easy to understand, suitable for a broad audience. "
        f"At the end, the full story should read as one cohesive piece of fiction, centered around the original character. "
        f"Here is the first topic to expand the story: **{topic}**. "
        f"Keep the tone fun and easy to follow. You can add silly or classic genre ideas — it should feel like a smooth and light continuation.\n\n"
        f"Start the story now, including the intro and your continuation. The total length should not exceed **80 words** at this point."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "user", "content": prompt}
        ]
    )

    print("--------This is the continuation of your story:--------\n")

    return textwrap.fill(response.choices[0].message.content, width=100)



def ai_end_story(current_status_story, genre):

    prompt = (
        f"You are a creative storyteller. Your task is to write a fictional story in the **{genre}** genre, "
        f"Stay as much as possible in the **{genre}** genre. .\n\n"
        f"The story should feel light, fun, and easy to follow — you can include **familiar clichés** from the genre and make the story a bit silly, exciting, or unusual.\n"
        f"The story should begin with the following two sentences taken from the character's Wikipedia page: **{current_status_story}**. "
        f"The story will grow step by step: I will provide three topics in total, each based on a Wikipedia link related to the main character. "
        f"For each topic I provide, you will continue the story by adding **exactly 3 new sentences**. "
        f"Each time you add to the story, always build on the existing text and connect the new content logically — **never rewrite or remove previous parts**. "
        f"The writing style should be simple and easy to understand, suitable for a broad audience. "
        f"At the end, the full story should read as one cohesive piece of fiction, centered around the original character. "
        f"Start the story now, including the intro and your continuation. The total length should not exceed **80 words** at this point."

    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "user", "content": prompt}
        ]
    )

    ending = textwrap.fill(response.choices[0].message.content, width=100)
    print()
    print("\n--------This is your final story--------\n")
    print(Style.BRIGHT+ Back.BLACK + Fore.CYAN+ending)
    print(Fore.YELLOW)






def main():
    welcome()
    while True:
        while True:
            user_input = input("Select the category: superheroes 🦸️, politicians 💼, cartoons 🖍️ or actors 🎥: ").lower().strip()
            if user_input == "superheroes" or user_input == "s":
                user_selection = superheroes_list
                break
            elif user_input == "politicians" or user_input == "p":
                user_selection = politicians_list
                break
            elif user_input == "cartoons" or user_input == "c":
                user_selection = cartoons_list
                break
            elif user_input == "actors" or user_input == "a":
                user_selection = actors_list
                break
            else:
                print("Please enter a valid input \n")

        selected_character = user_character(user_selection) #Select the character
        selected_genre = user_genre() #Select the genre
        minimum_articles = user_min_number_articles() #Select how many articles to include
        story_build(selected_character, selected_genre, minimum_articles) #range = user_min_number_articles

        play_again = input("Would you like to build another story? [Y] or [N] ").lower().strip()
        print()
        if play_again == "n":
            print("🏁 Thank you for playing! See you next time.")
            break


if __name__ == "__main__":
    main()




