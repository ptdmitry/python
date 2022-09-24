package exceptions.lesson_03;

public class DateOfBirthException extends Exception {

    public DateOfBirthException() {
        super("Неверно ввели дату рождения");
    }

}