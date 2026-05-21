// ALBERT EINSTEIN'S RIDDLE
//
// 1. In a street there are five houses, painted five different colours.
// 2. In each house lives a person of different nationality.
// 3. These five homeowners each drink a different kind of beverage, smoke
//    different brand of cigar, and keep a different pet.
//
// THE QUESTION: WHO OWNS THE FISH?
//
// Each variable holds which house number (1-5) has that attribute.

using Google.OrTools.Sat;

namespace ConstraintCSharp;

public static class Einstein
{
    public static void Solve()
    {
        Console.WriteLine("=== EINSTEIN'S RIDDLE: WHO OWNS THE FISH? ===\n");

        var model = new CpModel();
        IntVar H(string name) => model.NewIntVar(1, 5, name);

        // Colors
        var red = H("red"); var white = H("white"); var green = H("green");
        var yellow = H("yellow"); var blue = H("blue");

        // Nationalities
        var brit = H("brit"); var swede = H("swede"); var dane = H("dane");
        var norwegian = H("norwegian"); var german = H("german");

        // Drinks
        var tea = H("tea"); var coffee = H("coffee"); var milk = H("milk");
        var beer = H("beer"); var water = H("water");

        // Smokes
        var pallmall = H("pallmall"); var dunhill = H("dunhill");
        var blends = H("blends"); var bluemaster = H("bluemaster"); var prince = H("prince");

        // Pets
        var dogs = H("dogs"); var birds = H("birds"); var cats = H("cats");
        var horses = H("horses"); var fish = H("fish");

        model.AddAllDifferent(new[] { red, white, green, yellow, blue });
        model.AddAllDifferent(new[] { brit, swede, dane, norwegian, german });
        model.AddAllDifferent(new[] { tea, coffee, milk, beer, water });
        model.AddAllDifferent(new[] { pallmall, dunhill, blends, bluemaster, prince });
        model.AddAllDifferent(new[] { dogs, birds, cats, horses, fish });

        // Hint 1:  The Brit lives in the red house.
        model.Add(brit == red);
        // Hint 2:  The Swede keeps dogs.
        model.Add(swede == dogs);
        // Hint 3:  The Dane drinks tea.
        model.Add(dane == tea);
        // Hint 4:  The green house is immediately left of the white house.
        model.Add(green + 1 == white);
        // Hint 5:  The green house owner drinks coffee.
        model.Add(green == coffee);
        // Hint 6:  The Pall Mall smoker keeps birds.
        model.Add(pallmall == birds);
        // Hint 7:  The yellow house owner smokes Dunhill.
        model.Add(yellow == dunhill);
        // Hint 8:  The centre house owner drinks milk.
        model.Add(milk == 3);
        // Hint 9:  The Norwegian lives in the first house.
        model.Add(norwegian == 1);
        // Hint 10: The Blends smoker lives next to the cat owner.
        Neighbors(model, blends, cats);
        // Hint 11: The horse owner lives next to the Dunhill smoker.
        Neighbors(model, horses, dunhill);
        // Hint 12: The Blue Master smoker drinks beer.
        model.Add(bluemaster == beer);
        // Hint 13: The German smokes Prince.
        model.Add(german == prince);
        // Hint 14: The Norwegian lives next to the blue house.
        Neighbors(model, norwegian, blue);
        // Hint 15: The Blends smoker has a neighbour who drinks water.
        Neighbors(model, blends, water);

        var solver = new CpSolver();
        var status = solver.Solve(model);

        if (status != CpSolverStatus.Feasible && status != CpSolverStatus.Optimal)
        {
            Console.WriteLine("No solution found.");
            return;
        }

        (IntVar[] vars, string[] names)[] categories =
        [
            ([brit, swede, dane, norwegian, german],        ["Brit", "Swede", "Dane", "Norwegian", "German"]),
            ([red, white, green, yellow, blue],              ["Red", "White", "Green", "Yellow", "Blue"]),
            ([tea, coffee, milk, beer, water],               ["Tea", "Coffee", "Milk", "Beer", "Water"]),
            ([pallmall, dunhill, blends, bluemaster, prince],["Pall Mall", "Dunhill", "Blends", "Blue Master", "Prince"]),
            ([dogs, birds, cats, horses, fish],              ["Dogs", "Birds", "Cats", "Horses", "Fish"]),
        ];

        string[] labels = ["Nationality", "Color      ", "Drink      ", "Smoke      ", "Pet        "];

        string Find(IntVar[] vars, string[] names, long house) =>
            names[Array.FindIndex(vars, v => solver.Value(v) == house)];

        for (int h = 1; h <= 5; h++)
        {
            Console.WriteLine($"House {h}");
            Console.WriteLine("--------");
            for (int i = 0; i < categories.Length; i++)
                Console.WriteLine($"{labels[i]}: {Find(categories[i].vars, categories[i].names, h)}");
            Console.WriteLine();
        }

        var (natVars, natNames) = categories[0];
        var (petVars, petNames) = categories[4];
        Console.WriteLine($"The fish owner is: {Find(natVars, natNames, solver.Value(fish))}");
    }

    private static void Neighbors(CpModel model, IntVar a, IntVar b)
    {
        var diff = model.NewIntVar(-4, 4, "");
        model.Add(diff == a - b);
        var absDiff = model.NewIntVar(0, 4, "");
        model.AddAbsEquality(absDiff, diff);
        model.Add(absDiff == 1);
    }
}
