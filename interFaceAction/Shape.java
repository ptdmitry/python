package ArchitecturePO.Lesson3.Shape.interFaceAction;

public abstract class Shape {
    public abstract String name();
    public abstract int area();
    public abstract int perimeter();
    public int circleLength() {
        return 0;
    }
}