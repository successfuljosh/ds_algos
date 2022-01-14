//using System;

//namespace DangerousTask
//{
//    class Program
//    {
//        public static void Main(string[] args)
//        {
//            string[] line = Console.ReadLine().Split(' ');
//            int N = int.Parse(line[0]);
//            int A = int.Parse(line[1]);
//            int B = int.Parse(line[2]);

//            string Tiles = Console.ReadLine();

//            int secs = int.MaxValue;

//            int[] kovalskiCan = new int[N];
//            int[] ricoCan = new int[N];

//            int ricoStart = A,
//                kovalskiStart = B;

//            while (ricoStart >= 1)
//            {
//                if (Tiles[ricoStart - 1] == '1')
//                {
//                    ricoCan[ricoStart - 1] = 1;
//                    ricoStart -= 4;
//                }
//                else
//                {
//                    break;
//                }
//            }
//            while (kovalskiStart >= 1)
//            {
//                if (Tiles[kovalskiStart - 1] == '1')
//                {
//                    kovalskiCan[kovalskiStart - 1] = 1;
//                    kovalskiStart -= 7;
//                }
//                else
//                {
//                    break;
//                }
//            }

//            ricoStart = A;
//            kovalskiStart = B;

//            while (ricoStart <= N)
//            {
//                if (Tiles[ricoStart - 1] == '1')
//                {
//                    ricoCan[ricoStart - 1] = 1;
//                    ricoStart += 4;
//                }
//                else
//                {
//                    break;
//                }
//            }
//            while (kovalskiStart <= N)
//            {
//                if (Tiles[kovalskiStart - 1] == '1')
//                {
//                    kovalskiCan[kovalskiStart - 1] = 1;
//                    kovalskiStart += 7;
//                }
//                else
//                {
//                    break;
//                }
//            }

//            for (int i = 0; i < N; i++)
//            {
//                if (ricoCan[i] == 1 && kovalskiCan[i] == 1)
//                {
//                    secs = Math.Min(secs, Math.Abs(i + 1 - A) / 4 + Math.Abs(i + 1 - B) / 7);
//                }
//            }

//            if (secs == int.MaxValue)
//            {
//                Console.WriteLine(-1);
//            }
//            else
//            {
//                Console.WriteLine(secs);
//            }
//            Console.ReadLine();
//        }
//    }
//}
