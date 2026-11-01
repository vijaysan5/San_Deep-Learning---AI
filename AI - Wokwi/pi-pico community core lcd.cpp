// pi-pico community core lcd - 1602

//  >>> 1_____:

#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 10, 9, 8, 7);

void setup() {
  lcd.begin(16, 2);
  lcd.print(" Mayiladuthurai");

  lcd.setCursor(2, 1);
  lcd.print("TN 68 A 5770");
}

void loop() {
  delay(1); // Adding a delay() here speeds up the simulation
}



//  >>> 2______:
// LCD1602 and Pi Pico!

#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 10, 9, 8, 7);

void setup() {
  lcd.begin(16, 2);
  lcd.print(" Mayiladuthurai");

  lcd.setCursor(2, 1);
  lcd.print("TN 68 A 5770");
}

void loop() {
  delay(1000); // Adding a delay() here speeds up the simulation
  lcd.print("   ");
  delay(500);
  lcd.begin(16,2);
  lcd.print(" Mayiladuthurai");
  delay(500);
  lcd.setCursor(1,1);
  lcd.print("Welcome to 5770");
}