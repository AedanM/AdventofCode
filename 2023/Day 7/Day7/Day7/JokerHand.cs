using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;

namespace Day7
{
    internal class JokerHand
    {
        public int numCards { get; set; } = 5;
        public List<JokerCard> cards { get; set; } = [];
        public JokerHandType jokerHandType { get => GetJokerHandValue(); }
        public int bidAmount { get; set; } = 0;
        public string stringRep { get; private set; } = string.Empty;
        public JokerHand(string JokerHandString, Type t1) 
        {
            stringRep = JokerHandString;
            if (t1 == typeof(char))
            {
                List<char> cardList = new(JokerHandString.Trim().ToCharArray());
               

                if (cardList.Count == numCards)
                {
                    foreach (char cardChar in cardList)
                    {
                        cards.Add(new JokerCard(JokerCard.Suit.Clubs, JokerCard.CardTranslate[cardChar]));
                    }
                }
                else
                {
                    Console.WriteLine("Not enough cards in JokerHand");
                }
            }
        }
        public enum JokerHandType
        {
            High_Card,
            One_Pair,
            Two_Pair,
            Three_of_a_Kind,
            Full_House,
            Four_of_a_Kind,
            Five_of_a_Kind
        }

        private List<Tuple<JokerCard.Value,int>> countMatching()
        {
            List<Tuple<JokerCard.Value, int>> matchingCount = [];
            foreach (var uniqueCard in cards)
            {
                if(!(matchingCount.Any(card => card.Item1 == uniqueCard.value)))
                {
                    matchingCount.Add(new Tuple<JokerCard.Value, int>(uniqueCard.value, cards.Count(card => card.value == uniqueCard.value)));
                }
            }
            _ = matchingCount.OrderBy(el => el.Item2);
            if(matchingCount.Any(el => el.Item1 == JokerCard.Value.JOKER))
            {
                
                var Jokers = from val in matchingCount where val.Item1 == JokerCard.Value.JOKER select val;
                int numJokers = Jokers.First().Item2;
                if (numJokers != 5)
                {
                    matchingCount.Remove(new Tuple<JokerCard.Value, int>(JokerCard.Value.JOKER, numJokers));
                    int indexOfBest = 0;
                    int ValOfBest = 0;
                    for (int i = 0; i < matchingCount.Count; i++)
                    {
                        var value = matchingCount[i];
                        if (ValOfBest < value.Item2)
                        {
                            ValOfBest = value.Item2;
                            indexOfBest = i;
                        }
                    }
                    matchingCount[indexOfBest] = new Tuple<JokerCard.Value, int>(matchingCount[indexOfBest].Item1, matchingCount[indexOfBest].Item2 + numJokers);
                }

            }
            return matchingCount;
        }

        private JokerHandType GetJokerHandValue()
        {
            JokerHandType jHandType = JokerHandType.High_Card;
            var matchingCount = countMatching();
            switch (matchingCount.Count)
            {
                case 1:
                    jHandType = JokerHandType.Five_of_a_Kind;
                    break;
                case 2:
                    jHandType = (matchingCount[0].Item2* matchingCount[1].Item2) == 4 ? JokerHandType.Four_of_a_Kind : JokerHandType.Full_House;
                    break;
                case 3:
                    jHandType = (matchingCount[0].Item2 * matchingCount[1].Item2 * matchingCount[2].Item2) == 4 ? JokerHandType.Two_Pair : JokerHandType.Three_of_a_Kind;
                    break;
                case 4:
                    jHandType = JokerHandType.One_Pair;
                    break;
                case 5:
                    jHandType = JokerHandType.High_Card;
                    break;
                    
            }
            return jHandType;
        }
    }
}
