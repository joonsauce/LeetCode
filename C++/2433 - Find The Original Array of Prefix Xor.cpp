vector<int> findArray(vector<int>& pref) {
    vector<int> answer;
    int k, prev = 0;
    answer.push_back(pref[0]);
    for(int i = 1; i < pref.size(); i++) {
        k = pref[i] ^ pref[i - 1];
        answer.push_back(k);
    }
    return answer;
}