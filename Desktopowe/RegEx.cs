using System.Text.RegularExpressions;

namespace WinFormsApp1
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
                int cyfra = int.Parse(liczba);
                while ( cyfra > 0 )
                {
                    int kon = cyfra % 100;
                    kon%=
                }
            }
        }
    }
}
