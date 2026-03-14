// Простая логика для приветствия и будущих интерактивных действий
window.addEventListener('DOMContentLoaded', function () {
    const today = new Date();
    console.log('CRM швейного цеха загружена', today.toLocaleString());

    // Пример: можно добавить динамику через кнопки, секции, загрузку данных
    const cards = document.querySelectorAll('.card');
    cards.forEach((card) => {
        card.addEventListener('click', () => {
            card.style.opacity = '0.96';
            setTimeout(() => (card.style.opacity = ''), 120);
        });
    });
});