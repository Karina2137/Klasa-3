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
            Kalk kalk = new Kalk();
            int l1 = int.Parse(textBox1.Text);
            int l2 = int.Parse(textBox2.Text);
            int wynik = kalk.dodaj(l1,l2);
            label1.Text = wynik.ToString();
        }
    }
}
