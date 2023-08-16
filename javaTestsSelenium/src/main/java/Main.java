import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Main {
    public static void main(String[] args) {
        System.setProperty("webdriver.crome.driver", "C:\\WebDriver\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        //maximize window
        driver.manage().window().maximize();

//open browser with desired URL
        driver.get("http://qcmdbui.qcmdb.qrun.diasoft.ru/");
//enter username and password
        WebElement login = driver.findElement(By.id("username"));
        login.sendKeys("guest");
        WebElement password = driver.findElement(By.id("password"));
        password.sendKeys("12345678");
        //click the button
        WebElement button = driver.findElement(By.className("q-button"));
        button.click();

//open component Планирование поставок
        WebElement delivery = driver.findElement(By.xpath("/html/body/app-root/div/app-sidebar/div/div/div[2]/nav/ul/app-sidebar-inner/li/ul/app-sidebar-inner/li[2]/button/span"));
        delivery.click();

        //find and click button Добавить поставку
        driver.findElement(By.className("q-button.q-button--primary.ng-star-inserted")).click();

        //closing the browser
        driver.quit();
    }
}
