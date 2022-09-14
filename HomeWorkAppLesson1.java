package exceptions.lesson_01;

public class HomeWorkAppLesson1 {
    /*
    Задание №1
    Реализуйте 3 метода, чтобы в каждом из них получить разные исключения
     */
    public static void main(String[] args) {
//        indexOutArray();
//        objectToInteger();
        nullString();
    }

    public static void indexOutArray() {
        int[] arr = new int[]{1, 2};
        arr[3] = 3;
    }

    public static void objectToInteger() {
        Object objectOne = "1";
        Integer objectTwo = (Integer) objectOne;
    }

    public static void nullString() {
        String someString = null;
        System.out.println(someString.length());
    }
}
// ---------------------------------------------------------------------------------------------------------------------

public class HomeWorkAppLesson1 {
    /*
    Задание №2
    Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?
     */
    public static void main(String[] args) {
        String[][] matrix = new String[][]{
                {"1e", "0", "1"},
                {"1", "0", "1"},
                {"1", "1", "1"}};

        var sum = sum2d(matrix);
        System.out.println(sum);
    }

    public static int sum2d(String[][] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < 5; j++) {
                int val = Integer.parseInt(arr[i][j]);
                sum += val;
            }
        }
        return sum;
    }
}

/*
Возможно получить исключения:
1. "ArrayIndexOutOfBoundsException" в строке 49, где j < 5. Нужно написать j < arr[i].length
2. "NumberFormatException" в строке 50, т.к. массив arr с элементами класса String. Если в массиве будут только числа,
то исключение не выпадет и код сработает
 */
// ---------------------------------------------------------------------------------------------------------------------

import java.util.Arrays;

public class HomeWorkAppLesson1 {
    /*
    Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
    каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке.
    Если длины массивов не равны, необходимо как-то оповестить пользователя
     */
    public static void main(String[] args) {
        int[] arr1 = new int[]{1, 2, 3, 4};
        int[] arr2 = new int[]{5, 6, 7, 8};
        int[] arr3 = arrayDiff(arr1, arr2);
        String resultAsString = Arrays.toString(arr3);
        System.out.println(resultAsString);
    }

    public static int[] arrayDiff(int[] arr1, int[] arr2) {
        if (arr1.length != arr2.length) {
            throw new RuntimeException("Arrays have different size");
        }
        int[] result = new int[arr1.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = arr1[i] - arr2[i];
        }
        return result;
    }
}
// ---------------------------------------------------------------------------------------------------------------------

import java.util.Arrays;

public class HomeWorkAppLesson1 {
    /*
    Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
    каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке. Если длины массивов
    не равны, необходимо как-то оповестить пользователя. Важно: При выполнении метода единственное исключение,
    которое пользователь может увидеть - RuntimeException, т.е. ваше
     */
    public static void main(String[] args) {
        int[] arr1 = new int[]{15, 36, 28, 80};
        int[] arr2 = new int[]{5, 6, 0, 8};
        int[] arr3 = arrayDiv(arr1, arr2);
        String resultAsString = Arrays.toString(arr3);
        System.out.println(resultAsString);
    }

    public static int[] arrayDiv(int[] arr1, int[] arr2) {
        if (arr1.length != arr2.length) {
            throw new RuntimeException("Arrays have different size");
        }
        for (int i = 0; i < arr2.length; i++) {
            if (arr2[i] == 0) {
                throw new RuntimeException("Divide by zero. Index of number is: " + i);
            }
        }
        int[] result = new int[arr1.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = arr1[i] / arr2[i];
        }
        return result;
    }
}