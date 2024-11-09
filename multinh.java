
interface A {
  void show();
}

interface B extends A {
  void show();
}

interface C extends A {
  void show();
}

class D implements B, C {
  @Override
  public void show() {
    System.out.println("Overriden");
  }
}

public class multinh {
  public static void main(String[] args) {
    D d = new D();
    d.show();
  }
}
