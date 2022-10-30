package ArchitecturePO.Lesson3.Shape.interFaceAction;

public interface IPolygonable {
    static int IPerimeter(int length) {
        return length * 4;
    }
    default int IArea(int length) {
        return length * length;
    }
    static int IPerimeter(int length, int width) {
        return (length + width) * 2;
    }
    default int IArea(int length, int width) {
        return length * width;
    }
    static int IPerimeter(int side1, int side2, int side3) {
        return side1 + side2 + side3;
    }
    default int IArea(int side1, int side2, int side3) {
        return (int) (side1 + side2 + side3) / 2;
    }
}