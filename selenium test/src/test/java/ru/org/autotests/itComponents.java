package ru.org.autotests;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;

import java.time.Duration;

public class itComponents {
    public static void main(String[] args) {

        //setting the driver executable
        System.setProperty("webdriver.chrome.driver", "C:\\WebDriver\\chromedriver.exe");

//Initiating your chromedriver
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));

//maximize window
        driver.manage().window().maximize();

//open browser with desired URL
        driver.get("http://qcmdbui.qworktest.qrun.diasoft.ru/");
        //enter username and password
        WebElement login = driver.findElement(By.cssSelector("input[id='username']"));
        login.sendKeys("guest");
        WebElement password = driver.findElement(By.cssSelector("input[id='password']"));
        password.sendKeys("12345678");
        password.sendKeys(Keys.ENTER); //press Enter from keyboard


        //closing the browser
        driver.quit();
    }
}
