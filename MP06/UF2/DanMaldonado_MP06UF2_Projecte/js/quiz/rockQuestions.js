// Obtenim les preguntaes de rock
export async function fetchRockQuestions() {
    // Definim l'URL de l'API amb paràmetres per obtenir preguntes de rock
    const apiUrl = `https://opentdb.com/api.php?amount=10&category=12&type=multiple`;

    const response = await fetch(apiUrl);

    const data = await response.json();

    return data.results;
}
