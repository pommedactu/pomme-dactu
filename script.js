// Chargement et affichage des articles
document.addEventListener('DOMContentLoaded', function() {
    loadArticles();
});

async function loadArticles() {
    try {
        const response = await fetch('articles/index.json');
        const articles = await response.json();
        displayArticles(articles);
    } catch (error) {
        console.log('Aucun article pour le moment');
        displayPlaceholder();
    }
}

function displayArticles(articles) {
    const container = document.getElementById('articles');

    // Trier par date (plus récent en premier)
    articles.sort((a, b) => new Date(b.date) - new Date(a.date));

    container.innerHTML = articles.map(article => `
        <article class="article-card">
            <div class="article-image" style="background: linear-gradient(135deg, ${getGradient()})"></div>
            <div class="article-content">
                <div class="article-date">${formatDate(article.date)}</div>
                <h3 class="article-title">${article.title}</h3>
                <p class="article-excerpt">${article.excerpt}</p>
                <a href="articles/${article.slug}.html" class="read-more">Lire la suite →</a>
            </div>
        </article>
    `).join('');
}

function displayPlaceholder() {
    const container = document.getElementById('articles');
    container.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px;">
            <h3 style="font-size: 1.5em; margin-bottom: 15px; color: #666;">Premier article bientôt disponible</h3>
            <p style="color: #999;">Le premier article sera publié très prochainement. Revenez demain !</p>
        </div>
    `;
}

function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('fr-FR', options);
}

function getGradient() {
    const gradients = [
        '#667eea 0%, #764ba2 100%',
        '#f093fb 0%, #f5576c 100%',
        '#4facfe 0%, #00f2fe 100%',
        '#43e97b 0%, #38f9d7 100%',
        '#fa709a 0%, #fee140 100%'
    ];
    return gradients[Math.floor(Math.random() * gradients.length)];
}
