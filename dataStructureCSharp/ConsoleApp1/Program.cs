using System;

namespace ConsoleApp1
{
    class Program
    {
        static int N, K, A, B;
        static void Main(string[] args)
        {

            string[] line = Console.ReadLine().Split();
             N = int.Parse(line[0]);
            K = int.Parse(line[1]);

            line = Console.ReadLine().Split();
            A = int.Parse(line[0]);
            B = int.Parse(line[1]);

            double max_result = SearchMax(A, B);
            double min_result = SearchMin(A, B);
            Console.WriteLine(max_result+" "+min_result);
            //Console.ReadLine();
         
        }
        static double counter(double x, double y, double z, double w)
        {
            double f = Math.Ceiling(Math.Abs(x - y) / Math.Abs(z));
            double s = Math.Ceiling(Math.Abs(x - w) / Math.Abs(z));
            double ans = f + s + 1;
            return ans;
        }

        static double SearchMax(int first, int second)
        {
            double left = Math.Max(first, second);
            double right = left + (K * N);
            while ((right - left) > 1)
            {
                double m = Math.Floor((left + right) / 2);
                if (counter(m, A, K, B) > N)
                    right = m;
                else
                    left = m;
            }
            return left;
        }

        static double SearchMin(int first, int second)
        {
            double right = Math.Min(first, second);
            double left = right - (K * N);
            while ((right - left) > 1)
            {
                double m = Math.Floor((left + right) / 2);
                if (counter(m, A, K, B) > N)
                    left = m;
                else
                    right = m;
            }
            return right;
        }

    }
}
