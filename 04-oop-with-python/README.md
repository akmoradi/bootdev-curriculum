# Learn OOP

## CH2: Classes

### Classes
A class is a special type in an object-oriented programming like Python and it's kinda like a dictionary in that it usually stores key-value pairs:

```Python
# Define a new class called "soldier"
# with three properties: health, armor, damage
class soldier:
    health = 5
    armor = 3
    damage = 2
``` 

```Python
class Archer:
    health = 40
    arrows = 10

# Create several instances of the Archer class
legolas = Archer()
bard = Archer()

# Print class properties
print(lagos.health)     # 40
print(bard.arrows)      # 10
```


### Methods

```Python
class soldier:
    health = 5

    # This is a method that reduces
    # the health of the soldier
    def take_damage(self, damage):
        self.health -= damage

soldier_one = soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"

soldier_two = soldier()
soldier_two.take_damage(1)
print(soldier_two.health)
# prints "4"
```

### Methods Can Return

```Python
class soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self)
    speed = 10
    speed -= self.armor
    speed -= self.num_weapons
    return speed

soldier_one = soldier()
print(soldier_one.get_speed())
# prints "6"
```

```Python
class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        return self.armor * self.height

    def fortify(self):
        self.armor *= 2
```


### Methods vs Functions

```Pyhon
class soldier:
    health = 100

    def take_damage(self, damage, multiplier):
        # "self" is dalinar in the first example
        damage = damage * multiplier
        self.health -= damage

dalinar = soldier()
# damage and multiplier are passed explicitly as arguments
# 20 and 2, respectively
# 'dalinar' is passed implicitly as the first argument, "self"
dalinar.take_damage(20, 2)
print(dalinar.health)
# prints "60"

adolin = soldier()
# Again, adolin is passed implicitly as the first argument, "self"
# damage and multiplier are passed explicitly as arguments
adolin.take_damage(10, 3)
print(adolin.health)
# prints "70"
```

### Constructors

```Python
class soldier:
    name = "Lefolas"
    armor = 2
    num_weapons = 2
```

A _constuctor_ is a specific method on a class called __init__ that is called automatically when you create a new instance of a class.

```Python
class soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2
```

Not only is this safer, but it also allows to make the starting property values configurable:

```Python
class soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier_one = soldier("Legolas", 2, 10)
print(soldier_one.name)
# prints "Legolas"
print(soldier_one.armor)
# prints "2"
print(soldier_one.num_weapons)
# prints "10"

soldier_two = soldier("Gimli", 5, 1)
print(soldier_two.name)
# prints "Gimli"
print(soldier_two.armor)
#prints "5"
print(soldier_two.num_weapons)
# prints "1"
```

Add a constuctor to the Wall class.

```Python
class Wall:
    def __init__(self, depth, height, width)
    self.depth = depth
    self.height = height
    self.width = width
    self.volume = depth * height * width
```

### Assignment
Take a look at the Brawler class and the fight function provided, then complete the main function by doing the following:

- Create 4 new brawlers with the following stats:
    - Name: Aragorn. Speed: 4. Strength: 4.
    - Name: Gimli. Speed: 2. Strength: 7.
    - Name: Legolas. Speed: 7. Strength: 7.
    - Name: Frodo. Speed: 3. Strength: 2.
- Call fight twice:
    - The first fight should be Aragorn (attacker) vs Gimli (defender).
    - The second will be Legolas (attacker) vs Frodo (defender).

```Python
def main() -> None:
    aragorn = Brawler("Aragorn", 4, 4)
    gimli = Brawler("Gimli", 2, 7)
    legolas = Brawler("Legolas", 7, 7)
    frodo = Brawler("Frodo", 3, 2,)

    fight(aragorn, gimli)
    fight(legolas, frodo)


class Brawler:
    def __init__(self, name: str, speed: int, strength: int) -> None:
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        
    def fight(attacker: Brawler, defender: Brawler) -> None:
        print(f"{attacker.name}: {attacker.power} power")
        print(f"{defender.name}: {defender.power} power")
        if attacker.power > defender.power:
            print(f"{attacker.name} wins!")
        elif attacker.power < defender.power:
            print(f"{defender.name} wins!")
        else:
            print("It's a tie!")
        print("------------------------------")

main()
```

```Python
class Archer:
    def __init__(self, name: str, health: int, num_arrows: int) -> None:
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self) -> None:
        self.health -= 1
        if self.health <= 0:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target: "Archer") -> None:
        if self.num_arrows == 0:
            raise Exception(f"{self.name} can't shoot")
        
        print(f"{self.name} shoots {target.name}")
        self.num_arrows -= 1
        target.take_hit()
```

### Classes Practice

