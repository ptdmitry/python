package exceptions.lesson_02;

/*
Задание №1
Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает
введенное значение. Ввод текста вместо числа не должно приводить к падению приложения, вместо этого,
необходимо повторно запросить у пользователя ввод данных
 */

import java.util.InputMismatchException;
import java.util.Scanner;

public class HomeWorkAppLesson2 {

    public static void main(String[] args) {
        double number = userNumber();
        System.out.println("Вы ввели число: " + number);
    }

    public static double userNumber() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите десятичное число");
        double number = 0;
        while (true) {
            try {
                number = scanner.nextFloat();
                return number;
            } catch (InputMismatchException e) {
                System.err.println("Введено не число. Повторите ввод");
                String line = scanner.nextLine();
            }
        }
    }
}
// ---------------------------------------------------------------------------------------------------------------------

/*
Задание №2
Если необходимо, исправьте данный код
(задание 2 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

try {
int d = 0;
double catchedRes1 = intArray[8] / d;
System.out.println("catchedRes1 = " + catchedRes1);
} catch (ArithmeticException e) {
    System.out.println("Catching exception: " + e);
}
 */

public class HomeWorkAppLesson2 {

    public static void main(String[] args) {
        int[] intArray = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9};
        try {
            int d = 0;
            double catchedRes1 = intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArrayIndexOutOfBoundsException | ArithmeticException e){
            System.err.println("Catching exception: " + e);
        }
    }
}
// ---------------------------------------------------------------------------------------------------------------------

/*
Задание №3
Дан следующий код, исправьте его там, где требуется
(задание 3 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

public static void main(String[] args) throws Exception {
    try {
        int a = 90;
        int b = 3;
        System.out.println(a / b);
        printSum(23, 234);
        int[] abc = { 1, 2 };
        abc[3] = 9;
    } catch (Throwable ex) {
        System.out.println("Что-то пошло не так...");
    } catch (NullPointerException ex) {
        System.out.println("Указатель не может указывать на null!");
    } catch (IndexOutOfBoundsException ex) {
        System.out.println("Массив выходит за пределы своего размера!");
    }
}
public static void printSum(Integer a, Integer b) throws FileNotFoundException {
    System.out.println(a + b);
}
*/

public class HomeWorkAppLesson2 {

    public static void main(String[] args) {
        printSum(null, 234);
    }

    public static void printSum(Integer a, Integer b) {
        try {
            try {
                int c = 90;
                int d = 0;
                System.out.println(c / d);
            } catch (ArithmeticException ex) {
                System.err.println("Деление на ноль!");
            }
            try {
                int[] abc = {1, 2};
                abc[3] = 9;
            } catch (IndexOutOfBoundsException ex) {
                System.err.println("Массив выходит за пределы своего размера!");
            }
            try {
                System.out.println(a + b);
            } catch (NullPointerException ex) {
                System.err.println("Указатель не может указывать на null!");
            }
        } catch (Exception ex) {
            System.err.println("Что-то пошло не так...");
        }
    }
}
// ---------------------------------------------------------------------------------------------------------------------

/*
Задание №4
Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
Пользователю должно показаться сообщение, что пустые строки вводить нельзя.
*/

import java.util.Scanner;

public class HomeWorkAppLesson2 {

    public static void main(String[] args) {
        emptyStr();
    }

    public static void emptyStr() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите что-нибудь!");
        String line = scanner.nextLine();
        if (!line.isEmpty() && line.equals("")) {
                System.out.println("Вы ввели: " + line);
        } else {
            System.err.println("Вы ничего не ввели!");
            throw new RuntimeException ("String is empty!");
        }
    }
}