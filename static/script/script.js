// Global Varibales
var DropDownOpen = false;
function openTab(evt, tabName){
    var tab, workArea;
    workArea = document.getElementsByClassName('tab')
    
    for (let i = 0; i < workArea.length; i++) {
        const element = workArea[i];
        element.style.display = "none";
    }

    tab =  document.getElementById(tabName);
    tab.style.display = "block";
}

function CloseModal(evt){
    var modal = document.getElementById('popup');
    modal.style.display = 'none';
}

function OpenModal(evt, tabName) {
    var modal, modalContent, content;
    modal = document.getElementById("popup");
    modal.style.display = "flex";

    modalContent = document.getElementById("popup-holder").children;

    for (let i = 0; i < modalContent.length; i++) {
        const element = modalContent[i];
        element.style.display = "none";
    }

    content = document.getElementById(tabName);
    content.style.display = "block";
}

// Toogle Drop Down
function ToogleDropDown(event, ddClass){
    if (!DropDownOpen){
        OpenDropDown(event, ddClass);
    }else{
        CloseDropDown(event, ddClass);
    }
}

// Open Drop down
function OpenDropDown(event, ddClass){
    // Rotate
    event.target.style.transform = 'rotate(-90deg)';

    document.querySelector('.ddsmc').classList.add('activeDrop')

    // Update
    DropDownOpen = true;
}
// Close Drop Down
function CloseDropDown(event, ddClass){
    // Return back to normal
    event.target.style.transform = 'rotate(0deg)';

    document.querySelector('.ddsmc').classList.remove('activeDrop');

    // Update
    DropDownOpen = false;
}

// Gender Dropdown Item Click
function ChooseGender(event, gender, inputClass, ddClass){
    var input;
    input = document.querySelector(inputClass);
    input.value = gender;

    // Close Drop Down
    CloseDropDown(event, ddClass);
}

// Tabs
function TabChange(event, ddClass){
    var tabPanel = document.querySelector('.tab-panel').children;
    for (let i = 0; i < tabPanel.length; i++) {
        const element = tabPanel[i];
        element.style.display = 'none';
    }

    var tabHolder = document.querySelector('.tab-holder').children;
    for (let i = 0; i < tabHolder.length; i++) {
        const element = tabHolder[i];
        element.classList.remove('on');
    }
    event.target.classList.add('on');

    var tab = document.querySelector(ddClass);
    tab.style.display = 'block';

 
}