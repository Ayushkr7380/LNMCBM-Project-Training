import java.util.*;
class javaswitch{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while(true)
        {

            System.out.println("----Choose any option----");
            System.out.println("Press 1 for Perimeter of Rectangle");
            System.out.println("Press 2 for Area of Rectangle");
            System.out.println("Press 3 for Perimeter of Square");
            System.out.println("Press 4 for Area of Square");
            System.out.println("Press 5 for Circumference  of Circle");
            System.out.println("Press 6 for Area of Circle");
            System.out.println("Press 0 for Quit");
            System.out.println("Enter the number between 0 to 6 : ");
            int choice = sc.nextInt();

            // Switchcase
            if(choice ==0){
                break;

            }
            else
            {
                switch(choice){
                    case 1:
                        System.out.println("Enter the length of the rectangle: ");
                        double length1 = sc.nextDouble();

                        System.out.println("Enter the breadth of the rectangle: ");
                        double breadth1 = sc.nextDouble();
                        
                        double perimeter1 = 2*(length1 + breadth1);
                        System.out.println("Perimeter of rectangle is "+perimeter1);
                        break;
                    case 2:
                        System.out.println("Enter the length of the rectangle: ");
                        double length2 = sc.nextDouble();

                        System.out.println("Enter the breadth of the rectangle: ");
                        double breadth2 = sc.nextDouble();
                        
                        double area1 = length2 * breadth2;
                        System.out.println("Area of rectangle is "+area1);
                        break;
                    case 3:
                        System.out.println("Enter the side of square: ");
                        double side1 = sc.nextDouble();
                        
                        double perimeter2 = 4 * side1;
                        System.out.println("Perimeter of square is "+perimeter2);
                        break;
                    case 4:
                        System.out.println("Enter the side of square: ");
                        double side2 = sc.nextDouble();
                        
                        double area2 = side2 * side2;
                        System.out.println("Area of square is "+area2);
                        break;
                    case 5:
                        System.out.println("Enter the radius of circle: ");
                        double rad1 = sc.nextDouble();
                        
                        double circum1 = 2 * 3.14 * rad1;
                        System.out.println("Circumfernce of a circle is "+circum1);
                        break;
                    case 6:
                        System.out.println("Enter the radius of circle: ");
                        double rad2 = sc.nextDouble();
                        
                        double area3 = 3.14 * rad2 * rad2;
                        System.out.println("Area of a circle is "+area3);
                        break;
                    default:
                        System.out.println("Invalid Choice.");
                }
            }
        }
    }
} 