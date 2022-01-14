using System;

namespace Snoballs
{
    class Program
    {
        static void Main(string[] args)
        {
            var line1 = Console.ReadLine().Split();
            var line2 = Console.ReadLine().Split();

            var N = int.Parse(line1[0]);
            var M= int.Parse(line1[1]);

            var X = int.Parse(line2[0]);
            var Y = int.Parse(line2[1]);

            double first = N * X, second = M * Y;
            double NN = N, MM = M;
            while (first > 0 && second > 0)
            {
                first -= MM;
                second -= NN;
                NN = Math.Ceiling(first / X);
                MM = Math.Ceiling(second / Y);
            }
            if (first>second)
                Console.WriteLine("FIRST");
            else if (second >first)
                Console.WriteLine("SECOND");
            else
                Console.WriteLine("DRAW");

            //Console.ReadLine();
        }
    }
}
