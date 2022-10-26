package ArchitecturePO.Lesson3.Shape.interFaceAction;

public interface IRectangleable {

    default int IPerimeter(int length) {
        return length * 4;
    }

    default int IArea(int length) {
        return length * length;
    }

    default int IPerimeter(int length, int width) {
        return (length + width) * 2;
    }

    default int IArea(int length, int width) {
        return length * width;
    }
}