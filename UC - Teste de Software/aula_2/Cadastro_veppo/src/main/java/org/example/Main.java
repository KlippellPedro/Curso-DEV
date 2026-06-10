package org.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class Main {
    WebDriver driver; //Objeto que controla o navegador
    WebDriverWait wait; //Ojeto para esperas intelgentes

    @BeforeEach //Metodo executado antes de cada teste
    public void iniciar(){
        driver= new ChromeDriver();
        // Define uma espera maxima de 15 segundos
        wait = new WebDriverWait(driver, Duration.ofSeconds(15));

        driver.get("https://ecommerce.rodoviaria-poa.com.br/Principal");
        driver.manage().window().maximize(); //Maximiza a janela no navegador
    }
    // metodo auxiliar para criar pausas no codigo
    public void pausa(int tempo){
        try {
            Thread.sleep(tempo); // faz o codigo esperar o tempo informado
        }catch (InterruptedException e){
            e.printStackTrace(); // exibe erro caso ocorra interrupção
        }
    }
    @Test
    public void test(){
        // aguardo até que o botão do menu esteja clicavel
        WebElement menu = wait.until(ExpectedConditions.elementToBeClickable(By.name("hambTopmenu")));

        // executa cliqeu via JS (mais confiavel em alguns casos)
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();",menu);
        pausa(2000); // aguarda 2 segundos

        // aguarda até que o botão de cadastro esteja visivel
        WebElement cadastro = wait.until(ExpectedConditions.visibilityOfElementLocated(
                By.xpath("//*[@id=\"menu\"]/li[1]/div[2]/div/input[2]")
        ));

        // roda a tela até o botão de cadastro
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);",cadastro);

        // Clica no botão de cadastro vai JS
        ((JavascriptExecutor)driver).executeScript("arguments[0].click();", cadastro);
        pausa(3000);
    }
}