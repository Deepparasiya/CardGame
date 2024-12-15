using System;

namespace dotnetapp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What is your favourite web application language?");
            string answer = Console.ReadLine();
            Console.WriteLine("Your Answer is: " + answer + "\r\n");
        }
    }
}