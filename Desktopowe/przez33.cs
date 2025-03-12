using System.Text.RegularExpressions;

namespace przez33
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string liczba = textBox1.Text;

            Regex regex = new Regex(@"^\d{13,15}$");
            long licz = long.Parse(liczba);
            if (!regex.IsMatch(liczba))
            {
                label1.Text = "Nieprawidłowe dane";
            }
            else
            {
                long suma_wszystkich = 0;
                long przez11 = 0;
                while(licz>0)
                {
                    przez11 += licz % 10;
                    suma_wszystkich+= licz % 10;
                    licz /= 10;
                    przez11 -= licz % 10;
                    suma_wszystkich += licz % 10;
                    licz /= 10;
                }
                //label1.Text = $"{przez11} {suma_wszystkich}";
                if (przez11 % 11 == 0 && suma_wszystkich % 3 == 0)
                    label1.Text = $"Liczba{liczba} jest podzielna przez 3 i 11 czyli również przez 33";
                else
                    label1.Text = $"Liczba{liczba} nie jest podzielna przez 3 lub 11 czyli nie jest podzilna przez 33";
            }
            }
    }
}
