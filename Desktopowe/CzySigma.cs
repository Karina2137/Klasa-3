using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ProjectSigma
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime data = DateTime.Parse(textBox1.Text);
            int[] liczby = new int[] {data.Day, data.Month,data.Year};
            int SumaCyfr = 0;
            for (int i = 0; i < 3; i++)
            {
                SumaCyfr += sumaCyfr(liczby[i]);
            }
            label1.Text = SumaCyfr.ToString();
        }
        int sumaCyfr(int a)
        {
            int suma = 0;
            while (a > 0)
            {
                suma += a % 10;
                a = a / 10;
            }
            return suma;
        }
    }
}
