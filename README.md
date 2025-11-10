# 🚀 **Rocket Type Tester**

*A Pygame-based typing practice and reaction skill game.*

## **Overview**

This project is an interactive typing game built using **Python** and **Pygame**. Players are presented with words and must type them correctly before time runs out. The game features multiple screens including a main menu, tutorial pages, and gameplay. It tracks accuracy and speed, helping users improve typing fluency.

## **Features**

* 🎮 **Main Menu Navigation**
* ⌨️ **Real-time Typing Input**
* 🧠 **Word Display & Progression**
* 🕒 **Timer / Speed Feedback**
* 📊 **Score & Accuracy Display**
* 📚 **Step-by-step Tutorial Screens**
* 🎨 **Custom Graphics & Backgrounds**

## **Controls**

| Key           | Action                           |
| ------------- | -------------------------------- |
| **SPACE**     | Advance menus & tutorial screens |
| **ESC**       | Return/exit certain screens      |
| **Type keys** | Enter your typing input          |
| **ENTER**     | Submit typed word                |

## **Requirements**

Make sure you have Python installed, then install Pygame:

```bash
pip install pygame
```

## **How to Run**

1. Clone or download this repository.
2. Ensure the `images/` folder is present, containing required image assets.
3. Run the game:

```bash
python main.py
```

## **Project Structure**

```
project/
│ main.py
│
└── images/
    ├── background.png
    ├── <tutorial images>
    └── jfkAU4tM8XMUAPZDm4h5Nh-1200-80.jpeg
```

## **Screenshots**

Below are sample screens from the game, demonstrating menus, tutorials, and gameplay.

| Menu                        | Loading Screen                    | Gameplay                    |
| --------------------------- | --------------------------- | --------------------------- |
| ![](assets/images/img1.png) | ![](assets/images/img2.png) | ![](assets/images/img3.png) |

| Results & Accuracy Display                  | Tutorial 1            | Tutorial 2           
| --------------------------- | --------------------------- | --------------------------- 
| ![](assets/images/img4.png) | ![](assets/images/img5.png) | ![](assets/images/img6.png) 

## **Notes**

* The game uses multiple image assets for UI and tutorial slides.
* The screen resolution, word lists, and colors can be adjusted inside `MainMenu` and game classes.