using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;

namespace Day7
{
    internal class Hand
    {
        public int numCards { get; set; } = 5;
        public List<Card> cards { get; set; } = [];
        public HandType handType { get => GetHandValue(); }
        public int bidAmount { get; set; } = 0;
        public string stringRep { get; private set; } = string.Empty;
        public Hand(string HandString, Type t1) 
        {
            stringRep = HandString;
            if (t1 == typeof(char))
            {
                List<char> cardList = new(HandString.Trim().ToCharArray());
               

                if (cardList.Count == numCards)
                {
                    foreach (char cardChar in cardList)
                    {
                        cards.Add(new Card(Card.Suit.Clubs, Card.CardTranslate[cardChar]));
                    }
                }
                else
                {
                    Console.WriteLine("Not enough cards in hand");
                }
            }
           /* var sortCards = cards;
           // sortCards.Sort();
           // sortCards.Reverse();
            List<char> charRep = [];
            foreach(Card card in sortCards)
            {
                charRep.Add(Card.ReverseCardTranslate[card.value]);

            }
            stringRep = new string(charRep.ToArray());*/
        }
        public enum HandType
        {
            High_Card,
            One_Pair,
            Two_Pair,
            Three_of_a_Kind,
            Full_House,
            Four_of_a_Kind,
            Five_of_a_Kind
        }

        private List<Tuple<Card.Value,int>> countMatching()
        {
            List<Tuple<Card.Value, int>> matchingCount = [];
            foreach (var uniqueCard in cards)
            {
                if(!(matchingCount.Any(card => card.Item1 == uniqueCard.value)))
                {
                    matchingCount.Add(new Tuple<Card.Value, int>(uniqueCard.value, cards.Count(card => card.value == uniqueCard.value)));
                }
            }
            matchingCount.OrderBy(el => el.Item2);
            return matchingCount;
        }

        private HandType GetHandValue()
        {
            HandType handType = HandType.High_Card;
            var matchingCount = countMatching();
            switch (matchingCount.Count)
            {
                case 1:
                    handType = HandType.Five_of_a_Kind;
                    break;
                case 2:
                    handType = (matchingCount[0].Item2* matchingCount[1].Item2) == 4 ? HandType.Four_of_a_Kind : HandType.Full_House;
                    break;
                case 3:
                    handType = (matchingCount[0].Item2 * matchingCount[1].Item2 * matchingCount[2].Item2) == 4 ? HandType.Two_Pair : HandType.Three_of_a_Kind;
                    break;
                case 4:
                    handType = HandType.One_Pair;
                    break;
                case 5:
                    handType = HandType.High_Card;
                    break;
                    
            }
            return handType;
        }
    }
}
