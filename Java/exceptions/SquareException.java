package ArchitecturePO.Lesson3.Shape.exceptions;

public class SquareException extends RuntimeException {
    public SquareException() {
        super("Квадрат не существует");
    }
}