```Python
class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self. author = author


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: book) -> None:
        new_books: list[Book] = []
        for lib_book in self.books:
            if lib_book.title != book.title or lib_book.author != book.author:
                new_books.append(lib_book)
        self.books = new_books

    def search_book(self, search_string: str) -> list[Book]:
        results: list[Book] = []
        for book in self.books:
            if (
                search_string.lower() in book.title.lower() 
                or search_string.lower() in book.author.lower()
            ):
                results.append(book)
        return results
```

### Encapsulation

Encapsulation if the practice of hiding complexity inside a "black box" os that it's easier to focus on the problem at hand.

```Python
class Wizard:
    def __init__(self, name: str, stamina: int, intelligence: int) -> None:
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        
        self.health = self.__stamina * 100
        self.mana = self.__intelligence * 10
```












### Inheritance
Inheritance allows a "child" class to inherit properties and methods from a "parent" class. It's a way to share code between classes. 

```Python
class Aircraft:
    def __init__(self, height: int, speed: int) -> None:
        self.height = height
        self.speed = speed

    def fly_up(self) -> None:
        self.height += self.speed
```

```Python
class Helicopter(Aircraft):
    def __init__(self, height: int, speed: int) -> None:
        self.height = height
        self.speed = speed
        self.direction = 0

    def fly_up(self) -> None:
        self.height += self.speed

    def rotate(self) -> None:
        self.direction += 90
```

We can make Helicopter a child of Aircraft:

```Python
class Helicopter(Aircraft):
    def __init__(self, height: int, speed: int) -> None:
        super().__init__(height, speed)
        self.direction = 0

    def rotate(self): -> None:
        self.direction += 90
```

The super(). method returns a proxy of the parent class, meaning we can use it to call the parent class's constructor and other methods.

```Python
class Jet(Aircraft):
    def __init__(self, speed: int) -> None:
        # Jets always start on the ground
        super().__init__(0, speed)

    def go_supersonic(self) -> None:
        self.speed *= 2
```

#### Assignment
In Age of Dragons, all the archers are humans, but not all humans are necessarily archers. All humans have a name, but only archers have a __num_arrows property.

Complete the Archer class. It should inherit the Human class.

1. Its constructor should:
    - Call the parent constructor
    - Set the private __num_arrows property based on the constructor parameter
1. Its get_num_arrows(self) -> int method should return the number of arrows the archer has.


```Python
class Human:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name


class Archer(Human):
    def __init__(self, name: str, num_arrows: int) -> None:
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self) -> int:
        return self.__num_arrows
```

#### When to Inherit

Inheritance is a powerful tool, but don't overuse it. 

- Rul of thumb: A should inherit from B if A is _always_ a B. 
- In other words: A child class is a _strict_ subset of its parent class.
- When a child class inherits from a parent, it inherits _everything_. If you only want to share _some_ functionality, inheritance should **not** be the tool you use.


#### Inheritance Hierarchy

There is no (technical) limit to how deeply we can nest an inheritance tree.

Let's add a new game unit: Crossbowman.

```Python 
class Human:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name


class Archer(Human):
    def __init__(self, name: str, num_arrows: int) -> None:
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self) -> int
        return self.__num_arrows

    def use_arrows(self, num: int) -> None:
        if num > num_arrows:
            raise Exception("not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name: str, num_arrows: int) -> None:
        super().__init__(name, num_arrows)

    def triple_shot(self, target: Human) -> str
        self.use_arrow(3)
        target_name = target.get_name()
        return f"{target_name} was shot by 3 crossbow bolts"
```


#### Multiple Children

```Python
class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.__name = name
        self.__healthg = health

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__heatlh

    def take_damage(self, damage: int) -> None:
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name: str, health: int, num_arrows: int) -> None:
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target: Hero) -> None:
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
            self.__num_arrows -= 1
            target.take_damage(10)

class Wizard(Hero):
    def __init__(self, name: str, health: int, mana: int) -> None:
        super().__init__(name, health)
        self.__mana = mana

    def cast(self, target: Hero) -> None:
        if self.__mana <= 25:
            return Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)
```

### Dragons

#### Assignment

Complete the following methods:

Complete the unit's in_area method. It accepts an "area" represented by four coordinates: x_1, y_1, x_2, and y_2. The coordinates x_1 and y_1 represent the bottom-left corner, while x_2 and y_2 represent the top-right corner.
Determine if the unit is within the given area by using the unit's position coordinates pos_x and pos_y.
Return True if the unit's position falls inside or on the edge of the rectangle. Otherwise, return False.
Complete the dragon's breathe_fire method. It causes the dragon to breathe a swath of fire at the target area.
The target area is centered at (x, y). The area stretches for __fire_range in both directions inclusively.
Iterate over each unit in the units list, and check if the unit is in the area. If it is, add it to a new list that keeps track of the units hit by the blast.
Return the list of units hit by the blast.

