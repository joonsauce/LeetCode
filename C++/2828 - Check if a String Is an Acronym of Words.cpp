bool isAcronym(vector<string>& words, string s) {
    string new_s;
    for (int i = 0; i < words.size(); i++) {
        new_s.push_back(words[i][0]);
    }
    return s == new_s;
}