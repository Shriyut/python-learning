# composition is used to model a HAS A relationship
# inheritance is used to model a IS A relationship
# benefit of composition is that it creates separation between your objects

class Paper:
    def __init__(self, text, case):
        self.text = text
        self.case = case

class BriefCase:
    def __init__(self, price):
        self.price = price
        self.papers = []

    def add_paper(self, paper):
        self.papers.append(paper)

    def view_notes(self):
        return [paper.text for paper in self.papers]

class Lawyer:
    def __init__(self, name, briefcase):
        self.name = name
        self.briefcase = briefcase

    def write_note(self, text, case):
        paper = Paper(text, case)
        self.briefcase.add_paper(paper)

    def view_notes(self):
        print(self.briefcase.view_notes())

# python will infer briefcase object as long as it is present

cheap_briefcase = BriefCase(price=19.99)
sunny = Lawyer(name="sunny", briefcase=cheap_briefcase)

sunny.write_note("My client is XYZ", "1")
sunny.write_note("OK", "1")
sunny.view_notes()