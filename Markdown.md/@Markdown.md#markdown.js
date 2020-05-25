*[HTML]: HyperText Markup Language

<!HTML>
<head>
<script>
/*
Simple Caesar Cipher example with shifting right 3
look at ANSI character codes
visible characters are from 33 to 122
*/

#include <iostream>
#include <string>

using namespace std;

string CaesarEncrypt () {
    string plainText = "import_java.awt.*;";  // change your text here, pls use '_' instead of spaces
    int strLength = plainText.length();
    for (int i=0; i < strLength; i++) {
            switch(plainText[i]) {
                case 'x':
                    plainText[i] = 33;
                    break;
                case 'y':
                    plainText[i] = 34;
                    break;
                case 'z':
                    plainText[i] = 35;
                    break;
                default:  plainText[i] += 3;
            }
    }
    return plainText;
}
string CaesarDecrypt(string encText) {
    int strLength = encText.length();
    for (int i=0; i < strLength; i++) {
            switch(encText[i]) {
                case 33:
                    encText[i] = 'x';
                    break;
                case 34:
                    encText[i] = 'y';
                    break;
                case 35:
                    encText[i] = 'z';
                    break;
                default: encText[i] -= 3;
            }
    }
    return encText;
}

int main() {
    string encText = CaesarEncrypt();
    cout << "Encrypted text =>  " << encText << endl ;
    string decrText = CaesarDecrypt(encText);
    cout << "Decrypted text =>  " << decrText ;
    
    return 0;
}

</script>
</head>
<body>
</body>
</HTML>
