import java.util.Scanner;
public class SomaDoisNumeros{
    static public void main(String [] x){
        //declaração de variáveis
        Scanner leitor = new Scanner(System.in);
        int a, b;
        int resultado;
        //entrada de dados
        System.out.println("Digite o primero valor");
        a = leitor.nextInt();
        System.out.println("Digite o segundo valor");
        b = leitor.nextInt();
        //processamento
        resultado = a + b;
        //saida
        System.out.printf("%d + %d = %d", a, b, resultado);
    }
}
    
    