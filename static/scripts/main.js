console.log('=== I am in ===');

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
// text editor
tinymce.init({
  selector: '.post-content-textarea',
  menubar: false,
  
});



