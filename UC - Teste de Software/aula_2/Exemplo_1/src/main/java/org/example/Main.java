package org.example;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Main {
    WebDriver driver;
    @Test
    public void  test(){
        driver =new ChromeDriver();
        driver.get("http://www.facebook.com");

        //para acessar pelo Firefox
        driver =new FirefoxDriver();
        driver.get("http://www.facebook.com");

        //para acessar pelo Edge

        driver =new EdgeDriver();
        driver.get("http://www.facebook.com");
    }
}