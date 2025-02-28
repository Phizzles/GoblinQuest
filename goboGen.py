from dataclasses import dataclass
import random
import tkinter as tk

#=============================================================================#
#================================== CLASSES ==================================#
@dataclass
class Gobo:
    """Gobo class"""
    name:str
    skill:str
    weapon:str

    def __str__(self):
        return f'{self.name} who {self.skill} wielding {self.weapon}.'

class GoboGen2000:
    """Class to generate gobos with random names, skills, and weapons"""
    def __init__(self, names1:list[str], names2:list[str], skills:list[str], weapons:list[str]):
        self.names1 = names1
        self.names2 = names2
        self.skills = skills
        self.weapons = weapons
    
    def generate_gobo(self) -> list[str]:
        """Returns a list with the name, skill, and weapon of a gobo"""
        return Gobo(random.choice(self.names1) + random.choice(self.names2), 
                random.choice(self.skills), 
                random.choice(self.weapons))


#=============================================================================#
#================================= FUNCTIONS =================================#
def load_list_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


#=============================================================================#
#=================================== MAIN ====================================#
def main():
    ### LOAD DATA ###
    names1 = []
    names2 = []
    skills = []
    weapons = []

    names1 = load_list_from_file('names1.txt')
    names2 = load_list_from_file('names2.txt')
    skills = load_list_from_file('skills.txt')
    weapons = load_list_from_file('weapons.txt')
    
    ### CREATE GOBO GENERATOR ###
    gobo_gen = GoboGen2000(names1, names2, skills, weapons)
    for _ in range(10):
        print(gobo_gen.generate_gobo())

    ### TKINTER GUI ###
    GUI_TEXT_SIZE = 24
    GUI_TEXT_FONT = "Helvetica"

    def update_gobo(index):
        gobos[index].set(str(gobo_gen.generate_gobo()))

    root = tk.Tk()
    root.title("Gobo Generator")

    # Set background image
    background_image = tk.PhotoImage(file="images/background_2.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    gobos = [tk.StringVar() for _ in range(4)]
    for i in range(4):
        frame = tk.Frame(root, bg='white')
        frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(frame, textvariable=gobos[i], font=(GUI_TEXT_FONT, GUI_TEXT_SIZE), anchor='w', bg='white').pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(frame, text="Reroll", command=lambda i=i: update_gobo(i), font=(GUI_TEXT_FONT, GUI_TEXT_SIZE), bg='white').pack(side=tk.RIGHT)

    for i in range(4):
        update_gobo(i)  # Initialize with random gobos

    root.mainloop()

if __name__ == '__main__':
    main()