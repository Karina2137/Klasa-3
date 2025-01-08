using NUnit.Framework;
using NUnit.Framework.Legacy;
using WinFormsApp1;
namespace Test1
{
    class WinFormsApp1
    {
        [Test]
        public void test1()
        {
            //asing
            Kalk k = new Kalk();
            //act
            int wynik = k.dodaj(1, 2);
            //assert
            //ClassicAssert.Equals(wynik, 1);
            Assert.That(4, Is.EqualTo(wynik));
        }
    }
}
//Test programu
