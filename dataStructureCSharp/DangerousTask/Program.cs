using System;
using System.Linq;

namespace ColorFence
{
    class Program
    {
        public static void Main(string[] args)
        {
            //int N = int.Parse(Console.ReadLine());
            //string[] line = Console.ReadLine().Split(' ');
            //int[] A = new int[line.Length];
            //for (int i = 0; i < line.Length; i++)
            //{
            //    A[i] = int.Parse(line[i]);
            //}
            //Array.Sort(A);
            //int j = 1;
            //for (int i = 0; i < N - 1; i++)
            //{
            //    if (A[i] != A[i + 1])
            //    {
            //        j += 1;
            //    }
            //}
            //Console.WriteLine(j);

            string[] line = Console.ReadLine().Split(' ');
            int K = int.Parse(line[0]);
            int T = int.Parse(line[1]);
            string[] line2 = Console.ReadLine().Split(' ');
            int[] A = new int[line2.Length];
            for (int i = 0; i < line2.Length; i++)
            {
                A[i] = int.Parse(line2[i]);
            }
            Array.Sort(A);
            int re = MINI(K, T, A);
            Console.WriteLine(re);
            Console.ReadLine();
        }
        static int MINI(int K, int T, int[] A)
        {
            int P = 0;
            if (K >= 1 && K <= 5000)
            {
                if (T >= 1 && T <= Math.Pow(10, 5))
                {
                 
                    if (T <= K)
                        for (int j = 0; j < A.Length; j++)
                        {
                            P = P + (A[j] + T);
                        }

                    else if (T > K)
                        P = P + A.Max() * K + T;

                }
            }
            return P;
        }
    }
}
