using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading.Tasks.Dataflow;

namespace Day7
{
    internal class Card(Card.Suit inSuit, Card.Value inValue): IComparable
    {
        public enum Suit
        {
            Hearts,
            Diamonds,
            Spades,
            Clubs

        }
        public enum Value
        {
            ONE,
            TWO,
            THREE,
            FOUR,
            FIVE,
            SIX,
            SEVEN,
            EIGHT,
            NINE,
            TEN,
            JACK,
            QUEEN,
            KING,
            ACE

        }
        public static Dictionary<char, Value> CardTranslate = new Dictionary<char, Value>()
        {
            { '1',Value.ONE },
            { '2',Value.TWO },
            { '3',Value.THREE },
            { '4',Value.FOUR },
            { '5',Value.FIVE },
            { '6',Value.SIX },
            { '7',Value.SEVEN },
            { '8',Value.EIGHT },
            { '9',Value.NINE },
            { 'T',Value.TEN },
            { 'J',Value.JACK },
            { 'Q', Value.QUEEN },
            { 'K',Value.KING },
            { 'A', Value.ACE }

        };
        public static Dictionary<Value, char> ReverseCardTranslate = new Dictionary<Value, char>()
        {
            { Value.ONE, '1'},
            { Value.TWO, '2' },
            { Value.THREE, '3' },
            { Value.FOUR, '4' },
            { Value.FIVE, '5' },
            { Value.SIX, '6' },
            { Value.SEVEN, '7' },
            { Value.EIGHT, '8' },
            { Value.NINE, '9' },
            { Value.TEN, 'T' },
            { Value.JACK, 'J' },
            { Value.QUEEN, 'Q' },
            { Value.KING, 'K' },
            { Value.ACE, 'A' },

        };

        public Suit suit { get; set; } = inSuit;
        public Value value { get; set; } = inValue;

        public int CompareTo(object? obj)
        {
            if (obj == null || obj.GetType() != typeof(Card))
            {
                return 1;
            }
            else
            {
                Card card1 = obj as Card;
                return this.value.CompareTo(card1.value);
            }

        }
    }
}
