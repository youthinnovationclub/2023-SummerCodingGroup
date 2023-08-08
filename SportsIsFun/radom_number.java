import java.util.*;

public class radom_number {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("number the of letter length:");
        int t= scan.nextInt();
        char st;
        String list[] = new String[t];
       for(int i=0;i<t;i++){
           int min=65;
           int max=90;
           int random_int = (int)Math.floor(Math.random() * (max - min + 1) + min);
           st= (char) random_int;
           String change=String.valueOf(st);
           list[i]=change;

        }
        StringBuffer sb = new StringBuffer();
        for(int i = 0; i <list.length; i++) {
            sb.append(list[i]);
        }

       System.out.println(sb);
    }
}
