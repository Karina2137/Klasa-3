using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static Delegat.Program;

namespace Delegat
{
	internal class Program
	{
		public delegate void NotificationHandler(string message);
		public class EmailNotifier
		{
			public void SendEmail(string message)
			{
                Console.WriteLine($"Email wysłany: {message}");
            }
		}
		public class SMSNotifier
		{
			public void SendSMS(string message)
			{
				Console.WriteLine($"SMS wysłany: {message}");
			}
		}
		public class PushNotifier
		{
			public void SendPushNotifier(string message)
			{
                Console.WriteLine($"Powiadomienie PUSH wysłany: {message}");
			}
		}
		public class NotificationManager
		{
			public NotificationHandler Notify;
			public void AddNotificationMethod(NotificationHandler handler)
			{
				Notify += handler;
			}
			public void RemoveNotificationMethod(NotificationHandler handler)
			{
				Notify -= handler;
			}
			public void SendNotification(string message)
			{
				if (Notify == null)
				{
                    Console.WriteLine("Brak dostępnych metod powiadomień");
                }
				Notify?.Invoke(message);
			}
		}
		public static void ShowMenu()
		{
            Console.WriteLine("Menu");
            Console.WriteLine("1.Dodaj powiadomienie Email");
            Console.WriteLine("2.Dodaj powiadomienie SMS");
            Console.WriteLine("3.Dodaj powiadomienie Push");
            Console.WriteLine("4.Usuń powiadomienie Push");
            Console.WriteLine("5.Usuń powiadomienie Push");
            Console.WriteLine("6.Usuń powiadomienie Push");
            Console.WriteLine("7.Wyślij powiadomienie");
            Console.WriteLine("8.Wyjdź");
            Console.WriteLine("Wybierz opcję");
        }
		static void Main(string[] args)
		{
			var emailNotifier = new EmailNotifier();
			var smsNotifier = new SMSNotifier();
			var pushNotifier = new PushNotifier();

			var notificationManager = new NotificationManager();

			//notificationManager.SendNotification("test");

			while (true)
			{
				try
				{
					ShowMenu();
					var choise = int.Parse(Console.ReadLine());
					switch (choise)
					{
						case 1:
							notificationManager.AddNotificationMethod(emailNotifier.SendEmail);
							Console.WriteLine("Dodano powiadomienie email");
							break;
						case 2:
							notificationManager.AddNotificationMethod(smsNotifier.SendSMS);
							Console.WriteLine("Dodano powiadomienie SMS");
							break;
						case 3:
							notificationManager.AddNotificationMethod(pushNotifier.SendPushNotifier);
							Console.WriteLine("Dodano powiadomienie Push");
							break;
						case 4:
							notificationManager.RemoveNotificationMethod(emailNotifier.SendEmail);
							Console.WriteLine("Usunięto powiadomienie email");
							break;
						case 5:
							notificationManager.RemoveNotificationMethod(smsNotifier.SendSMS);
							Console.WriteLine("Usunięto powiadomienie SMS");
							break;
						case 6:
							notificationManager.RemoveNotificationMethod(pushNotifier.SendPushNotifier);
							Console.WriteLine("Usunięto powiadomienie Push");
							break;
						case 7:
							Console.WriteLine("Wpisz wiadomość do wysłania");
							var message = Console.ReadLine();
							notificationManager.SendNotification(message);
							break;
						case 8:
							return;
						default:
							Console.WriteLine("Nie poprawna opcja. Spróbuj ponownie");
							break;
					}
				}
				catch (Exception e) { Console.WriteLine(); }

			Console.ReadKey();
			}
		}
	}
}
