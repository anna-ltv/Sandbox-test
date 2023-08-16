package ru.org.autotests;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.chrome.ChromeOptions;

import java.time.Duration;

public class UITestingPlaygroundTests {

    private WebDriver driver;

    @Before
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "C:\\WebDriver\\chromedriver.exe");
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        try {
            driver = new ChromeDriver(options);
            driver.get("http://uitestingplayground.com/");
        } catch (Exception e) {
            // Handle the exception, e.g., print an error message
            e.printStackTrace();
        }
    }

    @After
    public void tearDown() {
        driver.quit();
    }

    @Test
    public void testDynamicButton() {
        driver.findElement(By.linkText("Dynamic ID")).click();
        driver.findElement(By.className("btn-primary")).click();

        // Assertions to check the correct page and correct button name
        assert driver.getPageSource().contains("Dynamic ID");
        assert driver.findElement(By.className("btn-primary")).getText().equals("Button with Dynamic ID");
    }

    @Test
    public void testClassAttribute() {
        driver.findElement(By.linkText("Class Attribute")).click();
        assert driver.getPageSource().contains("Class Attribute");

        driver.findElement(By.xpath("//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")).click();
        try {
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5)); // Set the timeout using Duration
            wait.until(ExpectedConditions.alertIsPresent());
            Alert alert = driver.switchTo().alert();
            alert.accept();
        } catch (NoAlertPresentException e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testHiddenLayers() {
        driver.findElement(By.linkText("Hidden Layers")).click();
        assert driver.getPageSource().contains("Hidden Layers");

        WebElement greenButton = driver.findElement(By.id("greenButton"));
        greenButton.click();

        // Wait for the blue button to appear
        WebElement blueButton = new WebDriverWait(driver, Duration.ofSeconds(7)) // Set the timeout using Duration
                .until(ExpectedConditions.presenceOfElementLocated(By.id("blueButton")));
        blueButton.click();
        assert blueButton.isEnabled();
    }

    @Test
    public void testClick() {
        driver.findElement(By.linkText("Click")).click();
        assert driver.getPageSource().contains("Click");

        // Click the button
        WebElement firstClick = driver.findElement(By.id("badButton"));
        String initialClass = firstClick.getAttribute("class");
        firstClick.click();
        String updatedClass = firstClick.getAttribute("class");

        // Assert that the class has changed from "btn btn-primary" to "btn btn-success"
        assert initialClass.equals("btn btn-primary");
        assert updatedClass.equals("btn btn-success");
    }

    @Test
    public void testTextInput() {
        driver.findElement(By.linkText("Text Input")).click();
        assert driver.getPageSource().contains("Text Input");

        // Enter a new button name in the field
        String newButtonName = "New Button";
        WebElement inputField = driver.findElement(By.className("form-control"));
        inputField.sendKeys(newButtonName);

        // Click the button to change name
        WebElement changeButtonName = driver.findElement(By.id("updatingButton"));
        changeButtonName.click();

        // Assert the button name has been changed
        assert driver.findElement(By.id("updatingButton")).getText().equals(newButtonName);
    }
}
