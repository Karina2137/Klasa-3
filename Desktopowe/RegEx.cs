using System.Text.RegularExpressions;

namespace ToDo3
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

            Regex regex = new Regex(@"^\d{7,9}$");
            if (!regex.IsMatch(liczba))
            {
                label1.Text = "Nieprawidłowe dane";
            }
            else
            {
                int reszty = 0;
                int cyfra = int.Parse(liczba);
                while (cyfra>0)
                {
                    int kon = cyfra % 100;
                    while (kon>=7)
                    {
                        kon -= 7;
                    }
                    reszty += kon;
                    kon = 0;
                    cyfra /= 100;
                }
                while (reszty>=7)
                {
                    reszty-= 7;
                }
                if (reszty == 0)
                {
                    label1.Text = $"Liczba {liczba} jest podzielna przez 7";
                }
                else
                {
                    label1.Text = $"Liczba {liczba} nie jest podzielna przez 7";
                }
            }
        }
    }
}
