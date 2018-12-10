namespace FlagPrinter
{
    using System;
    using System.Runtime.InteropServices;
    using System.IO;
    using System.Text;
    using System.Security.Cryptography;
    using System.Net;

    /// <summary>Contains native method declarations.</summary>
    internal static class NativeMethods
    {
        /// <summary>Checks the validity of the specified password.</summary>
        /// <param name="password">The password to validate.</param>
        /// <returns>0 if the password is valid, otherwise non-zero.</returns>
        [DllImport("PasswordValidation")]
        internal static extern int IsPasswordValid(string password);
    }

    /// <summary>Contains the main entry point of the application.</summary>
    public class Program
    {
        /// <summary>The decryption function :)</summary>
        public static string Decrypt()
        {
           //decryption algo here
           return plaintext;
        }
        
        /// <summary>Main entry point of the application.</summary>
        public static void Main()
        {
            while (true)
            {
                // read the user's password from stdin
                Console.Write("Enter password: ");
                var password = Console.ReadLine();

                // validate it using the secure authentication library
                Console.Write("Authentication: ");
                if (NativeMethods.IsPasswordValid(password) == 0)
                {
                    Console.WriteLine("ACCEPTED!\n");
                    Console.WriteLine(String.Format("Flag : {0}", plainText));
                    break;
                }
                // the password was rejected
                Console.WriteLine("REJECTED!\n");
            }
            Console.ReadKey();  // don't quit until after a key is pressed
        }
    }
}