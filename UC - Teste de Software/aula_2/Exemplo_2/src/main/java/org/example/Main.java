package org.example;

import org.testng.annotations.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Main {
    WebDriver driver;
    @Test
    public void  test(){
        driver =new ChromeDriver();
        driver.get("https://apsweb.senacrs.com.br/modulos/aluno/login.php5?");

        //para acessar pelo Firefox
        driver =new FirefoxDriver();
        driver.get("https://apsweb.senacrs.com.br/modulos/aluno/login.php5?");

        //para acessar pelo Edge

        driver =new EdgeDriver();
        driver.get("https://apsweb.senacrs.com.br/modulos/aluno/login.php5?");
    }
}