package ArchitecturePO.Lesson3.Shape.exceptions;

public class CircleException extends RuntimeException {
    public CircleException() {
        super("Круг не существует");
    }
}