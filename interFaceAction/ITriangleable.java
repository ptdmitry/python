package ArchitecturePO.Lesson3.Shape.interFaceAction;

public interface ITriangleable {

    default int IPerimeter(int side1, int side2, int side3) {
        return side1 + side2 + side3;
    }

    default int IArea(int side1, int side2, int side3) {
        return (int) (side1 + side2 + side3) / 2;
    }
}