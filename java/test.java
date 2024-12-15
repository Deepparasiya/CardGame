package java;

import java.util.*;

public class test{
    public static void main(String[] args){
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("What is youe favourite web programming language? ");
            String answer = scanner.nextLine();
            System.out.println("Your answer was: " + answer);
        }
    }
}