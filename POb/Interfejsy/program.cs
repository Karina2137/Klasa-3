using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
        class Book : IComparable<Book>
        {
            string title;
            public string author;
            public int yearOfPublication;
            public double price;
            public int CompareTo(Book other)
            {
                if (other == null) return 1;
                return price.CompareTo(other.price);
            }
        public Book(string title, string author, int yearOfPublication, double price)
        {
            this.title = title;
            this.author = author;
            this.yearOfPublication = yearOfPublication;
            this.price = price;
        }
        public override string ToString()
        {
            return $"{title},{author},{yearOfPublication},{price}zł";
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Book> books = new List<Book>();
            books.Add(new Book("Hobbit", "Nowak", 1937, 45.60));
            books.Add(new Book("Tam i z powrotem", "Pawlak", 1998, 35.78));
            books.Add(new Book("Jakby nie było nic", "Arbuz", 2001, 87.11));
            books.Add(new Book("M jak milczenie", "Karkowski", 2023, 41.63));

            Console.WriteLine("Lista książek");
            foreach (Book book in books)
            {
                Console.WriteLine(book);
            }
             
            books.Sort();
            Console.WriteLine();
            Console.WriteLine("Lista książek posortowanych według ceny");
            foreach (Book book in books)
            {
                Console.WriteLine(book);
            }
            Console.WriteLine();
            Console.WriteLine("Lista książek posortowanych według daty publikacji");
            var sortByYear = books.OrderBy(b => b.yearOfPublication);
            foreach (Book book in sortByYear)
            {
                Console.WriteLine(book);
            }
            Console.WriteLine();
            Console.WriteLine("Lista książek posortowanych według autorów");
            var sortByAuthor = books.OrderByDescending(a => a.author);
            foreach (Book book in sortByAuthor)
            {
                Console.WriteLine(book);
            }
            Console.WriteLine();
            Console.WriteLine("Lista książek posortowanych według ceny nierosnąco a następnie według roku od najstarszej książki");
            var sortByPriceAndYear = books.OrderByDescending(a => a.price).ThenBy(a => a.yearOfPublication);
            foreach (Book book in sortByPriceAndYear)
            {
                Console.WriteLine(book);
            }
            Console.WriteLine();
            Console.WriteLine("Lista książek które najpierw sortuje książki według ceny malejąco, następnie według roku publikacji rosnąco, a na końcu według autora alfabetycznie");
            var sortByPriceYearAndAuthor = books.OrderByDescending(a => a.price).ThenBy(a => a.yearOfPublication).ThenBy(a => a.author);
            foreach (Book book in sortByPriceAndYear)
            {
                Console.WriteLine(book);
            }

            Console.ReadKey();
        }
    }
}
