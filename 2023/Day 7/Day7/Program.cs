using Day7;
using System;
using System.Collections.Generic;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        private static void PopulateLists(List<Hand> HandList, List<JokerHand> JokerHandList)
        {
            string? line;
            try
            {
                StreamReader sr = new StreamReader("C:\\mysources\\aoc23\\Aedan\\Day 7\\Day7\\Day7\\Day7.txt");
                line = sr.ReadLine();
                while (line != null)
                {
                    var lineSplit = line.Split(' ');
                    var card = new Hand(lineSplit.First(), typeof(char));
                    var jokercard = new JokerHand(lineSplit.First(), typeof(char));
                    card.bidAmount = Convert.ToInt32(lineSplit.Last());
                    jokercard.bidAmount = Convert.ToInt32(lineSplit.Last());
                    HandList.Add(card);
                    JokerHandList.Add(jokercard);
                    line = sr.ReadLine();
                }
                sr.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception: " + e.Message);
            }
        }
        static void Main(string[] args)
        {

            var HandList = new List<Hand>();
            var JokerHandList = new List<JokerHand>();
            string? line;

            PopulateLists(HandList, JokerHandList);
            List<Hand> SortedList = [.. HandList.OrderBy(hand => hand.handType)
                                                .ThenBy(hand => hand.cards[0])
                                                .ThenBy(hand => hand.cards[1])
                                                .ThenBy(hand => hand.cards[2])
                                                .ThenBy(hand => hand.cards[3])
                                                .ThenBy(hand => hand.cards[4])
                                                .ThenBy(hand => hand.bidAmount)];
            List<JokerHand> SortedJokerList = [.. JokerHandList.OrderBy(hand => hand.jokerHandType)
                                                .ThenBy(hand => hand.cards[0])
                                                .ThenBy(hand => hand.cards[1])
                                                .ThenBy(hand => hand.cards[2])
                                                .ThenBy(hand => hand.cards[3])
                                                .ThenBy(hand => hand.cards[4])
                                                .ThenBy(hand => hand.bidAmount)];
            int runningSum = 0;
            int runningJokerSum = 0;
            foreach (var hand in SortedList)
            {
                runningSum += hand.bidAmount * (SortedList.IndexOf(hand) + 1);
                //Console.WriteLine($"{hand.bidAmount} {SortedList.IndexOf(hand) + 1} {hand.handType} {hand.stringRep}");
            }
            foreach (var hand in SortedJokerList)
            {
                runningJokerSum += hand.bidAmount * (SortedJokerList.IndexOf(hand) + 1);
                Console.WriteLine($"{hand.bidAmount} {SortedJokerList.IndexOf(hand) + 1} {hand.jokerHandType} {hand.stringRep}");
            }
            Console.WriteLine($"Part 1: {runningSum}");
            Console.WriteLine($"Part 2: {runningJokerSum}");
        }


    }
}