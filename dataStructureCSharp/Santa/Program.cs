using System;

namespace Santa
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] line = Console.ReadLine().Split();
            double x = double.Parse(line[0]);
            double k = double.Parse(line[1]);
            double r = double.Parse(line[2]);

            double c = 2 * Math.PI * r;
            double dist = c * k;
            double p = dist * x;
            Console.WriteLine(p);
            Console.ReadLine();
        }
    }
}
