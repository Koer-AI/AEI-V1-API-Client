// --- IMPORTANT: REPLACE WITH YOUR ACTUAL VALUES ---
// This URL should point to your own hosted audio file (public or temporary signed).
const AUDIO_FILE_URL = "YOUR_PUBLIC_OR_SIGNED_AUDIO_FILE_URL_HERE"; // e.g., "https://example.com/audio/sample.mp3"
const YOUR_EMAIL = "your_registered_email@example.com"; // e.g., "johndoe@example.com"
const YOUR_API_KEY = "YOUR_API_KEY_HERE"; // Replace with your actual API key, e.g., "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
// ---------------------------------------------------

// AEI-V1 API Endpoint
// Your actual API endpoint goes here.
const AEI_V1_API_ENDPOINT = "https://api.yourcompany.com/v1/classify-emotion";

/**
 * Sends a POST request to the Emotion Classification API.
 * @returns {Promise<object|string>} A promise that resolves with the JSON response
 * or rejects with an error message.
 */
async function classifyEmotion() {
    console.log("\nSending request to AEI-V1 API...");
    console.log(`Email: ${YOUR_EMAIL}`);
    console.log(`Audio URL: ${AUDIO_FILE_URL}`);

    try {
        // Construct URL with query parameter
        const url = new URL(AEI_V1_API_ENDPOINT);
        url.searchParams.append("audio_path_or_url", AUDIO_FILE_URL);

        // Prepare headers for authentication
        const headers = {
            "Email": YOUR_EMAIL,
            "Authorization": YOUR_API_KEY,
        };

        // Make the POST request using fetch
        const response = await fetch(url.toString(), {
            method: 'POST',
            headers: headers
        });

        // Process the response
        if (response.ok) { // Check if status code is 2xx
            console.log("\n--- API Response (Success) ---");
            const jsonResponse = await response.json();
            console.log(jsonResponse);
            return jsonResponse; // Return the JSON response
        } else {
            const errorText = await response.text();
            let errorMessage = `API Error (Status Code: ${response.status || 'Unknown'}): \n`;
            try {
                const errorJson = JSON.parse(errorText);
                errorMessage += `Details: ${JSON.stringify(errorJson, null, 2)}`;
            } catch (e) {
                errorMessage += `Raw Response: ${errorText}`;
            }
            console.error(errorMessage);
            throw new Error(errorMessage); // Throw an error for non-2xx responses
        }
    } catch (error) {
        console.error("\n--- Network or Request Error ---");
        console.error("Error:", error);
        throw new Error(`An unexpected error occurred: ${error.message}`); // Re-throw network errors
    }
}

// Example of how to call the function (for documentation purposes)
// You would typically call this in your application logic.
// classifyEmotion()
//     .then(result => {
//         console.log("Function call successful:", result);
//         // Handle the successful classification result here
//     })
//     .catch(error => {
//         console.error("Function call failed:", error);
//         // Handle errors during classification here
//     });
