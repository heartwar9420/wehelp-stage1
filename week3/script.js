let mergedData = [];
async function getData() {
    // 同時 fetch 兩個 JSON
    const [res1, res2] = await Promise.all([
        fetch('assignment-3-1.json'),
        fetch('assignment-3-2.json')
    ]);

    // 同時解析兩個 JSON
    const [textData, picsData] = await Promise.all([
      res1.json(),
      res2.json()
    ]);
    textData.rows.forEach(item => {
        const match = picsData.rows.find(p => p.serial === item.serial);
        if (!match || !match.pics) return;

        const imgParts = match.pics.split('/');
        const firstJpgIndex = imgParts.findIndex(p => p.includes('.jpg'));
        if (firstJpgIndex === -1) return;

        const imgPath = '/' + imgParts.slice(1, firstJpgIndex + 1).join('/');
        const firstImg = "https://www.travel.taipei" + imgPath;

        mergedData.push({
            serial : item.serial,
            title : item.sname,
            img : firstImg
        });
    });
    const promotions = document.querySelector('.promotions');

    promotions.innerHTML=""

    mergedData.slice(0,3).forEach((item, index) => {
        const promotions_block = document.createElement('div');
        promotions_block.classList.add(`promotion${index + 1}`);

        const img = document.createElement('img');
        img.src = item.img;

        const span = document.createElement('span');
        span.textContent = item.title;

        promotions_block.appendChild(img);
        promotions_block.appendChild(span);
        promotions.appendChild(promotions_block);
    });
    appendCards(3, 3 + currentCount);
}
function appendCards(start,end){
    const content_blocks = document.querySelector('.content_blocks');
    
    mergedData.slice(start,end).forEach((item,index) => {
        const li = document.createElement('li');
        li.classList.add(`card`);

        const img = document.createElement('img');
        img.classList.add('card_img');
        img.src = item.img;

        const star = document.createElement('img');
        star.classList.add('card_star');
        star.src = 'star.png';

        const span = document.createElement('span');
        span.classList.add('card_text');
        span.textContent = item.title;

        li.appendChild(img);
        li.appendChild(star);
        li.appendChild(span);
        content_blocks.appendChild(li);
    });
};

getData();

let currentCount = 10;
const STEP=10;
const loadmorebtn = document.getElementById('load-more-btn');

loadmorebtn.addEventListener('click',() =>
    {
    const start = 3 + currentCount;
    const end = 3 + currentCount + STEP;

    appendCards(start, end);
    currentCount += STEP;

    if (currentCount >= mergedData.length - 3) {
        loadmorebtn.style.display = 'none';
    }
});

const btn = document.getElementById('menuToggle'); //抓取漢堡按鈕元素
const panel = document.getElementById('menu'); //抓取右側選單元素
const iconHamburger = btn.querySelector('.icon-hamburger');//從按鈕裡面抓取漢堡圖片
const iconClose = btn.querySelector('.icon-close');//從按鈕裡面抓取關閉圖片
btn.addEventListener('click', () => 
    { //當使用者點擊按鈕後執行下列程式碼
    const isOpen = panel.classList.toggle('active');//切換選單樣式、並且記錄目前是開還是關
    btn.classList.toggle('active', isOpen); //讓css生效
    iconHamburger.hidden = isOpen; //針對狀態決定是否隱藏 hamburger.png
    iconClose.hidden = !isOpen; //針對狀態決定是否隱藏 close.png
});