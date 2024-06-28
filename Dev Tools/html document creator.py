# HTML funtion
def htmlPage(mangaName, noOfChapters, htmlChapterList, htmlChapterImgList, summery):
    htmlPageContent = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../../styling/commonStyles.css">
    <link rel="stylesheet" href="../../styling/mangaPageStyles.css">
    <link rel="icon" href="../../Resources/default/tabLogo.png">
    <title>Wolf Maina</title>
</head>

<body>
    <div class="notDisplay" id="bergerNavigation">
        <div>
            <p id="exit">X</p>
            <div>
                <a href="../../index.html">HOME</a>
                <a href="../Default/aboutUs.html">ABOUT&nbsp;US</a>
            </div>
        </div>
    </div>

    <div class="" id="mainBody">
        <!-- Top navigation area -->
        <div class="navigationBar">
            <section>
                <p id="menueIcon">☰</p>
            </section>
            <section class="logoSection">
                <a href="../../index.html">
                    <img src="../../Resources/default/logo.png" alt="Web Page Logo">
                    <p id="logoText">Wolf Mania</p>
                </a>
            </section>
            <section>
                <a href="../../index.html">
                    <img src="../../Resources/default/login.png" alt="Home Icon" id="homeImg">
                </a>
            </section>
        </div>

        <!-- Chapter name -->
        <div class="chapterContent">
            <p id="chapterName">{mangaName} Chapter 1</p>
            <p id="totalChapters" style="display: none;">{noOfChapters}</p>
        </div>

        <!-- Top chapter selection area -->
        <div class="topSelectionArea">
            <select class="chapters" id="topSelection">
                <option selected>Chapter 1</option>
                {htmlChapterList}
            </select><br>

            <button type="button" class="navigationBtns" id="nextBtn1">Next &gt;</button>
            <button type="button" class="navigationBtns" id="prevBtn1">&lt; Prev</button>
        </div>

        <!-- Manga section -->
        <div class="manga">
            <img src="../../Resources/default/begin.webp" alt="Begining Page" id="begin">
            <div id="mangaImages">
                <!-- Incerting img tags from js -->
                {htmlChapterImgList}
            </div>
            <img src="../../Resources/default/end.webp" alt="Ending Page">
        </div>

        <!-- Bottem chapter selection area -->
        <div class="BottonSelectionArea">
            <select class="chapters" id="buttonSelection">
                <option selected>Chapter 1</option>
                {htmlChapterList}
            </select>

            <a href="#"><button type="button" class="navigationBtns" id="nextBtn2">Next &gt;</button></a>
            <a href="#"><button type="button" class="navigationBtns" id="prevBtn2">&lt; Prev</button></a>
        </div>

        <!-- Manga Summery -->
        <div class="Summery">
            <p>&emsp;&emsp;{summery}</p>
        </div>

        <!-- Go to top button -->
        <div class="topBtn">
            <a href="#">
                <div>
                    <h2>^</h2>
                </div>
            </a>
        </div>

        <footer>
            <div class="disclaimer">
                <h1>Disclaimer!!</h1>
                <p>The content available on this website is not the original work of our organization. We do not
                    claim ownership of the manga and other related content provided here. All rights and credits go to
                    the
                    respective authors and publishers.<br><br>

                    &emsp;&emsp;Sharing the web links or distributing the content found on this site with others is
                    strictly
                    prohibited.
                    Unauthorized sharing or distribution. We kindly request all users to
                    respect these guidelines to ensure the continued availability of the content.</p>
            </div>

            <div class="lowerNavigationBar">
                <div>
                    <a href="../../index.html">HOME</a>
                    <a href="../Default/aboutUs.html">ABOUT&nbsp;US</a>
                </div>
                <hr>
                <p>&copy;&nbsp;All rights reserved 2024</p>
            </div>
        </footer>
    </div>

    <script src="../../scripts/chapterChangeBtns.js"></script>
</body>

</html>"""
    
    return htmlPageContent




# Getting the Chapter list
def chapterList(noOfChapters):
    chapterPrint = "<option>Chapter 2</option>"
    
    for i in range(3, (int(noOfChapters)+1)):
        chapterPrint = f"{chapterPrint}\n\t\t<option>Chapter {i}</option>"
        
    return chapterPrint




# Getting the Img list
def chapterImgList(chapter1Imgs, mangaName):
    chapterImgPrint = f"""<img src="../../Resources/manga/{mangaName}/Chapter 1/1.webp" alt="Page 1">"""
    
    for i in range(2, (int(chapter1Imgs)+1)):
        chapterImgPrint = f"""{chapterImgPrint}\n\t\t<img src="../../Resources/manga/{mangaName}/Chapter 1/{i}.webp" alt="Page {i}">"""
        
    return chapterImgPrint 




# Getting the user inputs
mangaName = input("Enter the manga name: ")
noOfChapters = input("Enter the number of chapters: ")
chapter1Imgs = input("Enter the number of imgs in chapter 1: ")
summery = input("Enter the summery of the manga: ")

# Callling for the funtions
htmlChapterList = chapterList(noOfChapters)
htmlChapterImgList = chapterImgList(chapter1Imgs, mangaName)
htmlPage(mangaName, noOfChapters, htmlChapterList, htmlChapterImgList, summery)

# Writing the html file
content = htmlPage(mangaName, noOfChapters, htmlChapterList, htmlChapterImgList, summery)

with open(f"{mangaName}.html", "w", encoding='utf-8') as file:
    file.write(content)
    print("\n\n\nFileWriting Sucessfull!!")