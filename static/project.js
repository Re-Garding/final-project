'use strict';
fetch('/dashboard_data')
.then((response) => response.json())
.then((data) => {
  console.log(data);
  const createDivs = (data) => {
    const container = document.querySelector('#dashb');
      container.insertAdjacentHTML('beforeend', `<div id="dashb" 
      <h3> ${data['Question']} </> 
      <br> <br/>
      <ul>
        <span> A </span> 
        <input type="radio" name="ans_choice" id="1" class="ans_choice">
        <label id="a_text"> ${data["A"]}</label>
      </ul>

      <ul>
        <span> B </span> 
        <input type="radio" name="ans_choice" id="1" class="ans_choice">
        <label id="a_text"> ${data["B"]}</label>
      </ul>


      <ul>
        <span> C</span> 
        <input type="radio" name="ans_choice" id="1" class="ans_choice">
        <label id="a_text"> ${data["C"]}</label>
      </ul>

      <ul>
        <span> D </span> 
        <input type="radio" name="ans_choice" id="1" class="ans_choice">
        <label id="a_text"> ${data["D"]}</label>
      </ul>

      <button id="submit" type = "button">Submit</button>
      <br> <br/>
      </div>`

      
      );

      const button = document.querySelector('#submit')
    button.addEventListener('click', () => {

      alert( data["correct_reasoning"]);
    });  
    }
    createDivs(data['daily_quiz'])
    
    const createDictionary = (data) => {
      const container = document.querySelector('#dashb');
        container.insertAdjacentHTML('beforeend', `<div id="dashb" 
        <ul>
          <span> <h3> Word of the Day </h3> </span> 
          
          <h3>
          <label id="text"> Please define in your own words what ${data["words"]} means, after you have thought of an 
          answer go ahead and click reveal, no worries if you didn't quite get it, jot it down on your notes and </label>
          </h3>
          <br> 
          <button id="reveal_text"> Reveal </button>
          <br/> 
        </ul>
        <br> <br/>
        <h3>Add what you learned to your notes! It is a greatway to reinforce your learning!Reference your notes as you continue
        this journey, it will be a great reminder to show how much you have learned so far! <h3/>
        <button id="notes" type = "button"> Notes </button>
        </div>`  

        );

        const button_notes = document.querySelector('#notes')
        button_notes.addEventListener('click', () => {
    
          window.open('http://localhost:5000/notepage').focus();
        });

        const button_word = document.querySelector('#reveal_text')
        button_word.addEventListener('click', () => {
    
          alert( data["word"]);
        });

      }

      
      createDictionary(data['daily_words'])
    });



