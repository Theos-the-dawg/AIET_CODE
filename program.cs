using System;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Collections;

namespace  Program
{
    
    class Program
    {
        public static void Main(String[] args)
        {
            //EXCERCISE 1 SIMPLE Program for entering name and age
                     System.Console.WriteLine("Welcome to my little text game");
                      System.Console.WriteLine("\t please input your name");
                      string name = Console.ReadLine();
                      System.Console.WriteLine($"welcome{name}");
                       System.Console.WriteLine("please tell us how old you are");
                       string age = Console.ReadLine();
                       int ConveteredAge = Convert.ToInt32(age);
             System.Console.WriteLine("so"+name+", you are "+ConveteredAge+" years of age");

        //     System.Console.WriteLine("please enter your age");
        // string age =Console.ReadLine();
//    int new_age =  Convert.ToInt32(age);

// switch (){
//             System.Console.WriteLine();
//             break;
//             }
//             case 1:



//   while (new_age != 18)
//         {
//                 System.Console.WriteLine("Please insert age");
//             //     new_age = Console.ReadLine();
//             //   int  new_age = Convert.ToInt32(new_age);

//                 if (new_age ==20 || new_age == 25)
//                 {
//                     System.Console.WriteLine("You are an adult");

//                 }
//                 else if (new_age > 70)
//                 {
//                     System.Console.WriteLine();
//                 }


  
//                 // System.Console.WriteLine("give us and age please ");
//                 // string age = Console.ReadLine(Convert.ToInt32(age));
                
                
//             }


// //  Console.ReadKey();




        }
        
    }
}