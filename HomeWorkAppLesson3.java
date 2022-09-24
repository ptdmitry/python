package exceptions.lesson_03;

/*
Напишите приложение, которое будет запрашивать у пользователя следующие данные в произвольном порядке,
разделенные пробелом: Фамилия Имя Отчество датарождения номертелефона пол

Форматы данных:
фамилия, имя, отчество - строки
дата_рождения - строка формата dd.mm.yyyy
номер_телефона - целое беззнаковое число без форматирования
пол - символ латиницей f или m.

Приложение должно проверить введенные данные по количеству. Если количество не совпадает с требуемым,
вернуть код ошибки, обработать его и показать пользователю сообщение, что он ввел меньше или больше данных,
чем требуется.

Приложение должно попытаться распарсить полученные значения и выделить из них требуемые параметры.
Если форматы данных не совпадают, нужно бросить исключение, соответствующее типу проблемы.
Можно использовать встроенные типы java и создать свои. Исключение должно быть корректно обработано,
пользователю выведено сообщение с информацией, что именно неверно.

Если всё введено и обработано верно, должен создаться файл с названием, равным фамилии,
в него в одну строку должны записаться полученные данные, вида
<Фамилия><Имя><Отчество><датарождения> <номертелефона><пол>

Однофамильцы должны записаться в один и тот же файл, в отдельные строки.

Не забудьте закрыть соединение с файлом.

При возникновении проблемы с чтением-записью в файл, исключение должно быть корректно обработано,
пользователь должен увидеть стектрейс ошибки.
 */

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class HomeWorkAppLesson3 {

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите свои данные - ФИО, дата рождения, номер телефона и пол в следующем формате\n" +
                "'Сидоров Иван Петрович 01.01.1992 89172583214 m'");
        String userStr = scanner.nextLine();
        int ex = userDataParser(userStr);
        if (ex == -1) {
            System.err.println("Введено меньше данных, чем требуется");
        } else if (ex == -2) {
            System.err.println("Введено больше данных, чем требуется");
        } else if (ex == 0) {
            System.out.println("Данные успешно записаны");
        }
    }

    static int userDataParser(String userStr) throws IOException {
        String[] standardList = new String[6];
        String[] userList = userStr.split(" ");
        if (userList.length < standardList.length) {
            return -1;
        } else if (userList.length > standardList.length) {
            return -2;
        }
        try {
            // Обработка номера телефона
            Pattern patternPhone = Pattern.compile("[0-9]{11}");
            Matcher matcherPhone = patternPhone.matcher(userStr);
            BigInteger phoneNumber = null;
            while (matcherPhone.find()) {
                phoneNumber = new BigInteger(userStr.substring(matcherPhone.start(), matcherPhone.end()));
            }
            if (phoneNumber != null) {
                try {
                    // Обработка даты рождения
                    Pattern patternDate = Pattern.compile("[0-31]{2}\\.[0-12]{2}\\.[0-9]{4}");
                    Matcher matcherDate = patternDate.matcher(userStr);
                    String dateOfBirth = null;
                    while (matcherDate.find()) {
                        dateOfBirth = userStr.substring(matcherDate.start(), matcherDate.end());
                    }
                    if (dateOfBirth != null) {
                        try {
                            // Обработка пола
                            Pattern patternMaleFemale = Pattern.compile("[fm]");
                            Matcher matcherMaleFemale = patternMaleFemale.matcher(userStr);
                            String userMaleFemale = null;
                            while (matcherMaleFemale.find()) {
                                userMaleFemale = userStr.substring(matcherMaleFemale.start(), matcherMaleFemale.end());
                            }
                            if (userMaleFemale != null) {
                                userFile(userStr, userList);
                                return 0;
                            } else {
                                throw new maleFemaleException();
                            }
                        } catch (maleFemaleException e) {
                            System.err.println(e.getMessage());
                        }
                    } else {
                        throw new DateOfBirthException();
                    }
                } catch (DateOfBirthException e) {
                    System.err.println(e.getMessage());
                }
            } else {
                throw new NumberPhoneException();
            }
        } catch (NumberPhoneException e) {
            System.err.println(e.getMessage());
        }
        return -3;
    }

    static void userFile(String userStr, String[] userList) throws IOException {
        // System.out.println(Arrays.toString(userList));
        if (Files.exists(Path.of("C:\\" + userList[0] + ".txt"))) {
            BufferedWriter writer = new BufferedWriter(new FileWriter("C:\\" + userList[0] + ".txt", true));
            writer.append(userStr).append("\n");
            writer.close();
        } else {
            Files.createFile(Path.of("C:\\" + userList[0] + ".txt"));
            BufferedWriter writer = new BufferedWriter (new FileWriter("C:\\" + userList[0] + ".txt"));
            writer.write("<Фамилия><Имя><Отчество><датарождения><номертелефона><пол>\n" + userStr + "\n");
            writer.close();
        }
    }
}