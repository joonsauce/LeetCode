bool halvesAreAlike(string s) {
    int s_size = s.size();
    int half_size = s_size >> 1;
    string a;
    string b;
    for (int i = 0; i < half_size; i++) {
        a += s[i];
        b += s[i + half_size];
    }
    int a_count = 0;
    int b_count = 0;
    for (int i = 0; i < half_size; i++) {
        switch (a[i]) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                a_count++;
            default:
                break;
        }
        switch (b[i]) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                b_count++;
            default:
                break;
        }
    }
    return a_count == b_count;
}