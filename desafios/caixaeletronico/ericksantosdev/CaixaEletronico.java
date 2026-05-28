package CodeBR;

import java.util.Locale;
import java.util.Scanner;

public class CaixaEletrônico {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        // Variabeis

        String nome;
        int opcao;
        double saque, deposito, saldo;

        // Impress

        System.out.println("Digite seu nome: ");
        nome = sc.nextLine();
        System.out.println("Digite seu saldo: ");
        saldo = sc.nextDouble();


        System.out.println("Carregando sistema...");


        System.out.println("1- Sacar ");
        System.out.println("2- Depositar ");
        opcao = sc.nextInt();


        // System

        switch(opcao){

            case 1: {
                System.out.println("Selecionado: Saque ");
                System.out.println("Informe o valor a ser sacado: ");
                saque = sc.nextDouble();

                if (saldo >= saque)
                {

                    saldo -= saque;
                    System.out.println("Ola, " + nome);
                    System.out.println("Saque realizado com sucesso");
                    System.out.printf("Saldo Atual: %.2f\n", saldo);
                    System.out.printf("Valor Sacado: %.2f\n", saque);

                }
                else
                {
                    System.out.println("Saldo insuficiente");
                }
                break;
            }
            case 2: {

                System.out.println("Selecionado: Depositar ");
                System.out.println("Informe o valor a ser depositado: ");
                deposito = sc.nextDouble();

                saldo += deposito;

                System.out.println("Depositado realizado com sucesso");
                System.out.printf("Saldo atual: %.2f\n", saldo);
                System.out.printf("Valor Depositado:  %.2f\n", deposito);
                break;
            }

        }

sc.close();
    }
}