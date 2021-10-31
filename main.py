from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome('/Users/parthvyas/chromeDriver/chromedriver')
expr = ["x+x+x+x", "3*x+a/a+b*x","2*x*x*x/y*x/x+x*y","2^x/2^2*x","(2*(x^2)+5*x-3)/(6*(x^2)+18*x)","3*x*a*b/a*c","(x^2+5*x-6)/(2-x)^2", "(sin(x))^2+(cos(x))^2", "(sin(x)+cos(x))/sin(x)","(x^2+y^2)*x/(24*x+y)","((x-1)/(x-2))+((x+1)/(x+2))", "((x-1)/(x-2))-((x+1)/(x+2))","((x-1)/(x-2))*((x+1)/(x+2))","((x-1)/(x-2))/((x+1)/(x+2))","(3*(x^2)*sin(x)+x*sin(x))/(sin(x)*cos(x))","(9/(3*(x^2)-3*y^2))+(x/(x*y-x^2))","(((x^2)+33*(x^2)+19*(x^2)+4*(x^2))*(4*(y^2)+3*(y^2)+2*y^2))/(3*(x^2)*(4*y^2)*(3*b^2)*(9*a^2)*(4*c^2)*(54*x^2))","(e^(x*x)-e^((-1)*x*x))/2*x","(e^(x*x)+e^((-1)*x*x))/2*x","sin(x)*sin(y)+cos(x)*cos(y)","(((3/(x-5))-(4/(x+5)))*(x+5)*(x-5))/(((7/((x+5)*(x-5))))*(x+5)*(x-5))","(((sin((x^2)+y^2))*(x^2)*(y^2))/((cos((x^2))+y^2)/(cos(x^2+1))))","(((sin((x^2)+y^2))*(x^2)*(y^2))/((cos((x^2))+y^2)/(cos(x^2+1))))/((exp(x^2)*x*a*b*c*y))","(tan(x)/cos(x))/(sin(x)/cos(x))/cot(x) + (x^2)*sin(tan(x)/cos(x))", "3*x*x/x^2","2*2/2*x", "x*x", "exp(ln(x))", "2*2/2^18","27/3^x"];
runTime = [0]*len(expr)

browser.get('https://www.wolframalpha.com/input/')
browser.fullscreen_window()
search = browser.find_element_by_class_name("_2oXzi")
search.send_keys('simplify '+ expr[0])
press = browser.find_element_by_css_selector('button[type="submit"]')

start = time.time()
press.click()

browser.implicitly_wait(5)

hovering = ActionChains(browser)
hover = browser.find_element_by_xpath('(//div[@class="Y4YRs"])[3]')
hovering.move_to_element(hover).perform()

hover_click = browser.find_element_by_xpath('(//button[@type="button"])[15]')
hovering.move_to_element(hover_click).click().perform()
end = time.time()
print(end-start)

browser.implicitly_wait(10)
browser.close()

















