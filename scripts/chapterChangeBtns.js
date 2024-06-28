// Getting the buttons
const bergerBar = document.getElementById("menueIcon");
const cutAndExit = document.getElementById("exit");

const documentNavigationBar = document.getElementById("bergerNavigation");
const documentMainContent = document.getElementById("mainBody");

const topMangaSelect = document.getElementById("topSelection");
const nextPageBtn1 = document.getElementById("nextBtn1");
const nextPageBtn2 = document.getElementById("nextBtn2");

const buttonMangaSelect = document.getElementById("buttonSelection");
const prevPageBtn1 = document.getElementById("prevBtn1");
const prevPageBtn2 = document.getElementById("prevBtn2");


// Function to the next page
function pageNavigation(newChapter, oldChapter, mangaTopic) {
    const totalChapters = (document.getElementById("totalChapters")).innerHTML;

    if (newChapter > 0) {
        if (newChapter <= totalChapters) {
            // Getting the manga name
            let mangaName = (mangaTopic.innerHTML).replace(` Chapter ${oldChapter}`, '');
            // console.log(chapter);
            // console.log(mangaName);
            mangaTopic.innerText = `${mangaName} Chapter ${newChapter}`;

            // Going to the file and reading the content in noChapter.txt notepad
            fetch(`../../Resources/manga/${mangaName}/Chapter ${newChapter}/noChapter.txt`)
                .then(response => {
                    return response.text();
                })

                .then(text => {
                    text = parseInt(text);

                    const images = document.getElementById("mangaImages");

                    // Getting the img link list from the files 
                    fetch(`../../Resources/manga/${mangaName}/Chapter ${newChapter}/linkList.txt`)
                        .then(respose => {
                            return respose.text();
                        })

                        .then(text => {
                            let lines = text.split('\n');
                            let htmlTag = `<img src="${lines[0]}" alt="img1"></img>`
                            // console.log(htmlTag);

                            for (let i = 1; i <= ((lines.length)-1); i++) {
                                htmlTag = `${htmlTag}\n<img src="${lines[i]}" alt="img${i}">`
                            }

                            images.innerHTML = htmlTag;
                        })
                })
        }
    }
}

// Funtion to go to the next page 
function nextPage() {
    // Getting the manga chapter
    const mangaTopic = document.getElementById("chapterName");
    let chapter = parseInt((mangaTopic.innerHTML).replace(/\D/g, ''));

    let newChapter = chapter + 1;
    let oldChapter = chapter;

    console.log(newChapter);
    console.log(oldChapter);
    pageNavigation(newChapter, oldChapter, mangaTopic);
    updateChapter(newChapter);
}

// Funtion to go to the previous page
function prevPage() {
    // Getting the manga chapter
    const mangaTopic = document.getElementById("chapterName");
    let chapter = parseInt((mangaTopic.innerHTML).replace(/\D/g, ''));

    let newChapter = chapter - 1;
    let oldChapter = chapter;

    console.log(newChapter);
    console.log(oldChapter);
    pageNavigation(newChapter, oldChapter, mangaTopic);
    updateChapter(newChapter);
}

// Changing the selected opption
function mangaSelect() {
    // Geting the selected chapter number 
    const selectedOption = this.options[this.selectedIndex].text;
    let chapter = parseInt(selectedOption.replace(/\D/g, ''));

    // Getting the current chapter number 
    const mangaTopic = document.getElementById("chapterName");
    let oldChapter = parseInt((mangaTopic.innerHTML).replace(/\D/g, ''));

    // Scroling to the top of the web page
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });

    console.log(chapter);
    console.log(oldChapter);

    // Calling for chapter update and page update funtions
    pageNavigation(chapter, oldChapter, mangaTopic);
    updateChapter(chapter);
}

// Updating the current chapter
function updateChapter(newChapter) {
    const topChapters = document.querySelectorAll("#topSelection option");
    const bottomChapters = document.querySelectorAll("#buttonSelection option");

    // Adding selected for the options 
    function updateChapterOption(chapters) {
        const totalChapters = (document.getElementById("totalChapters")).innerHTML;

        if (newChapter <= totalChapters) {
            chapters.forEach((chapter, index) => {
                chapter.selected = false;
            })

            console.log(`Test: ${newChapter}`);

            chapters[newChapter - 1].selected = true;
            console.log(chapters[newChapter]);
        }
    }

    updateChapterOption(topChapters);
    updateChapterOption(bottomChapters);
}

// Hamberger bar Navigations
function bergerBarNavigation() {
    // Changing the display settings
    documentMainContent.setAttribute("class", "notDisplay");
    documentNavigationBar.setAttribute("class", "doDisplay");

    cutAndExit.addEventListener("click", function () {
        documentMainContent.setAttribute("class", "");
        documentNavigationBar.setAttribute("class", "notDisplay");
    });
}

// Mouse cussor change 
function cursorShange() {
    bergerBar.style.cursor = 'pointer';
    cutAndExit.style.cursor = 'pointer';
}

// Calling the funtions
bergerBar.addEventListener("click", bergerBarNavigation);

bergerBar.addEventListener("mouseover", cursorShange);
cutAndExit.addEventListener("mouseover", cursorShange);

topMangaSelect.addEventListener("change", mangaSelect);
nextPageBtn1.addEventListener("click", nextPage);
nextPageBtn2.addEventListener("click", nextPage);

buttonMangaSelect.addEventListener("change", mangaSelect);
prevPageBtn1.addEventListener("click", prevPage);
prevPageBtn2.addEventListener("click", prevPage);