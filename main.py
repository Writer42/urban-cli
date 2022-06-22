
import json
import sys
from typing import Dict, List
from request import get_definition

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.padding import Padding

console = Console()


def clean_api_text(string: str) -> str:
    new_string = ''
    new_string = string.replace("[", "{").replace("]", "}")
    new_string = new_string.replace("{", "[green u]").replace("}", "[/]")
    return new_string


class Card:

    def __init__(self, article: Dict) -> None:

        self.author = article["author"]
        self.word = article["word"]
        self.definition = clean_api_text(article["definition"])
        self.example = clean_api_text(article["example"])

    def get_card(self) -> Group:
        card = Panel(Group(
            f"[red bold]{self.word}[/] by [cyan bold]{self.author}[/]:",
            Padding(self.definition, (1, 4)),
            Text("Example:", style='red bold'),
            Padding(self.example, (1, 4))
        ))
        return card


if __name__ == "__main__":
    print_number = 3
    urban_response = get_definition(input())
    st = json.loads(urban_response.text)
    cards: List[Card] = []
    with open("resp.json", "w") as f:
        if not st["list"]:
            print("Sorry, found nothing")
            sys.exit()
        for el in st["list"]:
            del el["sound_urls"]
            cards.append(Card(el))

        for i in range(print_number):
            try:
                print(cards[i].get_card())
            except IndexError:
                break

        json.dump(st, f, indent=2)
