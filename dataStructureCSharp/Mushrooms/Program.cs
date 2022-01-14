using System;
using System.Collections.Generic;
using System.Linq;


namespace Mushrooms
{
    class Program
    {
        static void Main(string[] args)
        {
            var line1 = Console.ReadLine().Split();
            var line2 = Console.ReadLine().Split();
            var n = int.Parse(line1[0]);
            var c = int.Parse(line1[1]);
            int[] B = new int[line2.Length];
            for (int i = 0; i < line2.Length; i++)
            {
                B[i] = int.Parse(line2[i]);
            }
            Array.Sort(B);
            var bigArray = new List<List<int>>();
            bigArray.Add(new List<int>());

            for (int i = 0; i < n+1; i++)
            {
                for (int j = i+1; j < n+1; j++)
                {
                    var seg = new ArraySegment<int>(B, i, j-i).ToList();
                    //foreach (var item in seg)
                    //{
                    //    Console.WriteLine(item);
                    //}
                    //Console.WriteLine();
                    if (seg.Sum()<=c)
                    {
                        bigArray.Add(seg);
                    }
                }
            }
            var num = bigArray.Count;
            Console.WriteLine(num);
            Console.ReadLine();
        }
    }
}
