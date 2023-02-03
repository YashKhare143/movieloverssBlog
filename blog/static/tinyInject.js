var script = document.createElement("script");
script.type = "text/javascript";
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js";
document.head.appendChild(script);

script.onload = function () {
  
  tinymce.init({
    selector: "#id_content",
    width: 1450,
    height: 900,
    plugins: [
      "a11ychecker",
      "advcode",
      "advlist",
      "anchor",
      "autolink",
      "codesample",
      "fullscreen",
      "help",
      "image",
      "editimage",
      "tinydrive",
      "lists",
      "link",
      "media",
      "powerpaste",
      "preview",
      "searchreplace",
      "table",
      "template",
      "tinymcespellchecker",
      "visualblocks",
      "wordcount",
    ],
    toolbar:
      "undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | " +
      "bullist numlist outdent indent | link image | print preview media fullscreen | " +
      "forecolor backcolor emoticons | help",
    menu: {
      favs: {
        title: "My Favorites",
        items: "code visualaid | searchreplace | emoticons",
      },
    },
    menubar: "favs file edit view insert format tools table help",
    content_css: "css/content.css",
  });
};
