package ArchitecturePO.Lesson3.Shape.interFaceAction;

public interface ICircleable {

    default int ICircleLength(int radius) {
        return (int) (2 * Math.PI * radius);
    }

    default int IArea(int radius) {
        return (int) (Math.PI * radius * radius);
    }
}