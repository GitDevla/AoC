using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;

namespace helpme {
    class Program {
        static int[,] data = {{2483411,3902983,2289579,3633785},
{3429446,303715,2876111,-261280},
{666423,3063763,2264411,2779977},
{3021606,145606,2876111,-261280},
{2707326,2596893,2264411,2779977},
{3103704,1560342,2551409,2000000},
{3497040,3018067,3565168,2949938},
{1708530,855013,2551409,2000000},
{3107437,3263465,3404814,3120160},
{2155249,2476196,2264411,2779977},
{3447897,3070850,3404814,3120160},
{2643048,3390796,2289579,3633785},
{3533132,3679388,3404814,3120160},
{3683790,3017900,3565168,2949938},
{1943208,3830506,2289579,3633785},
{3940100,3979653,2846628,4143786},
{3789719,1225738,4072555,1179859},
{3939775,578381,4072555,1179859},
{3880152,3327397,3404814,3120160},
{3280639,2446475,3565168,2949938},
{2348869,2240374,2551409,2000000},
{3727441,2797456,3565168,2949938},
{3973153,2034945,4072555, 1179859},
{38670,785556,311084,-402911},
{3181909,2862960,3565168, 2949938},
{3099490,3946226,2846628, 4143786}};
        static void Main(string[] args) {


            /*
             * for (let y = minY < 0 ? 0 : minY; y < limit; y++) {
        for (let x = minX < 0 ? 0 : minX; x < limit; x++) {
            if (!isCovered(waypoints, y, x)) return [x, y];
        }
    
            }*/
            var times = int.Parse(args[0]);
            precalcdata = preCalc();
            data = null;
            for (int y = times; y > 0 ; y--) {
                if (y % 10000 == 0) Console.WriteLine(y);
                Thread myNewThread = new Thread(() => asd(y));
                myNewThread.Start();
            }
            Console.WriteLine("Fuck");
            Console.ReadKey();
        }

        static void asd(int y) {
            for (int x = 0; x < 4000000; x++) {
                if (!isCovered(y, x)) {
                    Console.WriteLine("THE ONE PIECE IS REALLLLLL");
                    File.AppendAllText("haha.txt",$"x:{x}, y:{y}\n");
                    return;
                }
            }
        }

        static bool isCovered(int y, int x) {
            foreach (var i in precalcdata) {
                var Sy = i[0];
                var Sx = i[1];
                var dist = i[2];
                var dist2 = Math.Abs(Sx - x) + Math.Abs(Sy - y);
                if (dist2 <= dist) return true;
            }
            return false;
        }
        /*function isCovered(waypoints, y, x) {
            for (const data of waypoints) {
                let[Sx, Sy, Bx, By] = data;
                let dist = Math.abs(Sx - Bx) + Math.abs(Sy - By);
                let dist2 = Math.abs(Sx - x) + Math.abs(Sy - y);
                if (dist2 <= dist) return true;
            }
            return false;
        }*/
        static int[][] precalcdata;
        static int[][] preCalc() {
            List<int[]> outp = new();
            for (int i = 0; i < data.GetLength(0); i++) {
                var Sy = data[i, 0];
                var Sx = data[i, 1];
                var Bx = data[i, 2];
                var By = data[i, 3];
                var dist = Math.Abs(Sx - Bx) + Math.Abs(Sy - By);
                outp.Add(new int[] { Sx, Sy, dist });
            }
            return outp.ToArray();
        }
    }
}
