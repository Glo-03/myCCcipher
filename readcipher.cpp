#include <iostream>
namespace std;
using System;

namespace CaesarCipher
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a word to encode:");
            string word = Console.ReadLine();

            Console.WriteLine("Enter the number of characters to shift (positive for right shift, negative for left shift):");
            int shift = int.Parse(Console.ReadLine());

            string encodedWord = EncodeWord(word, shift);

            Console.WriteLine("Original word: " + word);
            Console.WriteLine("Encoded word: " + encodedWord);
        }

        public static string EncodeWord(string word, int shift)
        {
            string encodedWord = "";
            foreach (char c in word)
            {
                char letter = c;
                if (char.IsLetter(letter))
                {
                    if (char.IsUpper(letter))
                    {
                        letter = (char)(((letter - 65 + shift) % 26) + 65);
                    }
                    else
                    {
                        letter = (char)(((letter - 97 + shift) % 26) + 97);
                    }
                }
                encodedWord += letter;
            }
            return encodedWord;
        }
    }
}
