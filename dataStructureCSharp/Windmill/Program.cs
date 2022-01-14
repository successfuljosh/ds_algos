using System;
using System.Collections.Generic;
using System.Linq;


namespace Windmill
{
    class Program
    {
        static void Main(string[] args)
        {
            var line1 = Console.ReadLine().Split();
            var line2 = Console.ReadLine().Split();
            var N = int.Parse(Console.ReadLine());

            var Xz = int.Parse(line1[0]);
            var Yz = int.Parse(line1[1]);

            var Xc = int.Parse(line2[0]);
            var Yc = int.Parse(line2[1]);

            var distance = Math.Pow(Math.Pow(Xc - Xz, 2) + Math.Pow(Yc - Yz, 2), 0.5);
            var array = new List<double>();
            for (int i = 0; i < N; i++)
            {
                var line_o = Console.ReadLine().Split();
                var X = int.Parse(line_o[0]);
                var Y = int.Parse(line_o[1]);
                var result = Math.Pow(Math.Pow(Xc - X, 2) + Math.Pow(Yc - Y, 2), 0.5);
                array.Add(result);
            }

            if (array.Max() >= distance)
                Console.WriteLine("YES");
            else
                Console.WriteLine("NO");

            //Console.ReadLine();
        }
    }
}
