// Assign equal values to equal letters, and different values to
// different letters, in a way that satisfies the following sum:
//
//    SEND
//  + MORE
//  ------
//   MONEY

using Google.OrTools.Sat;

namespace ConstraintCSharp;

public static class SendMoreMoney
{
    public static void Solve()
    {
        Console.WriteLine("=== SEND + MORE = MONEY ===\n");

        var model = new CpModel();

        var s = model.NewIntVar(1, 9, "s"); // no leading zero
        var e = model.NewIntVar(0, 9, "e");
        var n = model.NewIntVar(0, 9, "n");
        var d = model.NewIntVar(0, 9, "d");
        var m = model.NewIntVar(1, 9, "m"); // no leading zero
        var o = model.NewIntVar(0, 9, "o");
        var r = model.NewIntVar(0, 9, "r");
        var y = model.NewIntVar(0, 9, "y");

        model.AddAllDifferent(new[] { s, e, n, d, m, o, r, y });

        model.Add(
            1000*s + 100*e + 10*n + d +
            1000*m + 100*o + 10*r + e ==
            10000*m + 1000*o + 100*n + 10*e + y);

        var solver = new CpSolver();
        solver.StringParameters = "enumerate_all_solutions:true";
        var cb = new Callback(s, e, n, d, m, o, r, y);
        solver.Solve(model, cb);

        Console.WriteLine($"\nFound {cb.Count} solution(s).");
    }

    private sealed class Callback(
        IntVar s, IntVar e, IntVar n, IntVar d,
        IntVar m, IntVar o, IntVar r, IntVar y) : CpSolverSolutionCallback
    {
        public int Count { get; private set; }

        public override void OnSolutionCallback()
        {
            Count++;
            long sv = Value(s), ev = Value(e), nv = Value(n), dv = Value(d);
            long mv = Value(m), ov = Value(o), rv = Value(r), yv = Value(y);
            Console.WriteLine($"  {sv}{ev}{nv}{dv} + {mv}{ov}{rv}{ev} = {mv}{ov}{nv}{ev}{yv}");
        }
    }
}
