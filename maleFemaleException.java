package exceptions.lesson_03;

public class maleFemaleException extends Exception {

    public maleFemaleException() {
        super("Неверно ввели пол");
    }
}