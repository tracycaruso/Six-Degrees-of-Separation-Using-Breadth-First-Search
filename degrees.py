import csv
import sys

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


class Node():
    def __init__(self, action, state, title, name, parent):
        self.action = action
        self.state = state
        self.parent = parent
        self.title = title
        self.name = name

    def __str__(self):
        return (f'action: {self.action}: {self.title}, state: {self.state}: {self.name}, parent: {self.parent}')


class Queue():
    def __init__(self, frontier, explored):
        self.frontier = frontier
        self.explored = explored

    def is_empty(self):
        return len(self.frontier) == 0

    def add(self, node):
        self.frontier.append(node)

    def add_to_explored(self, node):
        self.explored.append(node)

    def remove(self):
        return self.frontier.pop(0)


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)
    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        prin?"(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            movie = movies[path[i + 1][0]]["title"]  # path[1][0] : 112384
            person1 = people[path[i][1]]["name"]  # path[0][1] : 158
            person2 = people[path[i + 1][1]]["name"]  # path[1][1] : 102

            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def previously_recorded(queue, actor):
    return any(x for x in queue if x.state == actor)
        
def create_nodes(queue, person_id, parent):
    movie_list = neighbors_for_person(person_id)

    for movie, actor in movie_list:
      in_frontier = previously_recorded(queue.frontier, actor)
      in_explored = previously_recorded(queue.explored, actor)

      if not in_frontier and not in_explored:
        title = movies[movie]['title']
        name = people[actor]['name']
        queue.add(Node(movie, actor, title, name, parent))


def shortest_path(source, target):
  name = people[source]['name']
  start = Node(None, source, None, name, None)
  queue = Queue([start], [])

  while(True):
    if(queue.is_empty()):
        raise Exception('No solution')

    current_node = queue.remove()
    queue.add_to_explored(current_node)
    print(current_node)
    if current_node.state == target:
        steps = []
        while current_node.parent is not None:
          steps.append((current_node.action, current_node.state))
          current_node = current_node.parent

        steps.reverse()
        return steps
    else:
        create_nodes(queue, current_node.state, current_node)


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
