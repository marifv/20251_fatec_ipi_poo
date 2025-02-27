import javax.swing.JOptionPane;

public class SomaDoisNumeros {
    public static void main(String[] x) {
        // Declaração de variáveis
        double a, b, resultado;      
        // Entrada de dados
        a = Double.parseDouble(JOptionPane.showInputDialog("Digite o primeiro valor"));
        b = Double.parseDouble(JOptionPane.showInputDialog("Digite o segundo valor"));      
        // Processamento
        resultado = a + b;        
        // Saída
        JOptionPane.showMessageDialog(null, resultado);
    }
}

    
    