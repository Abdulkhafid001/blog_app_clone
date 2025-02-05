const apiUrl = "http://127.0.0.1:8000/api/blogposts/";
const getBlogPostBtn = document
  .getElementById("getBlogPostBtn")
  .addEventListener("click", function getAllBlogPosts() {
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response not ok.");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Blog posts:", data);
      })
      .catch((error) => {
        console.error("an error during fetch.");
      });
  });
