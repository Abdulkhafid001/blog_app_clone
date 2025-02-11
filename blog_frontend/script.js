// const apiUrl1 = "http://127.0.0.1:8000/api/blogposts/";
// const apiUrl2 = "http://127.0.0.1:8000/blogposts/";

// const getBlogPostBtn = document
//   .getElementById("getBlogPostBtn")
//   .addEventListener("click", function getAllBlogPosts() {
//     fetch(apiUrl)
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Network response not ok.");
//         }
//         return response.json();
//       })
//       .then((data) => {
//         console.log("Blog posts:", data);
//         const blogPostContainer = document.getElementById("blogPostContainer");
//         data.forEach((post) => {
//           const postElement = document.createElement("div");
//           postElement.innerHTML = `
//             <h2>${post.title}</h2>
//             <p>${post.content}</p>
//             <p>${post.pub_date}</p>
//             <small>Author: ${post.author.name}</small>
//           `;
//           blogPostContainer.appendChild(postElement);
//         });
//       })
//       .catch((error) => {
//         console.error("error: " + error);
//       });
//   });

// function addBlogPostsToHtml(data) {
//   const blogPostContainer = document.getElementById("blogPostContainer");
//   data.forEach((post) => {
//     const postElement = document.createElement("div");
//     postElement.innerHTML = `
//         <h2>${post.title}</h2>
//         <p>${post.content}</p>
//         <small>Author: ${post.pub_date}</small>
//     `;
//     blogPostContainer.appendChild(postElement);
//   });
// }

// // function to create a blog post in the backend
// document.getElementById("blogForm").addEventListener("submit", function (e) {
//   e.preventDefault();

//   // formdata
//   const title = document.getElementById("title").value;
//   const content = document.getElementById("content").value;
//   const postImage = document.getElementById("postImageUrl").value;
//   const pubDate = document.getElementById("pubDate").value;
//   const author = document.getElementById("author").value;

//   logSomething(postImage);

//   const blog = {
//     title: title,
//     content: content,
//     post_image: postImage,
//     pub_date: pubDate,
//     author: author,
//   };

//   sendDataToApi(apiUrl2, blog);
// });

// function sendDataToApi(apiUrl, data) {
//   fetch(apiUrl, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(data),
//   })
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error("Network response not ok.");
//       }
//       return response.json();
//     })
//     .then((data) => {
//       console.log("Blog post created:", data);
//     })
//     .catch((error) => {
//       console.error("error: " + error);
//     });
// }

// function logSomething(something) {
//   console.log("value: " + something);
// }

// // Mock data for blog posts
// const blogPosts = [
//   {
//     id: 1,
//     title: "First Blog Post",
//     content: "This is the content of the first blog post.",
//     likes: 0,
//     comments: [],
//   },
//   {
//     id: 2,
//     title: "Second Blog Post",
//     content: "This is the content of the second blog post.",
//     likes: 0,
//     comments: [],
//   },
// ];

// // Function to render blog posts
// function renderBlogPosts() {
//   const blogPostsSection = document.getElementById("blog-posts");
//   blogPostsSection.innerHTML = "";

//   blogPosts.forEach((post) => {
//     const postElement = document.createElement("div");
//     postElement.classList.add("blog-post");

//     postElement.innerHTML = `
//           <h2>${post.title}</h2>
//           <p>${post.content}</p>
//           <div class="actions">
//               <button onclick="likePost(${post.id})">Like (${
//       post.likes
//     })</button>
//               <button onclick="sharePost(${post.id})">Share</button>
//           </div>
//           <div class="comments">
//               <h3>Comments</h3>
//               <ul id="comments-${post.id}">
//                   ${post.comments
//                     .map((comment) => `<li>${comment}</li>`)
//                     .join("")}
//               </ul>
//               <input
//                   type="text"
//                   id="comment-input-${post.id}"
//                   placeholder="Add a comment..."
//                   onkeypress="if(event.key === 'Enter') addComment(${post.id})"
//               />
//           </div>
//       `;

//     blogPostsSection.appendChild(postElement);
//   });
// }

// // Function to handle liking a post
// function likePost(postId) {
//   const post = blogPosts.find((post) => post.id === postId);
//   post.likes += 1;
//   renderBlogPosts();
// }

// // Function to handle sharing a post
// function sharePost(postId) {
//   const post = blogPosts.find((post) => post.id === postId);
//   alert(`Sharing post: "${post.title}"`);
// }

// // Function to add a comment
// function addComment(postId) {
//   const commentInput = document.getElementById(`comment-input-${postId}`);
//   const comment = commentInput.value.trim();

//   if (comment) {
//     const post = blogPosts.find((post) => post.id === postId);
//     post.comments.push(comment);
//     commentInput.value = "";
//     renderBlogPosts();
//   }
// }

// // Initial render
// renderBlogPosts();


