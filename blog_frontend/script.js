const apiUrl1 = "http://127.0.0.1:8000/api/blogposts/";
const apiUrl2 = "http://127.0.0.1:8000/blogposts/";

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
        data.forEach((post) => {
          const postElement = document.createElement("div");
          postElement.innerHTML = `
            <h2>${post.title}</h2>
            <p>${post.content}</p>
            <p>${post.pub_date}</p>
            <small>Author: ${post.author.name}</small>
          `;
          blogPostContainer.appendChild(postElement);
        });
      })
      .catch((error) => {
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
document.getElementById("blogForm").addEventListener("submit", function (e) {
  e.preventDefault();

  // formdata
  const title = document.getElementById("title").value;
  const content = document.getElementById("content").value;
  const pubDate = document.getElementById("pubDate").value;
  const author = document.getElementById("author").value;

  const blog = {
    title: title,
    content: content,
    pub_date: pubDate,
    author: author,
  };

  sendDataToApi(apiUrl2, blog);
  // console.log(blog);
  // document.getElementById("blogForm").reset();
  alert("Blog post created successfully!");
});

function sendDataToApi(url, data) {
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      console.log("API response:", response);
    })
    .catch((error) => {
      console.error("error:", error);
    });
}