```Python
class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1: int, y_2: int, x_2: int, y_2: int) -> bool:
        if (x_1 <= pos_x <= x_2) and (y_1 <= pos_y <= y_2):
            return True
        return False


class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int) -> None:
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breath_fire(self, x: int, y: int, unit: list[Unit]) -> list[Unit]:
        units_smoked: list[Unit] = []
        for unit in units:
            if unit in area(
                (x - self.__fire_range),
                (y - self.__fire_range),
                (x + self.__fire_range),
                (y + self.__fire_range)
            ):
                units_smoked.append(unit)
        return units_smoked
```

### Dragons Fight

#### Assignment
Complete the bottom half of the main() -> None function using two for-loops:

Iterate over all the dragons and describe() each one in order.
Iterate over all the dragons again and have each dragon breathe_fire at coordinate x=3, y=3. Pass in all the other dragons (not the one currently breathing fire) as the units parameter, so we can see if they get hit.
Pass in the dragons in the same order as the original list, excluding the current dragon. For example, when Blue Dragon breathes fire, it should check to breathe fire on the other dragons in this order:

Green Dragon
Red Dragon
Black Dragon
Example Output
When you describe the dragons, your output should look like this:

Green Dragon is at 0/0
Red Dragon is at 2/2
Blue Dragon is at 4/3
Black Dragon is at 5/-1

The output of the first dragon breathing fire should look like this:

====================================
Green Dragon breathes fire at 3/3 with range 1
------------------------------------
Red Dragon is hit by the fire
Blue Dragon is hit by the fire
====================================
Red Dragon breathes fire at 3/3 with range 2
------------------------------------

##### Tips
**Copying a List**
To get a new copy of a list, use the copy() method. If you just do new_list = old_list, your new variable will just be a reference to the original list... which is not what we want.

nums: list[int] = [4, 3, 2, 1]
nums_copy: list[int] = nums.copy()
- # nums_copy is [4, 3, 2, 1]

**Delete from a List**
fruits: list[str] = ["apple", "banana", "cherry", "kiwi"]
del fruits[1]
- # fruits is ["apple", "cherry", "kiwi"]


```Python
def main() -> None:
    dragons = [
        Dragon("Green Dragon", 0, 0, 1)
        Dragon("Red Dragon", 2, 2, 2)
        Dragon("Blue Dragon", 4, 3, 3)
        Dragon("Black Dragon", 5, -1, 4)
    ]

    # Don't touch above this line

    for dragon in range(len(dragons)):
        describe(dragons[dragon])


    for dragon in range(0, len(dragons)):
        dragons_copy: list[Dragon] = dragons.copy()
        del dragons_copy[dragon]
        dragons[dragon].breath_fire(3, 3, dragons_copy)

    

# Don't touch below this line


def describe(dragon: "Dragon") -> None:
    print(f"{dragon_name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


Class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int) -> None:
        super.__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breath_fire(self, x: int, y: int, units: list[Unit]) | list["Dragon"] -> None:
        print("========================================")
        print(f"{self.name} breathes fire at {x}/{y} with range {self.fire_range}")
        print("----------------------------------------")
        for unit in units:
            in area = in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in area:
                print(f"{unit.name} is hit by the fire")

main()
```

### Inheritance Practice

```Python
class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def get_area(self) -> None:
        return self.length * self.width

    def get_perimeter(self) -> None:
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, length: int) -> None:
        super().__init__(length, length)
```

### Sieg Weapons

```Python
class Siege:
    def __init__(self, max_speed: int, efficiency: int) -> None:
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_costs(self, distance: int, food_price: int) -> float:
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self) -> float | None:
        pass


class BatteringRam(Siege):
    def __init__(
    self,
    max_speed: int,
    efficiency: int,
    load_weight: int,
    bed_area: int,
    ) -> None:
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance: int, food_price: int) -> float:
        base_cost = super().get_trip_cost(distance, food_price)
        return best_cost + (self.load_weight * 0.01)

        def get_cargo_volume(self) -> float:
            return self.bed_area * 2.0

class Catapult(Siege):
    def __init__(self, max_speed: int, efficiency: int, cargo_volume: int) -> None:
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_colume(self) -> None:
        return self.cargo_volume
```



## CH6: Polymorphism

Polymorphism is the ability of a variable, function or object to take on multiple forms. 
"poly": "many"
"morph": "form"

For example, classes in the same hierarchical tree may have methods with the _same name and signature_ but different implementations.

```Python
class Creature:
    def move(self) -> None:
        print("the creature moves")


class Dragon(Creature):
    def move(self) -> None:
        print("the dragon flies")


class Kraken(Creture):
    def move(self) -> None:
        print("the kraken swims")


creatures: list[Creature] = [Creature(), Dragon(), Kraken()]
for creature in creatures:
    creature.move()

# prints:
# the creature moves
# the dragon flies
# the kraken swims
```


