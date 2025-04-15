document.addEventListener("DOMContentLoaded", () => {
  const productList = document.getElementById("productList");
  const addProductForm = document.getElementById("addProductForm");
  const prevPageButton = document.getElementById("prevPage");
  const nextPageButton = document.getElementById("nextPage");
  const currentPageSpan = document.getElementById("currentPage");

  let currentPage = 1; // Default page is 1
  const itemsPerPage = 10; // Default page size is 10

  // Fetch and display products with pagination
  const fetchProducts = async (page, itemsPerPage) => {
    const response = await fetch(
      `/products?page=${page}&per_page=${itemsPerPage}`
    );
    const { products, totalPages } = await response.json();
    productList.innerHTML = "";
    products.forEach((product) => {
      const li = document.createElement("li");
      li.textContent = `${product.name} - ${product.category} - $${product.price}`;
      productList.appendChild(li);
    });
    currentPageSpan.textContent = page;
    prevPageButton.disabled = page === 1;
    nextPageButton.disabled = page === totalPages;
  };

  // Add product
  addProductForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const desc = document.getElementById("desc").value;
    const price = document.getElementById("price").value;
    const category = document.getElementById("category").value;
    const images = document.getElementById("images").value;
    const stock_quantity = document.getElementById("stock_quantity").value;

    await fetch("/products", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        desc,
        price,
        category,
        images,
        stock_quantity,
      }),
    });
  });
  fetchProducts(currentPage, itemsPerPage);

  // Pagination controls
  prevPageButton.addEventListener("click", () => {
    if (currentPage > 1) {
      currentPage--;
      fetchProducts(currentPage);
    }
  });

  nextPageButton.addEventListener("click", () => {
    currentPage++;
    fetchProducts(currentPage);
  });

  fetchProducts(currentPage);
});
