package exceptions.lesson_03;

public class NumberPhoneException extends NumberFormatException {
    public NumberPhoneException() {
        super("Неверно ввели номер телефона");
    }
}

