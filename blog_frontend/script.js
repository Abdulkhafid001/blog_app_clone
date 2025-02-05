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
        const blogPostContainer = document.getElementById("blogPostContainer");
        data.forEach(post => {
          const postElement = document.createElement("div");
          postElement.innerHTML = `
            <h2>${post.title}</h2>
            <p>${post.content}</p>
            <p>${post.pub_date}</p>
            <small>Author: ${post.author.name}</small>
          `;
        blogPostContainer.appendChild(postElement);
        });
       
      }).catch((error) => {
        console.error("error: " + error);
      });
  });

function addBlogPostsToHtml(data) {
  const blogPostContainer = document.getElementById("blogPostContainer");
  data.forEach((post) => {
    const postElement = document.createElement("div");
    postElement.innerHTML = `
        <h2>${post.title}</h2>
        <p>${post.content}</p>
        <small>Author: ${post.pub_date}</small>
    `;
    blogPostContainer.appendChild(postElement);
  });
}
