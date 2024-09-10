#include <bits/stdc++.h>
using namespace std;

// Declare global strings for language, plain text, cipher text, and decrypted cipher
string language, plain_text, cipher_text, decrypt_cipher;

int main()
{
    // Declare a key for shifting letters
    int key;

    // Declare maps to store encryption and decryption mappings
    map<char, char> dictionary_lang, dictionary_cipher;

    // Prompt user to enter the language (alphabet) used for encryption
    cout << "Enter your language letters please:\n";
    cin >> language;

    // Prompt user to enter a key for shifting letters
    cout << "Enter the key you want to use in hashing:\n";
    cin >> key;

    // Ignore leftover newline character in the input buffer
    cin.ignore();

    // Create the encryption dictionary by shifting letters by the key value
    for (int i = 0; i < language.length(); i++)
    {
        dictionary_lang[language[i]] = language[(i + key) % language.length()];
    }

    // Prompt user to enter the plain text to be encrypted
    cout << "Enter your plain text please:\n";
    getline(cin, plain_text);

    // Encrypt the plain text using the encryption dictionary
    for (char &c : plain_text)
    {
        if (dictionary_lang.find(c) != dictionary_lang.end())
        {
            cipher_text += dictionary_lang[c]; // Replace with encrypted character
        }
        else
        {
            cipher_text += c; // Leave non-language characters unchanged
        }
    }

    // Output the cipher text (encrypted text)
    cout << "Your cipher text is: " << cipher_text << "\n";

    // Create the decryption dictionary by shifting letters backwards by the key value
    for (int i = 0; i < language.length(); i++)
    {
        dictionary_cipher[language[i]] = language[(i - key + language.length()) % language.length()];
    }

    // Decrypt the cipher text using the decryption dictionary
    for (char &c : cipher_text)
    {
        if (dictionary_cipher.find(c) != dictionary_cipher.end())
        {
            decrypt_cipher += dictionary_cipher[c]; // Replace with decrypted character
        }
        else
        {
            decrypt_cipher += c; // Leave non-language characters unchanged
        }
    }

    // Output the recovered plain text (decrypted text)
    cout << "Recovered plain text : " << decrypt_cipher << "\n";
    return 0;
}
