using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading.Tasks.Dataflow;

namespace Day7
{
    internal class JokerCard(JokerCard.Suit inSuit, JokerCard.Value inValue): IComparable
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
            JOKER,
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
            { 'J',Value.JOKER },
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
            { Value.JOKER, 'J' },
            { Value.QUEEN, 'Q' },
            { Value.KING, 'K' },
            { Value.ACE, 'A' },

        };

        public Suit suit { get; set; } = inSuit;
        public Value value { get; set; } = inValue;

        public int CompareTo(object? obj)
        {
            if (obj == null || obj.GetType() != typeof(JokerCard))
            {
                return 1;
            }
            else
            {
                JokerCard card1 = obj as JokerCard;
                return this.value.CompareTo(card1.value);
            }

        }
    }
}
