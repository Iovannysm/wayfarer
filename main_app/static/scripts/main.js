console.log('=== I am in ===');

<<<<<<< HEAD
const textTooLong = function textTooLong(targetElement, appendToElement, text_length){
    if ( targetElement.val().length > text_length ){
        appendToElement.append(`<p class='error'>Text is more than ${text_length} characters, which is a little long<p>`);
    }
}

// Event listener to parent applies to all child
// $('p.Post.Content').on("click", (event) => titleTooLong());

$('#id_title').on('change', (event) => 
    textTooLong($('#id_title'),$('p.Post.Title'), 50)
)

$('#id_content').on('change', (event) => 
    textTooLong($('#id_content'),$('p.Post.Content'), 200)
)
=======
tinymce.init({
  selector: '#textEditor',
  menubar: false,
  
});

tinymce.init({
  selector: '#textEditorCreate',
  menubar: false,
  
});

>>>>>>> development
